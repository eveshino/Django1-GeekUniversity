from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Product

def index(request):

    products = Product.objects.all()


    # print(dir(request.user))
    # print(f"user: {request.user} ")
    #
    # if str(request.user) == 'AnonymousUser':
    #     teste = 'User not Logged'
    # else:
    #     teste = 'User Logged'

    context = {
        'curso': 'Programacao Web com Django Framework',
        'products': products
        # 'teste': teste
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')

def product(request, id):
    # prod = Product.objects.get(id=id)

    prod = get_object_or_404(Product, id=id)

    context = {
        'product': prod
    }
    # print(f'PK: {id}')
    return render(request, 'product.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)