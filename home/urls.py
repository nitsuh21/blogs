from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogs, name='blogs'),
    path('addblog/', views.addblog, name="addblog"),
    path('editblog/<int:id>/', views.editblog, name="editblog"),
    path('deleteblog/<int:id>',views.deleteblog,name="deleteblog" )
]