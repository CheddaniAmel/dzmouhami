from django.urls import path
from app1 import views

urlpatterns = [
    path('trusted_lawyers/',views.Trusted_lawyers),
    path('profil_avocat_filtered/',views.ProfilAvocatListView.as_view()),
    path('signup/', views.signup),
    path('login/', views.user_login),
    path('logout/', views.user_logout),

]

