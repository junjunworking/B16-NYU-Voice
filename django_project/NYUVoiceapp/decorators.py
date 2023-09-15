from functools import wraps
from django.http import HttpResponseForbidden

def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('You must be a staff member to access this page.')
    return _wrapped_view
