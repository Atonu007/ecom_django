# core/middleware.py

from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class DisableLoginRedirectForSwaggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path is for Swagger or Redoc
        if request.path in [reverse('schema-swagger-ui'), reverse('schema-redoc')]:
            request.user.is_authenticated = True  # Mock authenticated user

        response = self.get_response(request)
        return response
