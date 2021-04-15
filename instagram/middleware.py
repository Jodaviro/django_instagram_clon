"""Instagram Middleware"""

class ProfilecompletionMiddleware:
    """Ensure that every registered user has some data added to its profile"""
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code t≠o be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

