from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app01 import models

class Auth(BaseAuthentication):
    def authenticate(self, request):
        token = request.data['token']
        TokenObj = models.UserAuthToken.objects.filter(token=token).first()
        if not TokenObj:
            raise AuthenticationFailed({'code': '1004', 'error':'认证失败'})
        return (TokenObj.user.username, TokenObj)