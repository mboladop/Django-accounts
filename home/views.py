from django.shortcuts import render
from .models import Author

# Create your views here.
def get_index(request):
    authors = Author.objects.all()
    return render(request, "home/index.html", {'authors': authors})