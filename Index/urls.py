from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path("" , views.IndexView.as_view() , name = "index"),
    path("about_us" , views.About_Us , name = "about_us"),
    path("Contact-Us" , views.FormsView.as_view() , name ="Contact-Us"),
    path("product" , views.ProducdtView.as_view() , name ="product"),
    path("<int:pk>" , views.DetailProductView.as_view() , name="Detail")
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)