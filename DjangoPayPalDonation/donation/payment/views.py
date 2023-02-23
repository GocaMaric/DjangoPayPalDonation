from django.shortcuts import render

# Create your views here.

from .models import Donation


def donation_page(request):
    donation = Donation.objects.all()

    return render(request, 'payment/donation-page.html', {'my_donation': donation})


def payment_completed(request):
    return render(request, 'payment/payment-completed.html')


def payment_failed(request):
    return render(request, 'payment/payment-failed.html')
