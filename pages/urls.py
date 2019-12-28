from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index),
    path('resume/', views.resume),
    path('services/', views.services),
    path('portfolio/', views.portfolio),
    path('blog/', views.blog_list),
    path('blog/<int:pk>/', views.blog_list_n),
    path('blog/<slug:slug>/', views.blog_view),
    path('contact/', views.contact),
]