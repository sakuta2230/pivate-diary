from .views import detail1,index1,list1, login_view,login_yobi,signup_view,logout_view
from django.urls import path
app='sampleApp'
urlpatterns=[
   path('',index1.index,name='index'),
   path('list',list1.list,name='list'),
   path('detail/<int:pk>',detail1.detail,name='detail'),
   path('login_yobi',login_yobi.login_f,name='login_yobi'),
   path('login',login_view.loginfunc,name='login'),
   path('logout',logout_view.logoutfunc,name='logout'),
   path('signup',signup_view.signupfunc,name='signup')
]