from django.utils import timezone
import datetime
from pytz import timezone as tz
from user.models import UserProfile

REDIRECT='redirect'

STAY='stay'


DAYS={
    'day1':{
        'start_question':1,
        'end_question':18,
        'branches':[95,96,97,98,103,104],
        'date':datetime.datetime(2020,11,5,00,00,00,00,tzinfo=tz('Asia/Kolkata')),
    },
   'day2':{
        'start_question':19,
        'end_question':42,
        'branches':[105,106,99,100,109,110,111,112,113,114,115,116,101,102],
        'date':datetime.datetime(2020,11,6,tzinfo=tz('Asia/Kolkata')),
    },
    'day3':{
        'start_question':43,
        'end_question':72,
        'branches':[117,118,119,120,107,108,121,122,123,124,137,138,125,126,139,140,127,128],
        'date':datetime.datetime(2020,11,7,tzinfo=tz('Asia/Kolkata')),
    },
    'day4':{
        'start_question':73,
        'end_question':94,
        'branches':[129,130,131,132,143,144,133,134,145,146,147,148,135,136],
        'date':datetime.datetime(2020,11,8,tzinfo=tz('Asia/Kolkata')),
    },
}


BRANCHES=list(range(95,149))



def check_day_end(question_number) ->dict:
    now=timezone.localtime()
    print(now)

    # print("now: ",now.date())

    # print("day1: ",DAYS['day1']['date'].date())
    
    if now.date() < DAYS['day1']['date'].date(): #Redirect to welcome page
        return {'status':REDIRECT,'day':0}

    for day in range(1,4):
        if (now.date() < DAYS['day'+str(day+1)]['date'].date()) and (question_number>DAYS['day'+str(day)]['end_question']) and (question_number not in BRANCHES): 
            return {'status':REDIRECT,'day':day}  #Redirect to particular day end
    
    if now.date() > DAYS['day4']['date'].date():
        return {'status':REDIRECT,'day':4}

    return {'status':STAY,'day':-1} #Continue





def get_rank(user:UserProfile) ->int:

    pk=user.pk
    rank =1

    people=UserProfile.objects.filter(points__gte=user.points).exclude(user__is_active=False).order_by('-points','last_answered')

    rank =1

    for person in people:
        if person.pk==pk:
            break
        rank+=1

    return rank
