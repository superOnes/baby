from django.conf.urls import url
from .views import (AppLoginView, AppEventDetailView, AppEventDetailListView,
                    AppEventDetailDetailView,
                    HomePageView, HouseDetailView)

urlpatterns = [
    url(r'^login/', AppLoginView.as_view(), name='app_login'),
    url(r'^(?P<pk>\d+)/detail/', AppEventDetailView.as_view(),
        name='app_eventdetail'),
    url(r'^(?P<pk>\d+)/houses/', AppEventDetailListView.as_view(),
        name='app_house_list'),
    url(r'^house/(?P<pk>\d+)/', AppEventDetailDetailView.as_view(),
        name='app_house_info'),
    url(r'^homepage/', HomePageView.as_view(), name='home_page_view'),
    url(r'^housedel/', HouseDetailView.as_view(), name='aptp_eventdel'),
]
