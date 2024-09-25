from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si el usuario no está autenticado y no está en una página de login o logout
        if not request.user.is_authenticated and not request.path.startswith(reverse('login')):
            return redirect('login')  # Redirige a la página de login

        return self.get_response(request)
