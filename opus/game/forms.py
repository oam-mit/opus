from django import forms

class AptitudeForm(forms.Form):
    answer=forms.CharField(max_length=1000,label="",widget=forms.TextInput(attrs={'placeholder':'Enter your answer here'}))