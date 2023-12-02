# signals.py
from django.core.signals import request_started
from django.dispatch import receiver
from django.utils import timezone

@receiver(request_started)
def set_last_activity(sender, **kwargs):
    request = kwargs.get('request')
    if request and request.user.is_authenticated:
        request.session['last_activity'] = timezone.now()