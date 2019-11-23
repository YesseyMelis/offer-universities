from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


patterns = [
    path("", include("universities.urls", namespace="universities")),
]

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path("admin/", admin.site.urls),
    path("api/", include(patterns)),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
