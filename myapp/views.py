from pickle import FALSE
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from .models import feature,agent
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
def index(request):
    FEATURE  = feature.objects.all()[:3]
    AGENT  = agent.objects.all()
    return render(request,'index.html', {'Feature': FEATURE,'Agent': AGENT})

def home(request):
    FEATURE  = feature.objects.all()
    return render(request,'home.html',{'Feature': FEATURE})

def details(request,id):
    FEATURE  = feature.objects.get(pk=id)
    if request.method == "POST":
        message_name = request.POST['username']
        message_from = request.POST['email']
        message_to = request.POST['omail']
        message = request.POST['message']
        #send_mail(
        #    'Inquiry on property',
        #   message,
        #    message_from,
        #   [message_to],
        #   fail_silently=False
        #)
        messages.success(request,'Thank you'+ message_name +'\n Your message sent successfully')
        return render(request,'details.html',{'Feature': FEATURE})

    return render(request,'details.html',{'Feature': FEATURE})

def properties(request):
    if request.method == "POST":
        pro = feature()
        pro.name = request.POST['name']
        pro.address = request.POST['address']
        pro.price = request.POST['price']
        pro.area = request.POST['area']
        pro.beds = request.POST['beds']
        pro.baths = request.POST['baths']
        pro.oname = request.POST['oname']
        pro.oaddress = request.POST['oaddress']
        pro.omail = request.POST['omail']
        pro.ophone = request.POST['ophone']

        if len(request.FILES) != 0:
            pro.image = request.FILES['image']

        pro.save()
        messages.success(request,'Inserted Sucessfully')
        return redirect('/')

    return render(request,'properties.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword= request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'UserName already used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        
        else:
            messages.info(request, 'Password is not same')

    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Credentials Invalid")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')