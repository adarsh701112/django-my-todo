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

def update(request,id):
    user_data = get_object_or_404(User,id=id)
    if request.method == "POST":
        User.name = request.POST["name"]
        User.email = request.POST["email"]
        User.age = request.POST["age"]
        User.password = request.POST["password"]
           
     # Handle Profile Image (Keep the old image if none is uploaded)
        if "profile" in request.FILES:
            User.profile = request.FILES["profile"]
        messages.success(request, "User updated successfully!")
        
        return redirect('userInsert')
    
    return render(request,'update.html',context={'data':user_data})