# middleware.py
from django.utils import timezone
from django.contrib import auth
from django.conf import settings

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Check if the user's last activity is greater than the allowed session timeout
            last_activity = request.session.get('last_activity')
            if last_activity and (timezone.now() - last_activity).seconds > settings.AUTO_LOGOUT_DELAY:
                auth.logout(request)
                del request.session['last_activity']

        return response