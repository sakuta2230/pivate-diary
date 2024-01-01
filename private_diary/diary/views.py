from django.views.generic import ListView,UpdateView,CreateView
from django.views.generic import FormView,DetailView,DeleteView
from .models import blog,blogcon
from django.shortcuts import render
from .forms import InquiryForm,Registerform
from .forms import Registerform,Loginform
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
class InquiryView(FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm


# Create your views here.
def index(request):
    return render(request,"index.html")

class bloglist(LoginRequiredMixin,ListView):
    model=blogcon
    template_name ="blog_list.html"
    context_object_name = "contents"

class blogdetail(DetailView):

    model=blogcon
    template_name = "blog_detail.html"

def add(request):
    form=Registerform(request.POST)
    if form.is_valid():
       form.save()
    context={'rcontent':form}
    return render(request,"add.html",context)

class update(UpdateView):
    model=blogcon
    form_class = Registerform
    template_name="update.html"
    success_url = reverse_lazy("list")
    #def get_success_url(self):
        #return reverse("detail",kwargs={"pk":self.object.id})

class blogdelete(DeleteView):
    template_name = "blog_delete.html"
    model =blogcon

class login(LoginView):
    template_name="Login.html"


class logout(LogoutView):
    template_name = "logout.html"

def signupfunc(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=User.objects.create_user(username, "", password)
        return render(request,"signup.html",{"context": "新規登録完了"})
    if request.method=="GET":
        return render(request,"signup.html",{"context":"新規登録してください"})



