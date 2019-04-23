import re
from django import forms
from .models import User

from django.core.exceptions import ValidationError


class RegisterForms(forms.ModelForm):
    username = forms.CharField(min_length=5, required=True, max_length=20,
                               label='帐 号 ：',
                               widget=forms.TextInput(attrs={
                                   'placeholder': '请输入不少于6为的账号'
                               })
                               )
    email = forms.EmailField(required=True,
                             label='邮 箱 ：',
                             widget=forms.EmailInput(attrs={
                                 'placeholder': '请输入邮箱'
                             }),
                             error_messages={
                                 'required': '必填项',
                             })
    password = forms.CharField(min_length=5, required=True, max_length=20,
                               label='密 码 ：',
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': '6-20位非中文字符'
                               }))
    re_password = forms.CharField(min_length=5, required=True, max_length=20,
                                  label='确定密码：',
                                  widget=forms.PasswordInput(attrs={
                                      'placeholder': '6-20位非中文字符'
                                  }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if re.match('^[0-9]', password):
            raise ValidationError('请勿以数字开头')
        return password

    def clean(self):
        password = self.cleaned_data.get('password', '')
        password2 = self.cleaned_data.get('re_password', '')
        if password != password2:
            raise ValidationError('密码不一致')
        return self.cleaned_data
