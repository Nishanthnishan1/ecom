from django.shortcuts import render,get_object_or_404,redirect
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import RegistrationForm 






# Create your views here.

def home(request,c_slug=None):
    c_page=None
    product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:
        product_list=products.objects.all().filter(available=True)
        cat=categ.objects.all()
        
    
    return render(request,'index.html',{'pr':product_list,'ct':cat})

def prodDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})


def item(request):
     return render(request,'item.html')


def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    
    return render(request,'search.html',{'qr':query,'pr':prod})







def index(request):
    return render(request,'index.html')



def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process and save the registration data to the UserProfile model
            # Handle password hashing securely (e.g., using Django's built-in authentication system)
            user = form.save()
            return redirect('index')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html')




def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or a user-specific page
                return redirect('profile')  # Change 'profile' to the name of your profile view
    else:
        form = Login()

    return render(request, 'login.html', {'form': form})


