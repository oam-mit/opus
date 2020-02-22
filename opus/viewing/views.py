from django.shortcuts import render,reverse

from django.contrib.auth.models import User
from user.models import UserProfile

from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def index(request,reg_number):
    try:
        profile=UserProfile.objects.get(reg_number=reg_number)
    except:
        return render(request,template_name="viewing/notfound.html")

    obj=UserProfile.objects.order_by('-points')
    rank=1
    for i in obj :
        if i.reg_number==profile.reg_number:
            break
        rank+=1
    

    


    obj=obj[:5]

    context={
        'profile':profile,
        'rank':rank,
        'toppers':obj,
    }

    return render(request,template_name="viewing/index.html",context=context)

def search(request):
    try:
        profile=UserProfile.objects.get(reg_number=request.POST.get('reg'))
        return render(request,template_name="viewing/search.html",context={'profile':profile})
    except:
        return render(request,template_name="viewing/search.html",context={'profile':"No Records"})

    
