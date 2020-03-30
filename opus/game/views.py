from django.shortcuts import render,reverse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Story_Question
from django.http import HttpResponseRedirect,HttpResponse,HttpResponsePermanentRedirect
from user.models import UserProfile

from django.utils import timezone

from user.forms import ProfileUpdateForm,UserUpdateForm

from django.contrib import messages as mess

def check_staff(request):
    if request.user.is_staff:
        from django.contrib.auth import logout
        logout(request)
        mess.error(request,"Sorry, Staff is not allowed to Play",extra_tags="danger")
        return HttpResponseRedirect(reverse("user:login"))
    else:
        return HttpResponseRedirect(reverse("game:index"))

# Create your views here.
@login_required
def index(request):
    if request.user.userprofile.is_story is False:
        return redirect(reverse("game:aptitude"),permanent=True)
 
    # if now == 14 and request.user.userprofile.story == 20:
    #     return HttpResponseRedirect(reverse('game:day_ending',args=[1]))
    # elif now==15 and request.user.userprofile.story==40:
    #     return HttpResponseRedirect(reverse('game:day_ending',args=[2]))
    # elif now==16 and request.user.userprofile.story==60:
    #     return HttpResponseRedirect(reverse('game:day_ending',args=[3]))
    
    else:
        number=0
        now=timezone.now().date().day
        try:
            story=Story_Question.objects.get(question_number=request.user.userprofile.story)
        except:
            request.user.userprofile.is_ended=True
            request.user.userprofile.save()
            return HttpResponseRedirect(reverse('game:game_end'))

        table = UserProfile.objects.order_by('-points').exclude(user=User.objects.get(username='omkar').pk)[:5]
    
        if story.choice_1 is not None:
            number+=1
        if story.choice_2 is not None:
            number+=1
        if story.choice_3 is not None:
            number+=1
        number=int(12/number)

        context={
            'toppers':table,
            'story':story,
            'number':number,
        }
        return render(request,template_name='game/index.html',context=context)
    
   



@login_required
def check_story(request,option):
    if request.user.userprofile.is_story is False:
        return HttpResponseRedirect(reverse("game:aptitude"))
    question=Story_Question.objects.get(question_number=request.user.userprofile.story)

    #Increasing the story number
    #request.user.userprofile.story=request.user.userprofile.story+1

    if option >3 or option <0:
        return HttpResponse("Bad Response")

    if option==1:
        request.user.userprofile.path=question.story_answer.choice_1.level
    elif option==2:
        request.user.userprofile.path=question.story_answer.choice_2.level
    elif option==3:
        request.user.userprofile.path=question.story_answer.choice_3.level


    # level=''
    # #Checking option    
    # if option==1:
    #     level=question.story_answer.option_1
    # elif option==2:
    #     level=question.story_answer.option_2
    # elif option==3:
    #     level=question.story_answer.option_3
    
    # if level.lower() == 'good'.lower():
    #     request.user.userprofile.path=1
    # elif level.lower() == 'medium'.lower():
    #     request.user.userprofile.path=2
    # elif level.lower()=='bad'.lower():
    #     request.user.userprofile.path=3

    # else:
    #     return HttpResponse("Bad Request")
    
    #Setting story to false
    request.user.userprofile.is_story=False
        



    request.user.userprofile.save()
    return HttpResponseRedirect(reverse('game:aptitude'))

@login_required
def aptitude(request):
    from . forms import AptitudeForm
    
    if request.user.userprofile.is_story is True:
        return HttpResponseRedirect(reverse("game:index"))

    try:
        q=Story_Question.objects.get(question_number=request.user.userprofile.story).aptitude_question_set.get(question_number=request.user.userprofile.current_aptitude)
    except:
        request.user.userprofile.is_story=True
        if request.user.userprofile.path==1:
            request.user.userprofile.story=Story_Question.objects.get(question_number=request.user.userprofile.story).on_good
        elif request.user.userprofile.path==2:
            request.user.userprofile.story=Story_Question.objects.get(question_number=request.user.userprofile.story).on_medium
        else:
            request.user.userprofile.story=Story_Question.objects.get(question_number=request.user.userprofile.story).on_bad
        request.user.userprofile.current_aptitude=1
        request.user.userprofile.points+=request.user.userprofile.path+3*(3-request.user.userprofile.path)
        request.user.userprofile.save()
        return HttpResponseRedirect(reverse('game:index'))

    form=AptitudeForm()
    table = UserProfile.objects.order_by('-points').exclude(user=User.objects.get(username='omkar').pk)[:5]
    
    context={
        'form':form,
        'question':q,
        'toppers':table,

    }
    return render(request,template_name='game/aptitude.html',context=context)


def check_aptitude(request):
    from .forms import AptitudeForm
    if request.method=='POST':
        ip=request.POST.get('ans').lower().replace(" ","")
        answer=Story_Question.objects.get(question_number=request.user.userprofile.story).aptitude_question_set.get(question_number=request.user.userprofile.current_aptitude).answer.lower().replace(" ","")
        if ip == answer:
            request.user.userprofile.current_aptitude+=1
        else:
            return HttpResponse("wrong")
        if request.user.userprofile.current_aptitude>request.user.userprofile.path:
            request.user.userprofile.is_story=True
            if request.user.userprofile.path==1:
                request.user.userprofile.story=Story_Question.objects.get(question_number=request.user.userprofile.story).on_good
            elif request.user.userprofile.path==2:
                request.user.userprofile.story=Story_Question.objects.get(question_number=request.user.userprofile.story).on_medium
            else:
                request.user.userprofile.story=Story_Question.objects.get(question_number=request.user.userprofile.story).on_bad
            request.user.userprofile.current_aptitude=1
            request.user.userprofile.points+=request.user.userprofile.path+3*(3-request.user.userprofile.path)
        request.user.userprofile.save()
        return HttpResponse("correct")
    
    else:
        return HttpResponse("Not Allowed")



@login_required
def day_ending(request,day):
    #date=datetime.datetime.now()
    # if not (date.day == 14 and request.user.userprofile.story == 20) and not (date.day==15 and request.user.userprofile.story==40) and not (date.day==16 and request.user.userprofile.story==60):
    #     return HttpResponseRedirect(reverse('game:index'))
    table = UserProfile.objects.order_by('-points').exclude(user=User.objects.get(username='omkar').pk)
    context={
        'toppers':table,
        'day':day,
    }

    return render(request,'game/day_ending.html',context=context)


@login_required
def profile(request):
    obj=UserProfile.objects.order_by('-points')
    rank=1
    for i in obj :
        if i.reg_number==request.user.userprofile.reg_number:
            break
        rank+=1
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
def game_end(request):
    if request.user.userprofile.is_ended==False:
        return HttpResponseRedirect(reverse('game:index'))
    table = UserProfile.objects.order_by('-points').exclude(user=User.objects.get(username='omkar').pk)
    context={
        'toppers':table,
    }

    return render(request,template_name='game/game_end.html',context=context)