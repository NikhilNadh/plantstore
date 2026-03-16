from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Plant, Review, PlantCare


def plant_list(request):
    query = request.GET.get('q')

    if query:
        plants = Plant.objects.filter(name__icontains=query)
    else:
        plants = Plant.objects.all()

    return render(request, 'plant_list.html', {'plants': plants})


def signup_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('plant_list')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def index_view(request):
    return render(request, 'index.html')
def plant_detail(request, id):
    

    plant = get_object_or_404(Plant, id=id)
    reviews = Review.objects.filter(plant=plant)
    care = PlantCare.objects.filter(plant=plant).first()

    if request.method == "POST":
        rating = request.POST['rating']
        comment = request.POST['comment']

        Review.objects.create(
            plant=plant,
            user=request.user,
            rating=rating,
            comment=comment
        )

        return redirect('plant_detail', id=id)

    return render(request, 'plant_detail.html', {
        'plant': plant,
        'reviews': reviews,
        'care': care
    })


