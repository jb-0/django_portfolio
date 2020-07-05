from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', views.ProfileListView.as_view(), name='profiles'),
    path('profiles/<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),
]
