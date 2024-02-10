from sampleApp.form import login_form
from django.shortcuts import render

def login_f(request):
    template_name='login.html'
    form1=login_form.login()
    ctx={}
    ctx['form1']=form1
    return render(request,template_name,ctx)