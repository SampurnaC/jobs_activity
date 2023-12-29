from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from jobs.models import Job


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'home',]
    
    def location(self, item):
        return reverse(item)
