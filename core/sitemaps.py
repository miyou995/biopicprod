from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['core:index', 'core:portfolio','core:services','core:about','core:contact' ]
    def location(self, item):
        return reverse(item)
    
    
class ServiceSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
    
    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.updated