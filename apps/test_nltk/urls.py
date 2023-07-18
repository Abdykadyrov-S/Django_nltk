from django.urls import path
from .views import SynonymView, AntonymView

urlpatterns = [
    path('synonyms/', SynonymView.as_view(), name='synonyms'),
    path('antonyms/', AntonymView.as_view(), name='antonyms'),
]
