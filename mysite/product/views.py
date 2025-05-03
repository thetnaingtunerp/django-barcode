from django.shortcuts import render,HttpResponse
from .models import *
from barcode import Code39
import io
# Create your views here.
def index(request):
    pro = Product.objects.all()
    context = {'pro':pro}
    return render(request, 'index.html', context)

def generate_barcode(request, code):
    code_obj = Code39(code, writer=ImageWriter())
    buffer = io.BytesIO()
    code_obj.write(buffer)
    buffer.seek(0)
    barcode_obj, created = GeneratedBarcode.objects.get_or_create(code=code)
    
    if created:
        barcode_obj.image.save(f'{code}.png', buffer, save=True)
        action_performed = "created"
    else:
        action_performed = "fetched"

    myResponse = f'Barcode "{code}" {action_performed} successfully! <a href="{barcode_obj.image.url}">IMAGE LINK</a>'
    
    return HttpResponse(myResponse)