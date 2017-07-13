from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add-todo$', views.add_todo),
    url(r'^edit-todo$', views.edit_todo),
    url(r'^edit-todo/(?P<todo_id>\d+)$', views.edit_todo),
    url(r'^delete-todo/(?P<todo_id>\d+)$', views.delete_todo),

]
