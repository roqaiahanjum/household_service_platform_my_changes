from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('checkout/<int:booking_id>/', views.checkout_view, name='checkout'),
    path('init/<int:booking_id>/', views.init_payment, name='init_payment'),
    path('verify/', views.verify_payment, name='verify_payment'),
    path('success/', views.payment_success, name='payment_success'),
    path('failed/', views.payment_failed, name='payment_failed'),
]
