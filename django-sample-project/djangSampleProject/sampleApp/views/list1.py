from django.shortcuts import render
from sampleApp.model import article1
from django.contrib.auth.decorators import login_required

@ login_required
def list(request):
    article_list=article1.article.objects.all()
    return render(request,'list.html',{'article_list':article_list})