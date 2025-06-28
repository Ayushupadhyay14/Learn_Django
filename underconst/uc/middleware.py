from django.shortcuts import render
# adjust import based on your app structure
from .models import UnderConstruction


class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_staff:
            return self.get_response(request)

        try:
            uc = UnderConstruction.objects.first()
            if uc and uc.is_under_construction:
                context = {
                    "uc_note": uc.uc_note,
                    "uc_duration": uc.uc_duration
                }
                return render(request, 'uc/underc.html', context)
        except:
            pass
        return self.get_response(request)
