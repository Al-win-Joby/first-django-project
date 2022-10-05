from . import views

from django.urls import path

urlpatterns = [
     path('',views.landingpage,name="landingpage"),
    path('login', views.loginn,name="login"),
    path('signup',views.signup,name="signup"),
    path('signedup',views.signedup,name="signedup"),
    path('loggedin',views.loggedin,name="loggedin"),
    path('signed_up',views.signed_up,name="signed_up"),
    path('verify',views.verify,name="verify"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('home',views.home,name="home"),
    path('adminn',views.adminlogin,name="adminlogin"),
    path('adminloggedin',views.adminloggedin,name="adminloggedin"),
    path("createadminuser",views.createadminuser,name="createadminuser"),
    path('addadminuser',views.addadminuser,name="addadminuser"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('edit/<int:pk>',views.edit1,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('logout',views.logout1,name="logout"),
    #path('adminlogout',views.logout12,name='adminlogout')

]
