from django.shortcuts import render,reverse

from django.contrib.auth.models import User
from user.models import UserProfile

from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q,Count


# Create your views here.
def index(request,reg_number):
    try:
        profile=UserProfile.objects.get(reg_number=reg_number)
    except:
        return render(request,template_name="viewing/notfound.html")

    obj=UserProfile.objects.filter(points__gte=profile.points).order_by('-points','pk')

    rank_obj=obj.annotate(rank=Count('pk',filter=Q(pk__lt=request.user.userprofile.pk))).first()

 
 

    rank=rank_obj.rank+1
    # rank=1
    # for i in obj :
    #     if i.reg_number==profile.reg_number:
    #         break
    #     rank+=1
    

    


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
        pass
    try:
        queries=request.POST.get('reg').split()
        profiles=[]
        for query in queries:
            profile=UserProfile.objects.filter(Q(user__first_name__contains=query)|Q(user__last_name__contains=query)).distinct()
            for p in profile:
                profiles.append(p)
        profiles=list(set(profiles))
        return render(request,template_name="viewing/search.html",context={'profiles':profiles})
    except:
        return render(request,template_name="viewing/search.html",context={'profile':"No Records"})


    

    
