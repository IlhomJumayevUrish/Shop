from django.contrib import admin
from django.urls import path,include
from myshop import views
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/',include('rosetta.urls')),
    path('',include('myshop.urls',namespace='myshop'))
)
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
