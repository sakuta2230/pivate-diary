from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import blogcon

class InquiryForm(forms.Form):
    name=forms.CharField(label="名前")
    email=forms.EmailField(label="メールアドレス")

class Registerform(forms.ModelForm):
    class Meta:
        model=blogcon
        fields=['title','date','Contents','is_publick']
        labels={'title':'タイトル','date':'日付','Contents':'内容','is_publick':'公開設定'}

class Loginform(AuthenticationForm):
    def __int__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
