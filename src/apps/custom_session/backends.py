from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class AuthEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwars):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

        return None