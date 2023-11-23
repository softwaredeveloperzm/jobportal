# jobportal/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from apps.core.views import frontpage, signup, signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signin/', views.LoginView.as_view(template_name='core/signin.html'), name='signin'),
  
]
