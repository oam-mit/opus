from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,HttpResponsePermanentRedirect,HttpResponseForbidden
from django.utils import timezone
from django.db.models import Count,Q
from django.contrib import messages as mess
from .decorators import staff_not_required


from .models import Story_Question,Story_Options,Aptitude_Question
from .utils import check_day_end,REDIRECT,STAY,get_rank

from user.models import UserProfile,Winners
from user.forms import ProfileUpdateForm,UserUpdateForm







def check_staff(request): #Only non-staff members are allowed to play
    if request.user.is_staff:
        return HttpResponseRedirect(reverse("admin:index"))
    else:
        return HttpResponseRedirect(reverse("game:index"))

# Create your views here.
@login_required
@staff_not_required
def index(request):

    

    if request.user.userprofile.is_story is False:   #Player is on an aptitude question
        return redirect(reverse("game:aptitude"))

    
    

    else: 
        status=check_day_end(request.user.userprofile.story)                                           #Player is on story question
        if status['status']!=STAY:
            if status['day']>0:
                return redirect(reverse('game:day_ending',args=[status['day']]))
            else:
                return redirect(reverse('game:welcome'))

        
        try:
            story=Story_Question.objects.get(question_number=request.user.userprofile.story)
                                                     #Get the story question player is on

        except:                                      #No such story question exists, which means he has completed the game
            request.user.userprofile.is_ended=True   #Set flag to false 
            request.user.userprofile.save()
            return HttpResponseRedirect(reverse('game:game_end')) #Redirect to game end

        table = UserProfile.objects.getLeaderboard()
    
        number=int(12/story.story_options_set.count())

        context={
            'toppers':table,
            'story':story,
            'number':number,
        }
       
        return render(request,template_name='game/index.html',context=context)
    
   



@login_required
@staff_not_required
def check_story(request,option):
    if request.user.userprofile.is_story is False: #User is not on story question
        return HttpResponseRedirect(reverse("game:aptitude")) #Redirect to aptitude

    question_set=Story_Options.objects.filter(question__question_number=request.user.userprofile.story)

    if option >question_set.count() or option <0: #Invalid response
        return HttpResponseForbidden('Not allowed')

    selected_option=question_set[option-1] #Get selected option
    
    request.user.userprofile.path=selected_option.level.level #Set the level
    
    #Setting story to false
    request.user.userprofile.is_story=False
    
    request.user.userprofile.save()
   
    return redirect(reverse('game:index'))



@login_required
@staff_not_required
def aptitude(request):
    from . forms import AptitudeForm
    
    if request.user.userprofile.is_story is True: #User is on story question
        return HttpResponseRedirect(reverse("game:index"))

    try:
        question=Aptitude_Question.objects.get(story__question_number=request.user.userprofile.story,question_number=request.user.userprofile.current_aptitude) #Get the current aptitude question from the story question he is on

    except: #No aptitude question exists
        request.user.userprofile.is_story=True #Set story flag to true
        selected_option=Story_Options.objects.get(question__question_number=request.user.userprofile.story,level__level=request.user.userprofile.path)
        

        request.user.userprofile.story=selected_option.on_chosen

        request.user.userprofile.current_aptitude=1
        request.user.userprofile.points+=selected_option.level.points
        request.user.userprofile.last_answered=timezone.now()
        request.user.userprofile.save()
        return HttpResponseRedirect(reverse('game:index'))

    form=AptitudeForm()
    table = UserProfile.objects.getLeaderboard()
    
    context={
        'form':form,
        'question':question,
        'toppers':table,

    }
    return render(request,template_name='game/aptitude.html',context=context)

@staff_not_required
def check_aptitude(request):
    from .forms import AptitudeForm
    if request.method=='POST':

        ip=request.POST.get('ans').lower().replace(" ","") #Format the response
        
        answer=Aptitude_Question.objects.get(story__question_number=request.user.userprofile.story,question_number=request.user.userprofile.current_aptitude).answer.lower().replace(" ","")
        if ip == answer: #Corect answer
            request.user.userprofile.current_aptitude+=1
        else:
            return HttpResponse("wrong")

        if request.user.userprofile.current_aptitude>request.user.userprofile.path: #User has answered all aptitude questions expected
            request.user.userprofile.is_story=True

            selected_option=Story_Options.objects.get(question__question_number=request.user.userprofile.story,level__level=request.user.userprofile.path)

            request.user.userprofile.story=selected_option.on_chosen
    
            request.user.userprofile.current_aptitude=1
            request.user.userprofile.points+=selected_option.level.points
            request.user.userprofile.last_answered=timezone.now()
        request.user.userprofile.save()
        return HttpResponse("correct")
    
    else:
        return HttpResponse("Not Allowed")



@login_required
@staff_not_required
def day_ending(request,day):
    status=check_day_end(request.user.userprofile.story)
    if status['status']!=REDIRECT or status['day']!=day:
        return redirect(reverse('game:index'))
    table = UserProfile.objects.getLeaderboard()
    context={
        'toppers':table,
        'day':day,
    }

    return render(request,'game/day_ending.html',context=context)


@login_required
def profile(request):

    rank=get_rank(request.user.userprofile)
    
    

    if request.method=='POST':
      profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
      user_form=UserUpdateForm(request.POST,instance=request.user)
      if profile_form.is_valid() and user_form.is_valid():
        mess.success(request,'Successfully changed your Profile')
        profile_form.save()
        user_form.save()
        return HttpResponseRedirect(reverse('game:profile'))
    else:
        profile_form=ProfileUpdateForm(instance=request.user.userprofile)
        user_form=UserUpdateForm(instance=request.user)
   
    context={
        'rank':rank,
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return (render(request,'game/profile.html',context))


@login_required
@staff_not_required
def game_end(request):
    if request.user.userprofile.is_ended==False:
        return HttpResponseRedirect(reverse('game:index'))
    
    winner,created=Winners.objects.get_or_create(user=request.user.userprofile)
    table = UserProfile.objects.getLeaderboard()
    context={
        'toppers':table,
    }

    return render(request,template_name='game/game_end.html',context=context)


def welcome(request):
    status=check_day_end(request.user.userprofile.story)

    if status['status']!=REDIRECT or status['day']>0:
        return redirect(reverse('game:index'))
    
    return render(request,'game/welcome.html')