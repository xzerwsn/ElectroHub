from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import ShopUserCreationForm, ShopUserLoginForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    # Фильтрация по категории
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Фильтрация по цене
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    # Пагинация
    paginator = Paginator(products, 9)  # 9 товаров на страницу (3x3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'shopapp/product/list.html', {
        'category': category,
        'categories': categories,
        'page_obj': page_obj,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shopapp/product/detail.html', {'product': product})

def index(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:home')
    else:
        form = ShopUserCreationForm()
    return render(request, 'shopapp/auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:home')
    else:
        form = ShopUserLoginForm()
    return render(request, 'shopapp/auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('shop:home')