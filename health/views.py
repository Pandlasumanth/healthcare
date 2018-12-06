from django.shortcuts import render
from  .models import diseases
from .models import nongenric_medicines,genric_medicines,patients_register

# Create your views here.
def homelogin(request):
    type="homepage"
    return render(request,"index.html",{"type":type})
def patientlogin(request):
    try:
        session=request.session['pemail']
        if session != '':
            pdetails=patients_register.objects.filter(Email=session)
            return render(request,"patient_home.html",{"pdetails":pdetails})
        else:
            type = request.GET.get("type")
            return render(request,"index.html",{"type":type})
    except:
        type=request.GET.get("type")
        return render(request,"index.html",{"type":type})


def patientregisterpage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def patientregister(request):
    Id=request.POST.get("idno")
    Name=request.POST.get("name")
    User_id=request.POST.get("userid")
    Contact=request.POST.get("contact")
    Age=request.POST.get("age")
    date_of_birth=request.POST.get('dob')
    Gender=request.POST.get("gender")
    Occupation=request.POST.get("occupation")
    Height=request.POST.get("height")
    Weight=request.POST.get("weight")
    Email=request.POST.get("email")
    Password=request.POST.get("password")
    Address=request.POST.get("address")
    from .models import patients_register
    ps=patients_register(Id=Id,Name=Name,Contact=Contact,Age=Age,Date_of_birth=date_of_birth,Gender=Gender,Occupation=Occupation,Height=Height,Weight=Weight,Email=Email,Password=Password,User_id=User_id,Address=Address)
    ps.save()
    return render(request,"index.html",{"type":'H_patient',"message":'registered successfully'})
def CheckLogin(request):
    email=request.POST.get('pemail')
    password=request.POST.get('ppassword')
    from  .models import patients_register
    cp=patients_register.objects.filter(Email=email,Password=password)
    if cp:
        request.session['pemail']=email
        return render(request,"patient_home.html",{"pdetails":cp})
    else:
        return render(request,"index.html",{"type":"H_patient","message1":"Invalid Details Please Register.."})
def diseaseslogin(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def Generic(request):
    uemail=request.POST.get('generic')
    pdetails=patients_register.objects.filter(Email=uemail)
    generic=genric_medicines.objects.all()
    return render(request,"patient_home.html",{"generic":generic,"pdetails":pdetails})
def NonGeneric(request):
    uemail=request.POST.get('ngeneric')
    pdetails=patients_register.objects.filter(Email=uemail)
    generic=genric_medicines.objects.all()
    return render(request,"patient_home.html",{"ngeneric":generic,"pdetails":pdetails})
def PLogout(request):
    request.session['pemail']=''
    return render(request,"index.html")
