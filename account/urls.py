from django.conf.urls import url
from account.views import CurrentUserView
urlpatterns = [
    url(r'^user/$', CurrentUserView.as_view())
]