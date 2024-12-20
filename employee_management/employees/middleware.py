from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.COOKIES.get('user_id') and not request.path.startswith('/login'):
            return redirect('/login')
        return self.get_response(request)