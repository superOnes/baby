from functools import wraps
from datetime import datetime

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect

from .models import User


RETURN_JSON = 1
RETURN_PAGE = 2


def admin_required(func):
    @wraps(func)
    def return_wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            if request.user.is_admin:
                if request.user.expire_date is None \
                   or request.user.expire_date > datetime.now():
                    return func(request, *args, **kwargs)
            logout(request)
        return redirect('/acc/login/?next=%s' % request.get_full_path())
    return return_wrapper


def customer_login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        userid = request.GET.get('userid', request.POST.get('userid'))
        if not userid:
            return JsonResponse({'response_state': 401, 'msg': '用户没有登录！'})
        if not User.objects.filter(username=userid):
            return JsonResponse({'response_state': 401, 'msg': '用户没有登录！'})
        return func(request, *args, **kwargs)
    return wrapper


# def customer_login_time(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         userid = request.GET.get('userid', request.POST.get('userid'))
#         user = User.get(userid)
#         now = datetime.now()
#         if now <= user.customer.event.event_end:
#             if now <= user.customer.event.event_start:
#                 return JsonResponse({'response_state': 403, 'msg': '活动尚未开始'})
#             else:
#                 return func(request, *args, **kwargs)
#         else:
#             return JsonResponse({'response_state': 403, 'msg': '活动已经结束'})
#     return wrapper
#
#
# def login_time(func):
#     @wraps(func)
#     def wrapper(request, *args, **kwargs):
#         mobile = request.POST.get('tel')
#         identication = request.POST.get('personId')
#         try:
#             customer = Customer.objects.get(
#                 mobile=mobile, identication=identication)
#             now = datetime.now()
#         except BaseException:
#             return JsonResponse({'response_state': 400, 'msg': '认筹名单中没有此用户'})
#         else:
#             if now <= customer.event.event_end:
#                 return func(request, *args, **kwargs)
#             else:
#                 return JsonResponse({'response_state': 403, 'msg': '活动已经结束'})
#     return wrapper
