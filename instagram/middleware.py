"""Instagram Middleware"""
#Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileUpdateMiddleware:
    """Ensure that every registered user has some data added to its profile"""
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code t≠o be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_anonymous and not request.user.is_superuser:
            profile = request.user.profile

            if not profile.picture and not  profile.biography :
                if request.path not in [reverse('users:update_profile'), reverse('users:logout'), reverse('test')]\
                        and not request.path.startswith('/admin/'):

                    return redirect('users:update_profile')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response



