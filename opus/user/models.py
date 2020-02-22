from django.db import models
from django.contrib.auth.models import User

from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    reg_number=models.IntegerField(unique=True,error_messages={'unique':'Registration number already Exists'})
    mob_number=models.CharField(max_length=15,null=True)
    image=models.ImageField(upload_to='DPs',default='default.jpg')
    story=models.IntegerField(default=1)
    points=models.IntegerField(default=0)
    is_story=models.BooleanField(default=True)
    path=models.IntegerField(default=1)
    current_aptitude=models.IntegerField(default=1)
    is_ended=models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name +" " +self.user.last_name+"--->"+str(self.reg_number)
    
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height>200 or img.width>200:
            op=(200,200)
            img.thumbnail(op)
            img.save(self.image.path)
