
from django.urls import path, re_path
from .views import IndexView, AboutView, RecruitingView, ContactView, QuoteoView,  ServiceView, ServiceDetail, ClientListHTMXView, PortfolioView
from django.urls import path

app_name = 'core'


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('services', ServiceView.as_view(), name='services'),
    path('service_detail/<slug:slug>/', ServiceDetail.as_view(), name='service_detail'),
    path('clients', ClientListHTMXView.as_view(), name='clients'),
    path('about', AboutView.as_view(), name='about'),
    path('hiring', RecruitingView.as_view(), name='hiring'),
    path('contact', ContactView.as_view(), name='contact'),
    path('quote', QuoteoView.as_view(), name='quote'),
    # path('<str:language>/contact/', views.contact, name='contact'),
    # path('<str:language>/about/', views.about, name='about'),
    # path('<str:language>/hiring/', views.hiring, name='hiring'),
    # path('<str:language>/services/', views.services, name='services'),
    # path('<str:language>/index/', views.index, name='index'),
    # path('switch_language/', views.switch_language, name='switch_language'),
]
