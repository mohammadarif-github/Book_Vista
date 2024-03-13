from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import BookModel
from .forms import AddBookForm
from django.utils.text import slugify
from django.contrib import messages
from django.db.models import Q
import pdb

# Create your views here.


def home(request):
    return render(request,"home.html")

def book_list(request):
    return render(request,"show_books.html")

def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("homepage")
    return render(request,"registration.html",{"form":form,})

def user_logout(request):
    logout(request)
    return redirect("login")

def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=user_name, password=password)

        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            messages.error(request,"Invalid username or password. Please try again.")
    return render(request, "login.html")


@login_required(login_url="login")
def add_book(request):
    form = AddBookForm()

    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)  # Add request.FILES here
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.slug = slugify(book.book_title)
            book.save()
            return redirect("show_book")

    return render(request, "add_book.html", {"form": form})

def show_book(request):
    books = BookModel.objects.all()
    return render(request,"show_books.html",{"book_list":books})


def profile(request):
    user = request.user
    book_list = BookModel.objects.filter(owner=user)
    context ={
        "user":user,
        "book_list":book_list,
    }
    return render(request,"profile.html",context)

@login_required(login_url="login")
def edit_book(request, id):
    book = get_object_or_404(BookModel, pk=id)
    form = AddBookForm(instance=book)

    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.slug = slugify(book.book_title)
            book.save()
            return redirect("profile")
        else:
            print("Form Error:", form.errors)
    return render(request, "edit_book.html", {"form": form, "book": book})

def search_book(request):
    searching_book = request.GET.get("search",'')
    
    books = BookModel.objects.filter(
        Q(book_title__icontains=searching_book) | Q(author__icontains=searching_book) 
    )

    return render(request, "show_books.html", {"book_list": books})

def delete_book(request,id):
    book = BookModel.objects.get(pk=id).delete()
    return redirect("profile")
    
    
def show_pdf(request,id):
    book = BookModel.objects.get(pk=id)
    print(book.pdf.url)
    return render(request,"show_pdf.html",{"book":book})