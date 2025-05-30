from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductFilterForm

DEFAULT_CATEGORY_ID = 1
def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def contacts(request):
    return render(request, "home/contacts.html")

def products(request):
    form = ProductFilterForm(request.GET or None)

    products = Product.objects.all()
    try:
        default_category: Category = Category.objects.get(id=DEFAULT_CATEGORY_ID)
    except Category.DoesNotExist:
        default_category = None

    # применяем фильтры, если форма валидна
    if form.is_valid():
        brands = form.cleaned_data.get('brand')
        categories = form.cleaned_data.get('category')

        if brands:
            products = products.filter(brand__in=brands)
        if categories:
            category_id = request.GET.get('category')

            if category_id == '1':
                return redirect('/products')
            products = products.filter(category__in=categories)

    context = {
        'default_category': default_category,
        'products': products,
        'form': form,
    }
    return render(request, 'home/products.html', context)


def product_detail(request, brand_slug, product_slug):
    product: Product = get_object_or_404(Product, slug=product_slug, brand__slug=brand_slug)
    return render(request, 'home/a_product.html', {'product': product})
