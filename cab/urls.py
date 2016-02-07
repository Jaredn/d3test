from cab import views
from django.conf.urls import url

urlpatterns = [
    url(r'^cabtest', views.cabtest, name='cabtest'),
]
