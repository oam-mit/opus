from django.shortcuts import render,reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm,ProfileForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,template_name="user/index.html")

def signup(request):
    if request.method=="POST":
        u_form=UserForm(request.POST)
        p_form=ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid() and u_form.unique_name():
            u_form.save()
            p=UserProfile(user=User.objects.get(username=u_form.cleaned_data['username']),reg_number=p_form.cleaned_data['reg_number'])
            if p_form.cleaned_data['mob_number']:
                p.mob_number=p_form.cleaned_data['mob_number']
            p.save()
            messages.success(request,"Account Created Successfully")
            return HttpResponseRedirect(reverse('user:login'))
        else:
            messages.error(request,"You may have already Registered")
    else:
        u_form=UserForm()
        p_form=ProfileForm()
    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,template_name="user/signup.html",context=context)


def bot_reply(request):
    import os
    from opus import settings
    import dialogflow_v2 as dialogflow
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.path.join(settings.BASE_DIR,"static/testagent.json")
    dialogflow_session_client=dialogflow.SessionsClient()
    PROJECT_ID="testagent-kvxgyd"
    def detect_intent_text(text,session_id,language_code="en"):
        session=dialogflow_session_client.session_path(PROJECT_ID,session_id)
        text_input=dialogflow.types.TextInput(text=text,language_code=language_code)
        query_input=dialogflow.types.QueryInput(text=text_input)
        response=dialogflow_session_client.detect_intent(session=session,query_input=query_input)
        return response.query_result
    mes=request.GET.get('mes',None)
    response=detect_intent_text(mes,12345)
    return HttpResponse(response.fulfillment_text)