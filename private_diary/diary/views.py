from django.shortcuts import render
from django.http import HttpResponse
from .forms import InquiryForm
from django.views import generic

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm


# Create your views here.
def index(request):
    return render(request,"index.html")

#def hello(request):
    #return render(request,"index.html")