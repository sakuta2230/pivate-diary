from django import forms
from django.core.exceptions import ValidationError

class login(forms.Form):
    name=forms.CharField()
    passward=forms.CharField()
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")

        if password:
            if len(password) < 4:
                raise ValidationError("4文字以下は使用できません")
            
                    
                