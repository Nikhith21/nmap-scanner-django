
from django.urls import path

from . import views

# In the urls if the action succeded returns to all automatically
app_name='network_scanner'
urlpatterns = [
    path('network-scanner/', views.ScannerView.as_view(), name='form_scanner_view'),
    path('perform-scan/', views.ScannerView.as_view(), name='post_form_scanner'),
    path('scanner-history/<str:type>', views.ScannerHistoryListView.as_view(), name='scanner_type'),
    path('scanner-history/<int:scanner_history_id>/host', views.HostListView.as_view(), name='host_list'),
    path('scanner-history/<int:scanner_history_id>/host/<int:host_id>/os_match', views.OperativeSystemMatchListView.as_view(), name='os_matches_list'),
    path('scanner-history/<int:scanner_history_id>/host/<int:host_id>/ports', views.PortListView.as_view(), name='host_ports_list'),
]