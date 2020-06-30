from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings

def index(request):
    return render(request,'index.html',{})

def contact(request):
    if request.method == 'POST':
        yname = request.POST['yname']
        email = request.POST['email']
        phone = request.POST['phone']
        gsm = request.POST['gsm']
        size = request.POST['size']
        weight = request.POST['weight']
        application = request.POST['application']
        message = request.POST['message']

        # send an mail
        datatuple = (
            ('Message from CK Fabrics','Thank You!  for Contacting us, we will reach you as soon as possible.\n' + 'YOUR SPECIFICATIONS:\n'+'Gsm= '+gsm+ '\n'+ 'Size= '+ size+ '\n' + 'Weight= '+ weight+ '\n'+ 'Application= '+ application + '\n'+ message, settings.EMAIL_HOST_USER,[email]),
            ('Message from '+yname, 'DETAILS OF THE CUSTOMER:\n'+'Name='+ yname + '\n' + 'Email='+ email  +'\n' + 'Mobile number = '+ phone+'\n'+ 'GSM = '+gsm+ '\n'+ 'Size = '+ size+ '\n' + 'Weight = '+ weight+ '\n'+ 'Application: '+ application + '\n' + message, email,[settings.EMAIL_HOST_USER]),
        )
        send_mass_mail(datatuple, fail_silently=False)

        return render(request,'contact.html',{'yname':yname})
    else:
        return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def medical(request):
    return render(request,'medical.html',{})

def filtration(request):
    return render(request,'filtration.html',{})

def packaging(request):
    return render(request,'packaging.html',{})

def agriculture(request):
    return render(request,'agriculture.html',{})

def health(request):
    return render(request,'health.html',{})

def cosmetic(request):
    return render(request,'cosmetic.html',{})

def mattress(request):
    return render(request,'mattress.html',{})

def laminated(request):
    return render(request,'laminated.html',{})

def melt(request):
    return render(request,'melt_blown.html',{})

def spunbond(request):
    return render(request,'spunbond.html',{})
