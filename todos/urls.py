from django.conf.urls import url
from todos.views import TodoRetrieveView, CreateTodoView, TodosRetrieveView, CompleteTodoView, AddTodoImageView, TodoTitleRetrieveView
urlpatterns = [
    url(r'^todo/all/$', TodosRetrieveView.as_view()),
    url(r'^todo/create/$', CreateTodoView.as_view()),
    url(r'^todo/(?P<id>[0-9]+)/$', TodoRetrieveView.as_view()),
    url(r'^todo/completed/$', CompleteTodoView.as_view()),
    url(r'^todo/image/add/$', AddTodoImageView.as_view()),
    url(r'^todo/search/(?P<title>[0-9,A-Z,a-z]+)/$', TodoTitleRetrieveView.as_view())
]