from django.shortcuts import render
from .models import UserForm, User
import json
import os
from django.http import JsonResponse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'users.storage.json')

def add_user_to_storage(user_data):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users=[]
    
    existing_emails = {user['email'] for user in users}
    if user_data['email'] in existing_emails:
        raise ValueError('Email já cadastrado.')
                  
    new_id = max((user['id'] for user in users), default=0) + 1
    user_data['id'] = new_id

    users.append(user_data)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)
    

def index(request):
    return render(request, 'login.html')

def registerController(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password-repeat')

        form = UserForm(name, email, password, password_repeat)

        errors = form.is_valid()
        if errors is True:
            user = User(form.username, form.email, form.password)
            add_user_to_storage(user.to_dict())
        else:
            context['register_errors'] = errors

    return render(request, 'login.html', context)

def loginController(request):
    return render(request, 'login.html')
