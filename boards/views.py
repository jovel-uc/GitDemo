from django.http import HttpResponse

def home(reguest):
    return HttpResponse('Hello, World!')

# Create your views here.
