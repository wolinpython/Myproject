from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^list$', views.blog_list, name='blog_list'),
    url(r'^detail/(\d+)/$', views.get_detail, name='blog_get_detail'),
]
