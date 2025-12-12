from django.shortcuts import redirect



class DashboardAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Check if the current URl is in the dashboard app
        if request.path.startswith('/home/'):
            if not request.user.is_authenticated:
                return redirect('accounts:login')
            
        return self.get_response(request)