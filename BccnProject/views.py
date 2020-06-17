import hashlib, time
from django.conf import settings
from app01.models import UserAuthToken, Account
from django.http import JsonResponse
from rest_framework.views import APIView


def get_random_str(user):

    ctime = str(time.time())
    md5 = hashlib.md5(bytes(user,encoding="utf-8"))
    md5.update(bytes(ctime,encoding="utf-8"))
    return md5.hexdigest()

def get_hash_password(password):
    md5 = hashlib.md5(bytes(password, encoding="utf-8"))
    # 加盐
    md5.update(bytes(settings.SALT, encoding="utf-8"))
    return md5.hexdigest()


class LoginView(APIView):

    def post(self, request):
        res = {
            "state_code": 1000,
            "msg": None
        }
        try:
            username = request.data.get("user")
            pwd = request.data.get("pwd")
            user = Account.objects.filter(username=username, password=get_hash_password(pwd)).first()
            if user:
                random_str = get_random_str(user.username)
                token = UserAuthToken.objects.update_or_create(user=user, defaults={"token": random_str})
                res['token'] = str(random_str)
                res['user_id'] = user.id
            else:
                res["state_code"] = 1001,
                res["msg"] = "用户名或者密码错误"
        except Exception as e:
            res['state_code'] = 1002
            res['msg'] = str(e)
        return JsonResponse(res,json_dumps_params={"ensure_ascii": False})


class RegisterView(APIView):
    def post(self, request):
        res = {
            "state_code": 1000,
            "msg": None
        }
        try:
            username = request.data.get("user")
            pwd = request.data.get("pwd")
            user = Account.objects.filter(username=username).first()
            if user:
                res['state_code'] = 1001
                res['msg'] = '用户名或者密码错误'
                return JsonResponse(res, json_dumps_params={"ensure_ascii": False})
            else:
                password = get_hash_password(pwd)
                newUser = Account.objects.create(username=username, password=password)
                res['msg'] = "用户创建成功"
        except Exception as e:
            res['state_code'] = 1002
            res['msg'] = str(e)
        return JsonResponse(res, json_dumps_params={"ensure_ascii": False})