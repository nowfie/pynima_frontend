from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('product_ind/',views.product_ind,name='product_ind'),
    path('blog_ind/',views.blog_ind,name='blog_ind'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('product/',views.product,name='product'),
]
