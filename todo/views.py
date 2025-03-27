from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from todo.models import User    
from django.contrib import messages

def userInsert(request):
    if request.method == 'POST': 
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        age = request.POST.get("age")
        profile = request.FILES.get("profile")  # Correct way to get file

        # Create user instance and save
        p1 = User(
            name=name,
            email=email,
            password=password,
            age=age,
            profile=profile
        )
        p1.save()

        messages.success(request, "User create successfully!")

    # Fetch all users and render template
    data = User.objects.all()
    return render(request, 'insert.html', context={'data': data})

# delete data here !

def delete(request,id):
    p1= get_object_or_404(User, id=id)
    if p1:
        p1.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('userInsert')

# update data here !

def update(request, id):
    user_data = get_object_or_404(User, id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        age = request.POST.get("age")
        profile = request.FILES.get("profile")  
        
        user_data.name = name
        user_data.email = email
        user_data.password = password
        user_data.age = age
        
        if profile:
            user_data.profile = profile  
        
        user_data.save()
        return redirect('userInsert')

    return render(request, 'update.html', context={'data': user_data})