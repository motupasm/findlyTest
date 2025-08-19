from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("returnitem/", views.returnItemviews, name="returnitem"),
    path("founditem/", views.foundItemviews, name="founditems"),
    path("signin/", views.singinItemviews, name="signin"),
    path("signup/", views.singupItemviews, name="signup"),
    path("search/", views.search, name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
