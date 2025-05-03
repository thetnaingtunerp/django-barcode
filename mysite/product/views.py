from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    pro = Product.objects.all()
    context = {'pro':pro}
    return render(request, 'index.html', context)