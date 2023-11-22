"""NotesManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from NotesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='lnd'),
    path('login/',views.login,name='lgn'),
    path('register/',views.register,name='rgr'),
    path('home/<int:n_id>/',views.home,name='hm'),
    path('mainpage/<int:id>/',views.mainpage,name='mpg'),
    path('create/<int:id>/',views.createnote,name='crt'),
    path('display/<int:id>/',views.displaynote,name='dsp'),
    path('view/<int:id>/<int:nid>/',views.viewnote,name='view'),
    path('update/<int:id>/<int:nid>/',views.updatenote,name='upd'),
    path('delete/<int:id>/<int:nid>/',views.deletenote,name='dlt'),
    path('othernote/<int:id>/',views.othernote,name='oth'),
    path('request/<int:id>/<int:sid>/<int:nid>/<str:s_sub>/<str:s_note>/',views.requestnote,name="req"),
    path('reqpage/<int:id>/',views.reqpage,name='rpg'),
    path('accepted/<int:id>/<int:rid>/<int:atid>/<int:nid>/',views.accepted,name='accp'),
    path('declined/<int:id>/<int:rid>/<int:atid>/<int:nid>/',views.declined,name='dcn'),
    path('acceptednotes/<int:id>',views.acceptednotes,name='acn'),
    path('viewreq/<int:id>/<int:nid>/',views.viewreqnote,name='viewreq'),
    path('likebut/<int:id>/<int:nid>/',views.likebutton,name='like'),
    path('dislikebut/<int:id>/<int:nid>/',views.dislikebutton,name='dislike'),
]
