from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pynima_app/base/home.html')

def about(request):
    return render(request,'pynima_app/base/about.html')

def product_ind(request):
    return render(request,'pynima_app/base/product_ind.html')

def blog_ind(request):
    return render(request,'pynima_app/base/blog_ind.html')

def contact(request):
    return render(request,'pynima_app/base/contact.html')

def blog(request):
    return render(request,'pynima_app/base/blog.html')

def product(request):
    return render(request,'pynima_app/base/product.html')