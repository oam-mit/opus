from django.shortcuts import render
from user.models import UserProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def get_rank(request,registration_number):
    users=UserProfile.objects.order_by('-points')
    found=0
    rank=1
    for user in users:
        if user.reg_number==registration_number:
            found=1
            break
        rank+=1
    if found==1:
        context={
            'rank':rank
        }
    else:
        context={
            'rank':'Not found'
        }
    return Response(context)
