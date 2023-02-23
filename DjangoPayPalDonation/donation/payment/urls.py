from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation_page, name='donation-page'),

    path('payment-completed', views.payment_completed, name='payment-completed'),

    path('payment-failed', views.payment_failed, name='payment-failed'),
]
