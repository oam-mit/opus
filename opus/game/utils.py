from django.utils import timezone
import datetime
from pytz import timezone as tz

DAYS={
    'day1':{'question_number':4,'date':datetime.datetime(2020,10,5,tzinfo=tz('Asia/Kolkata'))},
    'day2':{'question_number':10,'date':datetime.datetime(2020,10,6,tzinfo=tz('Asia/Kolkata'))},
    'day3':{'question_number':100,'date':datetime.datetime(2020,10,7,tzinfo=tz('Asia/Kolkata'))},
    'day4':{'question_number':200,'date':datetime.datetime(2020,10,8,tzinfo=tz('Asia/Kolkata'))}
}



def check_day_end():
    now=timezone.localtime()
  


    print(now)

    return None

