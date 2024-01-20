from django.urls import path
from . import views

urlpatterns = [
    path('/',views.blogs, name='blogs'),
    path('addblog/', views.addblogs, name="addblogs")
]