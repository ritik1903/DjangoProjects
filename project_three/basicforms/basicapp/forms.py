from django import forms
from django.core import validators




class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter your email again:')
    text=forms.CharField(widget=forms.Textarea)


    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure email match!")


    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidateError("GOTCHA BOT!")
        return botcatcher
