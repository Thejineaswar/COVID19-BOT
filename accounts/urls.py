from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/hospital',views.Hospitalsignup,name='hsignup'),
    path('signup/testing',views.Testingsignup,name='tsignup'),
    path('update/hospital',views.Hospitalupdate,name='hupdate'),
    path('update/testing',views.Testingupdate,name='tupdate'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
