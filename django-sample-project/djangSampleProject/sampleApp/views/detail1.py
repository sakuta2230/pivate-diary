from django.shortcuts import render,get_object_or_404
from sampleApp.model import article1
def detail(request,pk):
    object=get_object_or_404(article1.article, pk=article1.article.pk)
    return render(request,detail.html,{'object':object})