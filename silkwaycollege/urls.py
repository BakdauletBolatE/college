from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('req/', include('registrationapp.urls'))
]

urlpatterns += i18n_patterns(
    path('', include(('sapp.urls', 'sapp'))),
    path('employees/', include(('employeesapp.urls', 'employeesapp'))),
    path('speciliazation/', include(('specializationapp.urls', 'specapp'))),
    path('news/', include(('newsapp.urls', 'newsapp'))),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
