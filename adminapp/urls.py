from adminapp import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('manageproduct', views.manageproduct, name='manageproduct'),
    path('managecategory', views.managecategory, name='managecategory'),
    # path('accounts/userprofile/', views.userprofile, name='userprofile'),
    path('customers', views.customers, name='customers'),
    path('editcategory/<int:pk>', views.editcategory, name='editcategory'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
