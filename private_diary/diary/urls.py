from django.urls import path
from . import views
urlpatterns=[#path("hello",views.index,name="hello"),
 path("",views.index,name="index"),
  path("inquiry",views.InquiryView.as_view(),name="inquiry")
]
