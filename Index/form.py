from django import forms
from .models import Contact_Us_db, NewsUser


class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact_Us_db
        fields = '__all__'
        exclude = ["date" ,"readed_by_admin"]
        widgets = {
            "name" : forms.TextInput(attrs={"placeholder": "Enter your name"}),
            "email" : forms.EmailInput(attrs={"placeholder": "Enter your email"}),
            "phone" : forms.TextInput(attrs={"placeholder" : "Enter your phone number"}),
            "message" : forms.TextInput(attrs={"placeholder": "Enter your message"}),
        }

class New_User_Form(forms.ModelForm):
    class Meta:
        model = NewsUser
        fields = '__all__'
        # widgets = {
        #     "Email" : forms.EmailInput()
        # }
        # labels = {
        #     "Email" : "ایمیل"
        # }