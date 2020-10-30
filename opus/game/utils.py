from django.utils import timezone
import datetime
from pytz import timezone as tz
from user.models import UserProfile

REDIRECT='redirect'

STAY='stay'


DAYS={
    'day1':{
        'start_question':1,
        'end_question':1,
        'branches':[],
        'date':datetime.datetime(2020,10,30,tzinfo=tz('Asia/Kolkata')),
    },
   'day2':{
        'start_question':2,
        'end_question':2,
        'branches':[],
        'date':datetime.datetime(2020,10,31,tzinfo=tz('Asia/Kolkata')),
    },
    'day3':{
        'start_question':3,
        'end_question':3,
        'branches':[],
        'date':datetime.datetime(2020,11,1,tzinfo=tz('Asia/Kolkata')),
    },
    'day4':{
        'start_question':4,
        'end_question':5,
        'branches':[],
        'date':datetime.datetime(2020,11,2,tzinfo=tz('Asia/Kolkata')),
    },
}



def check_day_end(question_number) ->dict:
    now=timezone.localtime()
    
    if now < DAYS['day1']['date']: #Redirect to welcome page
        return {'status':REDIRECT,'day':0}

    for day in range(1,4):
        if now < DAYS['day'+str(day+1)]['date'] and question_number>DAYS['day'+str(day)]['end_question'] and question_number not in DAYS['day'+str(day)]['branches']: 
            return {'status':REDIRECT,'day':day}  #Redirect to particular day end
    

    return {'status':STAY,'day':-1} #Continue





def get_rank(user:UserProfile) ->int:

    pk=user.pk
    rank =1

    people=UserProfile.objects.filter(points__gte=user.points).order_by('-points','pk')

    rank =1

    for person in people:
        if person.pk==pk:
            break
        rank+=1

    return rank
