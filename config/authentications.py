from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class TruthMeBroAuthentication(BaseAuthentication):
    def authenticate(self, request):  # request에 쿠키나 헤더가 들어있다.
        username = request.headers.get("Trust-Me")
        print(username)
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed
