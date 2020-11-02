from django.db import models
from django.contrib.auth.models import User

from PIL import Image

from .managers import UserProfileManager

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    reg_number=models.CharField(unique=True,error_messages={'unique':'Registration number already Exists'},max_length=15)
    mob_number=models.CharField(max_length=15,null=True)
    image=models.ImageField(upload_to='DPs',default='default.jpg')
    story=models.IntegerField(default=1)
    points=models.IntegerField(default=0)
    is_story=models.BooleanField(default=True)
    path=models.IntegerField(default=1)
    current_aptitude=models.IntegerField(default=1)
    is_ended=models.BooleanField(default=False)
    userid=models.CharField(max_length=15,null=True,blank=True)
    last_answered=models.DateTimeField(null=True,blank=True)

    objects=UserProfileManager()

    def __str__(self):
        return self.user.first_name +" " +self.user.last_name+"--->"+str(self.reg_number)
    
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height>200 or img.width>200:
            op=(200,200)
            img.thumbnail(op)
            img.save(self.image.path)


class Winners(models.Model):
    user=models.ForeignKey(to=UserProfile,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.reg_number