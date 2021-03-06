from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, get_user_model, logout

from products.models import Product, CarouselImageHome
from .forms import ContactForm, LoginForm, RegisterForm


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }

    print('user logged in')
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("Login valido")
            return redirect('/')
    else:
        print('Login invalido!')
        return render(request, 'auth/login.html', context)


def logout_page(request):
    context = {
        'content': 'Você efetuou o logout com sucesso!'
    }
    logout(request)
    return render(request, 'auth/logout.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'auth/register.html', context)


def home_page(request):
    allProducts = Product.objects.all()
    featured = CarouselImageHome.objects.all()
    imageProducts = featured.filter(use=True)
    context = {
        'allProducts': allProducts,
        'imageProducts': imageProducts,
    }

    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        'title': 'pagina sobre',
        'content': 'Bem-vindo a pagina sobre'
    }
    return render(request, 'about/view.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'pagina de contato',
        'content': 'Bem-vindo a pagina de contato',
        'form': contact_form
    }
    if request.method == 'POST' and contact_form.is_valid():
        contact_form.cleaned_data
        print(contact_form.cleaned_data)

    return render(request, 'contact/view.html', context)
