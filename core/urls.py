from django.urls import path
from .views import category_page

app_name = 'core'

urlpatterns = [
    path('<slug:category_slug>/', category_page, name='category-page'),
]
