from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
def signupfunc(request):    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(password)
        try:
            User.objects.create_user(username,'',password)
        except IntegrityError :
            return render(request,'signup.html',{'error':'このユーザー名はすでに使用されています'})
    
    return render(request,'signup.html',{'error':'ユーザー登録してください'})