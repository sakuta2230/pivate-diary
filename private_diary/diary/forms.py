from django import forms

class InquiryForm(forms.Form):
    name=forms.CharField(label="名前")
    email=forms.EmailField(label="メールアドレス")