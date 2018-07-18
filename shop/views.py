from django.shortcuts import render_to_response, render, get_object_or_404
from .models import Category, Product, Ad, Brand, SubCat, Filt, Color, Memory, Unit, Ram, Proc, Diagonal, Material, Display
from cart.forms import CartAddProductForm
from django.http import JsonResponse, HttpResponse
import json
from django.urls import reverse
from cart.cart import Cart
from django.core import serializers

def get_goods(cats):
    products = Product.objects.all()
    goods = []
    for product in products:
        if product.category in cats:
            goods.append(product)
    return goods

def get_filt_vals(filt, products):
    cont = []
    if filt.name == 'color':
        for product in products:
            if not product.color in cont:
                cont.append(product.color)
    elif filt.name == 'diagonal':
        for product in products:
            if not product.diagonal in cont:
                cont.append(product.diagonal)
    elif filt.name == 'memory':
        for product in products:
            if not product.memory in cont:
                cont.append(product.memory)
    elif filt.name == 'ram':
        for product in products:
            if not product.ram in cont:
                cont.append(product.ram)
    elif filt.name == 'material':
        for product in products:
            if not product.material in cont:
                cont.append(product.material)
    elif filt.name == 'processor':
        for product in products:
            if not product.proc in cont:
                cont.append(product.proc)
    elif filt.name == 'display':
        for product in products:
            if not product.display in cont:
                cont.append(product.display)
    return cont

def get_refs(goods, refs):
    for product in goods:
        for category in product.refer_to.all():
            if not category in refs:
                refs.append(category)
    return refs

def ajax_goods(filts):
    goods = Product.objects.all()
    for key in filts:
        print("key = ", key, filts[key])
        if key == 'category_slug':
            goods = goods.filter(category__category__slug = filts[key])
        elif key == 'color':
            goods = goods.filter(color__name__in = filts[key])
        elif key == 'diagonal':
            goods = goods.filter(diagonal__name__in = filts[key])
        elif key == 'memory':
            goods = goods.filter(memory__name__in = filts[key])
        elif key == 'ram':
            goods = goods.filter(ram__name__in = filts[key])
        elif key == 'proc':
            goods = goods.filter(proc__name__in = filts[key])
        elif key == 'material':
            goods = goods.filter(material__name__in = filts[key])
        elif key == 'refer_to':
            goods = goods.filter(refer_to__in = SubCat.objects.all().filter(name__in = filts[key]))
        elif key == 'subcat':
            goods = goods.filter(category__name__in = filts[key])
    goods = goods[filts['from']:9]
    return (goods)


def FiltedGoods(request, category_slug=None):
    data = json.loads(request.body.decode('utf-8'))
    goods = ajax_goods(data)
    cont = ''
    i = 0
    for item in goods:
        item.url = reverse('shop:ProductDetail', args=[item.id, item.slug])
        if not item.name == None:
            print(item.name)
    data = serializers.serialize("json", goods)
    return HttpResponse(data)

def FakeList(request, category_slug=None):
    # ordering = request.GET.get("sort");
    if category_slug == None or category_slug == 'all':
        categories = Category.objects.all().order_by('id')
        goods = Product.objects.all()
        return render(request, 'shop/product/fakelist.html', {
            'categories': categories,
            'goods': goods,
        })
    else:
        cont = {}
        refs = []
        categories = []
        cat = Category.objects.get(slug = category_slug)
        cats = SubCat.objects.all().filter(category = cat)
        goods = get_goods(cats)
        filts = Filt.objects.filter(cats=cat).order_by('id')
        for filt in filts:
            cont[filt.name] = get_filt_vals(filt, goods)
        if category_slug == 'accessories':
            refs = get_refs(goods, refs)
        for product in goods:
            if not product.category in categories:
                categories.append(product.category)
        return render(request, 'shop/product/fakelist.html', {
            'goods': goods,
            'category': cat,
            'categories': categories,
            'filts': filts,
            'vals': cont,
            'refs': refs,
        })

def Index(request):
    index = 'index'
    brands = Brand.objects.all()
    news = Ad.objects.filter(active=True)
    categories = Category.objects.all()
    cart = Cart(request)
    products = Product.objects.all()
    cat_object = Category.objects.get(name='Mac')
    filts = Filt.objects.filter(cats=cat_object).order_by('id')
    colors = Color.objects.all().order_by('id')
    mems = Memory.objects.all().order_by('id')
    rams = Ram.objects.all().order_by('id')
    proces = Proc.objects.all().order_by('id')
    diagonals = Diagonal.objects.all().order_by('id')
    goods = Product.objects.all().filter(discount=True)[:4]
    cols = []
    for col in colors:
        for prod in products:
            if prod.color == col and col not in cols:
                cols.append(col)
    return render(request, 'shop/index.html', {
        'index': index,
        'categories': categories,
        'ads': news,
        'brands': brands,
        'cart': cart,
        'filts': filts,
        'cols': cols,
        'mems': mems,
        'rams': rams,
        'proces': proces,
        'diags': diagonals,
        'goods': goods,
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
    print(category_slug)
    if cat != None:
        category_slug = cat
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
