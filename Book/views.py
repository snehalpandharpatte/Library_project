from django.shortcuts import render, redirect
from django.http import HttpResponse
from Book.models import Book

# Create your views here.
#DTL ---Django Templating Language
#dynamic data- backend data show on html page by using {{books(pass key)}}
#{for any condition}

import logging
import time
logger = logging.getLogger("first")
# logger.info("In homepage view")

def homepage(request):  #request --httprequest, user defined function
    logger.info("In homepage view")
    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.active_objects.all() # through custom manager
    logger.info(f"All books data: {all_books}")
    
    # print(all_books)
    return render(request, template_name="home.html", context={"books": all_books})


def save_book(request):
    # print("In save Book")
    # print(request.POST)
    logger.info(request.POST)
    b_name = request.POST.get("name")
    b_author = request.POST.get("auth")
    b_price = request.POST.get("price")
    b_qty = request.POST.get("qty")
    b_pub = request.POST.get("pub")
    if b_pub == "on":
        flag = True
    else:
        flag = False       
    if request.POST.get("id"):
        try:
            book_obj = Book.objects.get(id=request.POST.get("id"))
        except Exception as msg:
            logger.error(f"{msg}-----------in exception")

        book_obj.name = b_name
        book_obj.author = b_author
        book_obj.qty = b_qty
        book_obj.price = b_price
        book_obj.is_Published = flag
        book_obj.save()
        return redirect('welcome')
    else:
        b = Book(name=b_name,author=b_author,qty=b_qty,price=b_price,is_Published=flag)
        b.save()
        return redirect('welcome')

def edit_book(request, id):
    try:
        print("AA")
        book_obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        msg = f"No book found for id: {id}"
        return HttpResponse(msg)
    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.active_objects.all()
    return render(request, template_name="home.html", context={"book": book_obj, "books": all_books})

def delete_book(request, id):
    book_obj = Book.objects.get(id=id)
    # book_obj.delete()
    book_obj.is_deleted = 'Y'
    book_obj.save()
    return redirect('welcome')

def hard_delete_book(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.delete()
    return redirect('welcome')

def restore_book(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = 'N'
    book_obj.save()
    return redirect('welcome')


def show_deleted_data(request):
    all_deleted_books = Book.inactive_objects.all()
    return render(request, template_name="home.html", context={"books": all_deleted_books})


def all_restore_book(request):
    inactive_books = Book.inactive_objects.all() 
    for book in inactive_books:
        book.is_deleted = "N"
        book.save()     
    return redirect('welcome')

def all_delete_book(request):
    all_deleted_books = Book.active_objects.all()
    for book in all_deleted_books:
        book.is_deleted = "Y"
        book.save()    
    return redirect('welcome')


