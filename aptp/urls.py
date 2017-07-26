from django.conf.urls import url
from .views import (
    ProView,
    AppEventDetailView,
    AppEventDetailListView,
    AppEventDetailHouseInfoView,
    AddFollow,
    AppHouseChoiceConfirmView,
    AppOrderListView,
    AppOrderInfoView,
    FollowView,
    AppEventDetailUnitListView,
    AppEventDetailHouseListView)

urlpatterns = [
    url(r'^(?P<pk>\d+)/detail/', AppEventDetailView.as_view(), name='app_eventdetail'),
    url(r'^(?P<pk>\d+)/houses/', AppEventDetailListView.as_view(), name='app_building_list'),
    url(r'^prodel/', ProView.as_view(), name='app_protocol_detail'),
    url(r'^unit/', AppEventDetailUnitListView.as_view(), name='app_unit_list'),
    url(r'^houselist/$', AppEventDetailHouseListView.as_view(), name='app_house_list'),
    url(r'^houseinfo/', AppEventDetailHouseInfoView.as_view(), name='app_house_info'),
    url(r'^addfollow/', AddFollow.as_view(), name='app_house_follow'),
    url(r'^followlist/', FollowView.as_view(), name='app_follow_view'),
    url(r'^orderconfirm/', AppHouseChoiceConfirmView.as_view(), name='app_follow_view'),
    url(r'^orderinfo/', AppOrderInfoView.as_view(), name='app_order_info'),
    url(r'^orderslist', AppOrderListView.as_view(), name='app_order_list'),
]
