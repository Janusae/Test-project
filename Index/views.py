from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, CreateView, ListView, DetailView

from .models import Contact_Us_db, Producdt, Tag, NewsUser
from django.views import View
from .form import Contact_Form, New_User_Form


# Create your views here.
class IndexView(CreateView):
    template_name = "Index/Index.html"
    model = NewsUser
    form_class = New_User_Form
    context_object_name = "form"
    success_url = "product"



def About_Us(request):
    return render(request , "Index/about_us.html")
def django_render_header(request):
    return render(request , "header.html")
def django_render_footer(request):
    return render(request , "footer.html")


# class ContactUsView(View):
#     def get(self , request):
#         form = Contact_Form()
#         return render(request , "Index/contect_us.html",{"form":form})
#     def post(self , request):
#         form = Contact_Form(request.POST)
#         if form.is_valid():
#             name =
class FormsView(CreateView):
    template_name = "Index/contect_us.html"
    model = Contact_Us_db
    form_class = Contact_Form
    success_url = "Index"
    context_object_name = "form"
class ProducdtView(ListView):
    template_name = "Index/product.html"
    model = Producdt
    context_object_name = "data"
class DetailProductView(DetailView):
    template_name = "Index/detail.html"
    model = Producdt
    context_object_name = "data"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = Tag.objects.filter(product=self.object)
        return context