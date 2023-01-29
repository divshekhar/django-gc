from django.http import JsonResponse
from django.views import View


class GoogleCalendarInitView(View):
    def get(self, request, *args, **kwargs):
        data = {'message': 'Google Calendar initialized!'}
        return JsonResponse(data)


class GoogleCalendarRedirectView(View):
    def get(self, request, *args, **kwargs):
        data = {'message': 'Google Calendar Redirect!'}
        return JsonResponse(data)
