from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(request.POST.get('group'))
            login(request, user)
            return redirect ('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Tu cuenta no está activa'})
        else:
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')
    
