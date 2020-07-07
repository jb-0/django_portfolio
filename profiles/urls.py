from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('new-profile/', views.new_profile, name='new-profile')
]
