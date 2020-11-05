from django.conf.urls import url
from todos.views import TodoRetrieveView
urlpatterns = [
    url('todo/all', TodoRetrieveView.as_view())
]