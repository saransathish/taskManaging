from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('login/done/<int:id>',views.done,name='done'),
    path('login/createtodo/',views.createtodo,name='createtodo'),
    path('signup/',views.signup,name="signup"),
    path('signup/back/',views.back,name="back"),
    path('signup/signup/',views.createuser,name="createuser"),

]
