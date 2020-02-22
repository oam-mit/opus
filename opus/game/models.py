from django.db import models

# Create your models here.

class Levels(models.Model):
    level=models.IntegerField(default=1,blank=False)
    description=models.CharField(null=False,max_length=10)

    def __str__(self):
        return (self.description)
    
    class Meta:
        verbose_name_plural='Levels'



class Story_Question(models.Model):
    question_number=models.IntegerField(blank=False,unique=True)
    question=models.TextField(max_length=1000)
    choice_1=models.CharField(max_length=1000,null=True,blank=True)
    choice_2=models.CharField(max_length=1000,null=True,blank=True)
    choice_3=models.CharField(max_length=1000,null=True,blank=True)
    on_good=models.IntegerField(blank=False,default=1001)
    on_medium=models.IntegerField(blank=False,default=1002)
    on_bad=models.IntegerField(blank=False,default=1003)

    def __str__(self):
        return self.question


class Story_Answer(models.Model):
    question=models.OneToOneField(Story_Question,on_delete=models.CASCADE)
    choice_1=models.ForeignKey(to=Levels,on_delete=models.CASCADE,related_name='option_1',null=True,blank=True)
    choice_2=models.ForeignKey(to=Levels,on_delete=models.CASCADE,related_name='option_2',null=True,blank=True)
    choice_3=models.ForeignKey(to=Levels,on_delete=models.CASCADE,related_name='option_3',null=True,blank=True)
   
    def __str__(self):
        return (self.question.question)

class Aptitude_Question(models.Model):
    story=models.ForeignKey(Story_Question,on_delete=models.CASCADE)
    question_number=models.IntegerField(default=1)
    question=models.CharField(max_length=1000)
    answer=models.CharField(null=True,max_length=1000,blank=True)
    
    
    


