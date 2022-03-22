from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns=[
   path('',views.timeline,name='timeline'),
   path('accounts/profile/',views.profile,name='profile'),
   path('accounts/login',views.login),
   path('signup/',views.signup,name='signup'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)