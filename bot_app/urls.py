from django.conf.urls import include
from django.conf.urls import url

from bot_app.views import Dashboard


urlpatterns = [

	url(r'$', Dashboard.as_view(), name="dashboard" ),
]
