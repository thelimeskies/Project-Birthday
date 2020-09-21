from django.shortcuts import render
from .models import Index
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('dob') and \
                request.POST.get('email') and request.POST.get('phone_number'):
            post = Index()
            post.firstname = request.POST.get('firstname')
            post.lastname = request.POST.get('lastname')
            post.dob = request.POST.get('dob')
            post.email = request.POST.get('email')
            post.phone_number = request.POST.get('phone_number')
            post.contact_id = request.POST.get('contact_id')
            post.save()
            messages.success(request, "Submitted Successfully.")

            return render(request, 'index.html')

    else:
        return render(request, 'index.html')
