from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name="home"),
    path('cause/<slug>', views.single, name="causes-single"),
    path('all-causes/', views.all_causes, name="causes-list"),
    path('about-us', views.about, name="about"),
    path('contact-us', views.contact, name="contact"),
    path('search', views.search, name="search"),
    path('events', views.events, name="events"),
    path('donation', views.donation, name="donation"),
    path('initiate-payment/<slug>', views.initiate_payment, name='initiate_payment'),
    path('verify-payment/<str:ref>/', views.verify_payment, name='verify_payment'),
    path('event-details/<slug>', views.event, name="event"),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)