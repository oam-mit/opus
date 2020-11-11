from django.db import models

# Create your models here.

class Levels(models.Model):
    level=models.IntegerField(default=1,blank=False)
    description=models.CharField(null=False,max_length=10)
    points=models.IntegerField()

    def __str__(self):
        return (self.description)
    
    class Meta:
        verbose_name_plural='Levels'



class Story_Question(models.Model):
    question_number=models.IntegerField(blank=False,unique=True)
    question=models.TextField(max_length=10000)

    def __str__(self):
        return self.question


class Story_Options(models.Model):
    question=models.ForeignKey(to=Story_Question,on_delete=models.CASCADE)
    level=models.ForeignKey(to=Levels,on_delete=models.CASCADE)
    option=models.TextField(max_length=10000)
    on_chosen=models.IntegerField()

    def __str__(self):
        return self.option +"--->"+self.level.description
    
    class Meta:
        unique_together=[['question','level']]
        ordering=['pk']





class Aptitude_Question(models.Model):
    story=models.ForeignKey(Story_Question,on_delete=models.CASCADE)
    question_number=models.IntegerField(default=1)
    question=models.TextField(max_length=1000)
    answer=models.CharField(null=True,max_length=1000,blank=True)
    

    def __str__(self):
        return self.question
    
    class Meta:
        unique_together=[['story','question_number']]
    

