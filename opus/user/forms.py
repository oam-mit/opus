from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

from PIL import Image

class UserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'abc_123','class':'col-12'}),
        help_text="<ul><li>Username should be unique</li></ul>")
    
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'XXXXXXXXXXX','class':'col-12'}),
        help_text="<ol><li>Passwords are not stored in Raw form. Hence, even the admins cannot see your password</li><li>Password should not be too similar to your username</li><li><b>Password should not be entirely Numeric</b></li></ol>",
        label="Password")
    
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'col-12','placeholder':'First Name'}),label="Firstname")
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'col-12','placeholder':'Last Name'}),label="Lastname")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'col-12','placeholder':'xyz@xyz.com'}),help_text="If you forget your password, then your Email ID will be used to reset it.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)
    

    class Meta:
        fields=['username','first_name','last_name','email','password1']
        model=User

    def unique_name(self):
        name=self.cleaned_data['first_name']
        surname=self.cleaned_data['last_name']
        try: 
            User.objects.get(first_name=name,last_name=surname)
            return False
        except:
            return True

    
    def save(self,commit=True):
        user=super(UserForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.username=self.cleaned_data['username']
        if commit:
            user.save()
        
        return user

class ProfileForm(forms.ModelForm):
    reg_number=forms.CharField(widget=forms.NumberInput(attrs={'class':'col-12'}),label="Registration Number <br>(Non-MAHE students should enter phone number)",
        error_messages={'unique':'Registration number already Exists'})
    mob_number=forms.CharField(widget=forms.TextInput(attrs={'class':'col-12'}),label="Mobile Number",min_length=10,max_length=15,required=False)
    class Meta:
        model=UserProfile
        fields=['reg_number','mob_number']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['image']
    
class UserUpdateForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False,label="")
    class Meta:
        model=User
        fields=['username']


from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}),
        label="Enter Username or Registration Number")
    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s or Registration Number and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': ("This account is inactive."),
    }


from django.contrib.auth.views import LoginView
class CustomLoginView(LoginView):
    form_class=CustomAuthenticationForm

