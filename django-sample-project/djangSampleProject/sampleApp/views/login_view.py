from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
def loginfunc(request):    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('list')
        else :
            return render(request,'login.html',{'loginuser':username+'はログインに失敗しました'})
    else:
        return render(request,'login.html',{'loginuser':'ログインしてください'})