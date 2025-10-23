from django.urls import path
from . import views

urlpatterns = [
    path('', views.VendorListView.as_view(), name='vendor-list'),
    path('<int:pk>/', views.VendorDetailView.as_view(), name='vendor-detail'),
    path('search/', views.search_vendors, name='search-vendors'),
    path('check-availability/', views.check_availability, name='check-availability'),
    path('book/', views.create_booking, name='create-booking'),
]
