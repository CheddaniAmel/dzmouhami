from django.urls import path
from app1 import views

urlpatterns = [
    path('trusted_lawyers/',views.Trusted_lawyers),
    path('highest_rated_avis/', views.get_highest_rated_avis),
    path('profil_avocat_filtered/',views.ProfilAvocatListView.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),
    path('addavis/<int:profilavocat_id>/', views.add_avis_to_profilavocat),
    path('profilavocat/<int:pk>/blogs/', views.ProfilAvocatBlogsView.as_view(), name='profilavocat-blogs'),
    path('profilavocat/<int:pk>/', views.ProfilAvocatDetailView.as_view(), name='profilavocat-detail'),


    
    
    
    

]

