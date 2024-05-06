from django.shortcuts import render,redirect
from .models import program
# Create your views here.
def all(request):
    data=program.objects.all()
    return render(request,"all.html",{"data":data})
def search(request):
    if request.method =="POST":
        option=request.POST.get("option")
        value=request.POST.get("value")
        if option=="eid":
            datas=program.objects.filter(eid=value)
        elif option=="name":
            datas=program.objects.filter(name=value)
        return render(request,"search.html",{"datas":datas})
    return render(request,"search.html")
def delete(request):
    if request.method=="POST":
        eid=request.POST.get("eid")
        n=program.objects.get(eid=eid)
        n.delete()
        return redirect(all)
    return render(request,"delete.html")
def update(request):
    if request.method == "POST":
        eid = request.POST.get("eid")
        option = request.POST.get("option")
        value = request.POST.get("value")
        
        if eid:  
            data = program.objects.filter(eid=eid)
            if data.exists():  
                if option and value:
                    if option == "phone":
                        data.update(phone=value)
                    elif option == "email":
                        data.update(email=value)
                    elif option == "position":
                        data.update(position=value)
                    elif option == "salary":
                        data.update(salary=value)
                else:
                    return render(request, "update.html")

                
                
                data = program.objects.filter(eid=eid)
                return render(request, "update.html", {"datas": data})

            
        else:
            return render(request, "update.html")
    else:
        
        return render(request, "update.html")
   
def home(request):
    return render(request,"home.html")
def master(request):
  return render(request,"master.html")
def edetails(request):
    if request.method=="POST":
        eid=request.POST.get('eid')
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        date=request.POST.get('date')
        position=request.POST.get('position')
        salary=request.POST.get('salary')
        program.objects.create(eid=eid,name=name,age=age,phone=phone,email=email,date=date,position=position,salary=salary)
        m="successfully added"+name
        return render(request,"edetails.html",{"name":m})
    return render(request,"edetails.html")
def deleteall(request):
    program.objects.all().delete()
    return redirect(all)