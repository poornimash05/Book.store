from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse  # 👈 import for root view
from base.views.user_views import save_fcm_token

# 👇 root path view
def root_view(request):
    return JsonResponse({'message': 'Welcome to the Book Store API 🎉'})

urlpatterns = [
    path('', root_view),  # 👈 handles "/"
    path('admin/', admin.site.urls),
    path('api/coupons/', include('base.urls.coupon_urls')),
    path('api/products/', include('base.urls.product_urls')),
    path('api/users/', include('base.urls.user_urls')),
    path('api/orders/', include('base.urls.order_urls')),
    path('api/save-token/', save_fcm_token, name='save-fcm-token'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
