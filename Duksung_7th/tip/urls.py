from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('post/',views.post,name='post'),
    path('detail/',views.detail,name='detail'),
    path('post_list/',views.post_list,name='post_list'),
    path('<int:tip_id>/',views.detail,name='detail'),
    path('<int:pk>/edit/',views.edit, name='edit'),
    path('int:pk>/delete/',views.delete,name='delete'),
    path('deleteall/',views.deleteall,name='deleteall'),
    path('download/<int:pk>',views.download,name='download'),
    #path('post_list/',views.post_list,name='post_list'),
    #path('show/',views.show,name='show'),
    path('login/login/',views.LoginView,name="login"),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)