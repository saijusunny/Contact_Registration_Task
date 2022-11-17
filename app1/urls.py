from django.urls import path
from . import views
urlpatterns = [
    path('allcont/', views.all_cont,name='allcont'),
    path('addcont/', views.add_cont,name='addcont'),
    path('editcont/<int:id>', views.edit_cont,name='editcont'),
    path('viewcont/<int:id>', views.one_cont,name='onecont'),
    path('deletecont/<int:id>', views.delete_cont,name='deletecont'),
    path('usercreate/', views.usercreate, name='usercreate'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('', views.loginpage, name='loginpage'),
    path('signup/', views.signup, name='signup'),
   
]
