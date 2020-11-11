from django.shortcuts import render,reverse

from django.contrib.auth.models import User


from user.models import UserProfile
from game.utils import get_rank

from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.db.models import Q,Count


# Create your views here.
def index(request,reg_number):
    try:
        profile=UserProfile.objects.get(reg_number=reg_number)
    except:
        raise Http404()


    rank=get_rank(profile)

    context={
        'profile':profile,
        'rank':rank,
    }

    return render(request,template_name="viewing/index.html",context=context)


def search(request):
   
    queries=request.POST.get('reg').split()
 
    profiles=[]
    for query in queries:
        profile=UserProfile.objects.filter(Q(user__first_name__icontains=query)|Q(user__last_name__icontains=query)|Q(reg_number__icontains=query)).distinct()
            
        for p in profile:
            profiles.append(p)
        profiles=list(set(profiles))
    
        return render(request,template_name="viewing/search.html",context={'profiles':profiles})
    


    

    
