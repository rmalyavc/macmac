from django.shortcuts import render_to_response, render, get_object_or_404
from .models import Category, Product, Ad, Brand, SubCat
from cart.forms import CartAddProductForm
from django.http import JsonResponse, HttpResponse
import json
from django.urls import reverse
from cart.cart import Cart


def Index(request):
    index = 'index'
    brands = Brand.objects.all()
    news = Ad.objects.filter(active=True)
    categories = Category.objects.all()
    cart = Cart(request)
    return render(request, 'shop/base.html', {
        'index': index,
        'categories': categories,
        'ads': news,
        'brands': brands,
        'cart': cart,
    })
    
def Brands(request):
    brands = Brand.objects.all()
    return render(request, 'shop/brands.html', {
            'brands': brands
        })
        
def BrandDetail(request, id, slug):
    brand = get_object_or_404(Brand, id=id, slug=slug)
    return render(request, 'shop/brands.html', {
            'brand': brand
        })
        
def Delivery(request):
    return render(request, 'shop/brands.html', {
            'delivery': "delivery"
        })
        
def CategoryList(request):
    categories = Category.objects.all()
    return render(request, 'shop/brands.html', {
        'categories': categories
    })
    
def SubCats(request, category_slug):
    subCats = SubCat.objects.all()
    container = {}
    result = []
    for subCat in subCats:
        if subCat.category.slug == category_slug:
            container = subCat
            result.append(container)
    return render(request, 'shop/brands.html', {
        'subCats': result
    })        
    

# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    originalquery = request.GET.get("q")
    ordering = request.GET.get("sort")
    cat = request.GET.get("cat")
    if cat != None:
        category_slug = cat
    print(category_slug)
    brands = Brand.objects.all()
    categories = Category.objects.all()
    subCats = SubCat.objects.all()
    if ordering == 'cheap':
        products = Product.objects.all().order_by('price')
        goods = Product.objects.all().order_by('price')
    elif ordering == 'expansive':
        products = Product.objects.all().order_by('-price')
        goods = Product.objects.all().order_by('-price')
    else:
        products = Product.objects.all()
        goods = Product.objects.all()
    
    if not originalquery == None:
        query = originalquery.lower()
    else:
        query = originalquery
    
    if not query == None:
        q = []
        q = query.split(' ')
        size = len(q)
        testobject = {}
        result = []
        
        for product in goods:
            if q[0] == product.item_code.lower():
                result.clear()
                result.append(product)
                break
            else:    
                i=0
                for i in range(size+1):
                    if i == size:
                        query = ' '.join(q)
                    else:
                        query = q[i]
                    if query in product.name.lower() or query in product.item_code.lower() or query in product.brand.lower():
                        testobject = product
                        if not testobject in result:
                            result.append(testobject)
                        print(testobject)
        return render(request, 'shop/product/list.html', {
            'category': category,
            'categories': categories,
            'subCats': subCats,
            'products': result,
            'query': query,
            'brands': brands
        })
    else:
        if category_slug:
            if not category_slug == 'all':
                category = get_object_or_404(SubCat, slug=category_slug)
                if ordering == 'cheap':
                    products = products.filter(category=category).order_by('price')
                elif ordering == 'expansive':
                    products = products.filter(category=category).order_by('-price')
                else:
                    products = products.filter(category=category)
                
        return render(request, 'shop/product/list.html', {
            'category': category,
            'categories': categories,
            'subCats': subCats,
            'products': products,
            'brands': brands
        })

def News(request, ad_slug):
    ad = get_object_or_404(Ad, slug=ad_slug)
    return render(request, 'shop/news.html',
                             {'ad': ad})

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})
    # return render(request, 'shop/product/detail.html', {'product': product}) 
    
def Search(request, category_slug=None, id=None, slug=None):
    query = request.GET.get("term").lower()
    print(query)
    products = Product.objects.all()
    found = []
    result = {}
    for product in products:
        if query in product.name.lower() or query in product.item_code.lower() or query in product.brand.lower():
            product_json = {}
            product_json["id"] = product.id
            product_json["name"] = product.name 
            product_json["item_code"] = product.item_code
            product_json["img"] = product.img
            product_json["description"] = product.description
            product_json['label'] = product.item_code + ' ' + product.name
            product_json['value'] = product.item_code + ' ' + product.name
            found.append(product_json)
    result = json.dumps(found)
    print(result)
    return HttpResponse(result, content_type='application/json')

def Register(request):
    return render(request, 'shop/register.html', {
        'page': 'register'
        })
