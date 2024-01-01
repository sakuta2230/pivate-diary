from django.urls import path
from . import views
from .views import signupfunc
urlpatterns=[#path("hello",views.index,name="hello"),
 path("",views.index,name="home"),
 path("inquiry",views.InquiryView.as_view(),name="inquiry"),
 path("list",views.bloglist.as_view(),name="list"),
 path("detail/<int:pk>/",views.blogdetail.as_view(),name="detail"),
 path("add",views.add,name="add"),
path("update/<int:pk>/",views.update.as_view(),name="update"),
path("delete/<int:pk>/",views.blogdelete.as_view(),name="delete"),
 path("login",views.login.as_view(),name="login"),
 path("logout",views.logout.as_view(),name="logout"),
 path("signup/",signupfunc,name="signup"),
]
