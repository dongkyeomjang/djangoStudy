from django.contrib import admin
from django.urls import path, include #include 추가
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='root.html'), name='root'),
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')), #blog1/urls.py를 include
    path('instagram/', include('instagram.urls')), #instagram/urls.py를 include
]

#DEBUG는 개발모드일 때만 True이며, 실제 서비스 시에는 False로 설정함.
if settings.DEBUG: # 장고는 서비스 시에 media나 static file을 실제 프로덕션에서 제공하는 것을 권장하지 않음. 따라서 개발모드일 때만 제공하도록 설정함
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)