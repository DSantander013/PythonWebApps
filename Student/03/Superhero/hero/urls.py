from django.urls import path
from .views import HulkView, IndexView, IronManView, CaptainAmerica, TheFlash, SpiderMan

urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('spiderman', SpiderMan.as_view()),
    path('captainamerica', CaptainAmerica.as_view()),
    path('theflash', TheFlash.as_view()),
]
