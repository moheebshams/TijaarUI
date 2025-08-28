from django.shortcuts import render



def home(request): return render(request, 'index.html')
def header(request): return render(request, 'header.html')
def hero(request): return render(request, 'hero.html')
def category(request): return render(request, 'category.html')
def featured(request): return render(request, 'featured.html')
def electronics(request): return render(request, 'electronics.html')
def decor(request): return render(request, 'decor.html')
def customer(request): return render(request, 'customer.html')
def why(request): return render(request, 'why.html')
def offer(request): return render(request, 'offer.html')
def footer(request): return render(request, 'footer.html')

def addToCart(request): return render(request, 'addToCart.html')
def form(request): return render(request, 'form.html')
def trackYourOrder(request): return render(request, 'trackYourOrder.html')

