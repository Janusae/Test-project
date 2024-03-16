from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(label="نام کاربری" , widget=forms.TextInput(attrs={"placeholder":"Enter your username"}))
    email = forms.EmailField(label="ایمیل" , widget=forms.EmailInput(attrs={"placeholder":"Enter your email"}))
    password = forms.CharField(label="گذرواژه" , widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"}))
    confirm_password = forms.CharField(label="تکرار گذرواژه" , widget=forms.PasswordInput(attrs={"placeholder":"Enter your confirm password"}))
    def clean_confirm_password(self):
        passwd = self.cleaned_data.get("password")
        confirm_pass = self.cleaned_data.get("confirm_password")
        if passwd == confirm_pass:
            return confirm_pass
        else:
            raise ValidationError(confirm_pass , "Your password and confirm password do not match")
class LoginForm(forms.Form):
    email = forms.EmailField(label="ایمیل" , widget=forms.EmailInput(attrs={"placeholder":"Enter your email"}))
    password = forms.CharField(label="گذرواژه" , widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"}))

class  Forget_form(forms.Form):
    email = forms.EmailField(label="ایمیل" , widget=forms.EmailInput())

class  Reseat_pass(forms.Form):
    password = forms.CharField(label="گذرواژه" , widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"}))
    confirm_password = forms.CharField(label="تکرار گذرواژه" , widget=forms.PasswordInput(attrs={"placeholder":"Enter your confirm password"}))
    def clean_confirm_password(self):
        passwd = self.cleaned_data.get("password")
        confirm_pass = self.cleaned_data.get("confirm_password")
        if passwd == confirm_pass:
            return confirm_pass
        else:
            raise ValidationError(confirm_pass , "Your password and confirm password do not match")