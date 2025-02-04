from travels.models import IPAddress
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


class IPTrackingMiddleware:
    ATTEMPT_LIMIT = 1

    def __init__(self, get_response):
        self.get_response = get_response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    def __call__(self, request):
        if request.path.startswith('/destinations/') and not request.user.is_authenticated:
            ip_address = self.get_client_ip(request)
            if ip_address:
                ip_record, created = IPAddress.objects.get_or_create(ip_address=ip_address)
                if not created:
                    ip_record.increment_attempt()
                    print(f"IP: {ip_address}, Attempts: {ip_record.get_attempt_count()}")
                else:
                    print(f"New IP added: {ip_address}")
                
                if ip_record.get_attempt_count() > self.ATTEMPT_LIMIT:
                    print(f"Access Restricted for IP: {ip_address}, Attempts: {ip_record.get_attempt_count()}")
                    messages.error(request, 'You need to login to view more')
                    return redirect('login')
                
                

        response = self.get_response(request)
        print(f"Response sent for: {request.path}")
        return response
