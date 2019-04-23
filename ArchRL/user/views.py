from django.views.generic.base import View
# 返回方法
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

from .models import User
from .forms import RegisterForms
from ArchRL.settings import SECRET_KEY
from celery_tasks import tasks

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired

# from django.views.generic import CreateView
# class Test(CreateView):
#     success_url = '/'
#     template_name = 'register.html'
#     form_class = RegisterForms
#     model = User
#
#     def form_valid(self, form):
#         self.object = form.save()
#         return super(Test, self).form_valid(form)

class Register(View):
    def get(self, request):
        re_forms = RegisterForms()
        return render(request, 'register.html', {
            're_forms': re_forms,
        })

    def post(self, request):
        re_forms = RegisterForms(request.POST)
        if re_forms.is_valid():
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            re_password = request.POST.get('re_password', '')
            if not password == re_password:
                return JsonResponse({'msg': '密码不一致'})
            user = User.objects.filter(username=username)
            if user:
                return JsonResponse({'msg': '账号已存在'})

            user = User.objects.create_user(username, email, password)
            user.is_active = 0
            user.save()
            serializer = Serializer(SECRET_KEY, 60 * 60)
            info = {'confirm': user.id}
            token = serializer.dumps(info)
            token = token.decode()
            tasks.send_register_active_email.delay(email, username, token)
            return render(request, 'register.html', {
                're_forms': re_forms,
            })
        else:
            all_error = re_forms.errors.get('__all__')
            return render(request, 'register.html', {
                're_forms': re_forms,
                'all_error': all_error,
            })



class ActiveView(View):

    def get(self, request, token):
        serializer = Serializer(SECRET_KEY, 60 * 60)
        try:
            user_id = serializer.loads(token)['confirm']
            user = User.objects.get(id=user_id)
        except SignatureExpired:
            return HttpResponse('激活连接已过期')
        except User.DoesNotExist:
            return HttpResponse('账户异常，无法激活')
        user.is_active = 1
        user.save()
        return redirect('http://47.94.144.96:8080')