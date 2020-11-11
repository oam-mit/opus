from django.core.management.base import BaseCommand
from  user.models import UserProfile


from opus.settings import EMAIL_HOST_USER,EMAIL_HOST_PASSWORD,DEFAULT_FROM_EMAIL
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Q

class Command(BaseCommand):
    help = 'Send mail to Players who have not updated userid yet'

    def handle(self,*args,**kwargs):
        users=UserProfile.objects.filter(Q(userid__isnull=True)|Q(userid__exact='')).values_list('reg_number','user__email','user__first_name','user__last_name',flat=False)

        if users.count()>0:

            messages=[]

            for reg_number,email,first_name,last_name in users:
                html=render_to_string('user/userid_mail.html',context={'first_name':first_name,'last_name':last_name})
                plain_message=strip_tags(html)
                self.stdout.write(reg_number+" "+email)
                messages.append(("Reminder for submitting UserId to Hopeless Opus, Acumen",plain_message,DEFAULT_FROM_EMAIL,[email],html))

            connection = get_connection(
            username=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD, fail_silently=False)

            
            final_messages=[]

            for subject,text,from_email,recipient,html  in messages:
                message = EmailMultiAlternatives(subject, text, from_email,to=recipient)
                message.attach_alternative(html, 'text/html')

                final_messages.append(message)
            try:
                connection.send_messages(final_messages)
                self.stdout.write(self.style.SUCCESS(f'Sent email {users.count()} participants'))
            
            except Exception as e:
                self.stdout.write(self.style.WARNING('Some error occurred\n' + str(e)))
        else:
            self.stdout.write(self.style.SUCCESS('Everyone has submitted their Userids!!'))






        


