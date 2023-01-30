from django.urls import path
from.import views
app_name='app6'
urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('registerimage/',views.registerimage,name='registerimage'),
    path('homeimage/<int:id>',views.homeimage,name='homeimage'),
    path('loginimage/',views.loginimage,name='loginimage'),
    path('update/<int:id>',views.update,name='update'),
    path('show_users/',views.show_users,name='show_users'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logout/',views.logout,name='logout'),
]