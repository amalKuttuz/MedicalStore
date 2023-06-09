from Webapp import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about', views.aboutpage, name='about'),
    path('contact', views.contactpage, name='contact'),
    # path('/ProductCategory/<str:pk>', views.ProductCategory.as_view, name='ProductCategory'),
    path('Productdetails/<int:pk>', views.productpage, name='Productdetails'),
    path('accounts/userprofile/', views.userprofile, name='userprofile'),
    path('addtocart/<int:pk>', views.addtocart, name='addtocart'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
