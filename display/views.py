from django.shortcuts import render
from django.http import HttpResponse
from .models import  Contact



# Create your views here.

def home(request):
    # images = profile.objects

    return render(request,'display/home.html')
# {'images':images}

def contact(request):
    if request.method== "POST":
        # print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
         
        sent_mail(
            name,
            phone,
            email,
             ['nrimsha55@gmail.com'],
         )

        

       # print(email,name, phone, desc )
#after importng the model here add the moadel..
# the name is for model eg email=email and the secont is in the veiws
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
 
    return render(request,'display/contact.html')
