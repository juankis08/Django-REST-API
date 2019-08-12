
from django.conf.urls import url
from .views import UserRudView, UserAPIView

urlpatterns = [
   url(r'^$', UserAPIView.as_view(), name='user-create'),
   url(r'^(?P<pk>\d+)/$', UserRudView.as_view(), name='user-rud'),
   #url(r'^user/$', UserList.as_view(), name='user-list')
]
