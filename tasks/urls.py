from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('login/done/<int:id>',views.done,name='done'),
    path('login/undo/<int:id>',views.undo,name='undo'),
    path('login/logout/',views.logout,name='logout'),
    path('login/createtodo/',views.createtodo,name='createtodo'),
    path('login/past/',views.past,name='past'),
    path('login/past/goback/',views.goback,name='goback'),
    path('login/past/logout/',views.logout,name='logout'),

    path('signup/',views.signup,name="signup"),
    path('signup/back/',views.back,name="back"),
    path('signup/signup/',views.createuser,name="createuser"),
    path('login/past/download/', views.download_file, name='download_file'),

]
