from django.urls import path

from . import views

urlpatterns=[
    # path('', views.home, name='home'),
    path('', views.save_embed, name='save_embed'),
    # path('github/client/', views.github_client, name='github_client'),
    # path('oxford/', views.oxford, name='oxford'),
]