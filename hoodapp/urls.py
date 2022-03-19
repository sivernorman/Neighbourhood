from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns=[
   # path('accounts/profile/',views.profile,name = 'profile'),
   path('',views.timeline,name = 'timeline'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)