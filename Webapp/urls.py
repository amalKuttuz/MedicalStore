from Webapp import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='home'),
    # path('/ProductCategory/<str:pk>', views.ProductCategory.as_view, name='ProductCategory'),
    path('Productdetails/<int:pk>', views.ProductPage, name='Productdetails'),
    path('accounts/userprofile/', views.Profile, name='profile'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
