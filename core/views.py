from django.shortcuts import render
from core.models import Category

# Create your views here.

def home_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'core/home.html', context)


def category_page(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'category': category,
    }
    return render(request, 'core/category-page.html', context)
