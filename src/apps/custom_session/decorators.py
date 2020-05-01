
from django.http import Http404


def role_required(rol):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            print(rol)
            user = request.user
            if user.is_authenticated and user.user_type == rol:
                return func(request, *args, **kwargs)
            else:
                raise Http404
        return wrap
    return decorator
