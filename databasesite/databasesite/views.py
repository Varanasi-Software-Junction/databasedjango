from django.http import HttpResponse
from django.shortcuts import render
from dbuse.models import Book
from . import views


def index(request):
	return HttpResponse("Hello")
	
def test(request):
	return render(request,"test.html")
	

def insert(request):

	book=Book(
	bookname="Progrmming",price="100",subject="C Basic"
	)
	book.save()
	#data={"name":name,"price":price,"subject":subject}
	return HttpResponse("Book Entered")
