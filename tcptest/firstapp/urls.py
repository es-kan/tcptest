from django.conf.urls import url

from views import IndexView

urlpatterns = [
    url(r'^index/', IndexView.as_view())
]
