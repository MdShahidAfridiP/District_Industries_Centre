from django.shortcuts import render
from django.core.mail import send_mail
from .models import *

def home(request):
    #send_mail('django subject','this is the body of django finally','shahid.cse.rymec@gmail.com',['shahidzainsz77@gmail.com'],fail_silently=False)
    obj_left=left_notification.objects.all()
    obj_right=right_notification.objects.all()
    return render(request,"index.html",{'obj_left':obj_left,'obj_right':obj_right})

def index2(request):
    obj_left = left_notification.objects.all()
    obj_right = right_notification.objects.all()
    return render(request, "index.html", {'obj_left': obj_left, 'obj_right': obj_right})

def index3(request):
    return render(request,"index-3.html")

def index4(request):
    return render(request,"about.html")

def aboutus(request):
    obj=testimonials.objects.all()
    return render(request,"about.html",{'objs':obj})

def services(request):
    return render(request,"services.html")

def policies(request):
    objs=g_policies.objects.all()
    return render(request,"projects.html",{'objs':objs})

def contact(request):
    return render(request, "contact.html")


def contact1(request):
    name=request.POST['username']
    phone=request.POST['phone']
    email=request.POST['email']
    subject=request.POST['subject']
    message=request.POST['message']
    form=f'Name : {name}\n Phone : {phone}\n Email : {email}\n message : {message}'
    send_mail(subject,form,email,['shahidzainsz77@gmail.com'],fail_silently=False)
    return render(request,"contact.html",{'name':name})


def service_details(request):
    return render(request,"service-detail.html")

def service_auto(request):
    return render(request,"service-detail(auto).html")

def service_finance(request):
    return render(request,"service-detail(finance).html")

def service_land(request):
    return render(request,"service-detail(land).html")

def service_power(request):
    return render(request,"service-detail(power).html")

def service_tech(request):
    return render(request,"service-detail(tech).html")

def service_water(request):
    return render(request,"service-detail(water).html")

def gos(request):
    obj=g_orders.objects.all()
    return render(request,"gos.html",{'objs':obj})

def acts(request):
    act_obj=g_acts.objects.all()
    rules_obj=rules.objects.all()
    return render(request,"acts.html",{'act_obj':act_obj,'rules_obj':rules_obj})

def dept(request):
    invest_obj=invester_services.objects.all()
    related_obj=related_dept.objects.all()
    return render(request,"dept.html",{'invest_obj':invest_obj,'related_obj':related_obj})

def mainscheme(request):
    return render(request,"mainscheme.html")

def ruler(request):
    obj=rural_schemes.objects.all()
    return render(request,"rural.html",{'objs':obj})

def dicschemes(request):
    obj=dic_schemes.objects.all()
    return render(request,"schemes.html",{'objs':obj})

def schemepage(request):
    obj = dic_schemes.objects.all()
    return render(request,"schemes.html",{'objs':obj})

def invest(request):
    return render(request,"invest.html")

def why(request):
    return render(request,"why.html")

def district(request):
    return render(request,"district.html")

def indust(request):
    return render(request,"indust.html")
