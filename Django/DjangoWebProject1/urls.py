"""
Definition of urls for DjangoWebProject1.
"""

from django.conf.urls import include,url
import SalesTaxCPS.scripts.dataVisualization

# Django processes URL patterns in the order they appear in the array.
urlpatterns = [
    url(r'^$', SalesTaxCPS.scripts.dataVisualization.showData, name='dataVisualization'),
]