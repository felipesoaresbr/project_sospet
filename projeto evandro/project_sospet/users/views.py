from django.shortcuts import render
from .models import User
import json

def login(request):
    return render(request, 'login.html')

def registerController(request):
    errors = []
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password-repeat')

        if not name or not email or not password or not password_repeat:
            errors.append('Todos os campos devem ser preenchidos.')
        if password != password_repeat:
            errors.append('Senhas não coincidem.')
        if len(password) < 6:
            errors.append('Senha deve conter pelo menos 6 caractéres.')

        if errors:
            for error in errors:
                print(error)
        else:
            user = User(username=name, email=email, password=password)
            print(f"Usuário criado: {user.username}, {user.email}")

    return render(request, 'login.html')
