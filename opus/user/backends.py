from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.contrib.auth.models import User

UserModel = get_user_model()

class RegistrationNumberBackend(ModelBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user =User.objects.get(userprofile__reg_number=username) 
            # user=userprofile.user
        except :
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
    
    # def user_can_authenticate(self, user):
    #     """
    #     Reject users with is_active=False and with staff status. Custom user models that don't have
    #     that attribute are allowed.
    #     """
    #     is_active = getattr(user, 'is_active', None)
    #     is_staff=getattr(user,'is_staff',None)
    #     return (not is_staff and is_active) or is_active is None
