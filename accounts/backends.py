from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        
        if email is None or password is None:
            return None
        
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        
        if not user.check_password(password):
            return None
        
        if not self.user_can_authenticate(user):
            return None
        
        return user