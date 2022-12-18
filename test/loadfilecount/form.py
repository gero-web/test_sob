from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
    

class WordCountForm(forms.Form):
    text = forms.CharField(max_length=50)