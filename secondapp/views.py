from django.shortcuts import render,redirect
from addapp.models import*
from.models import Register




# Create your views here.
def check1(request):
    data=Category.objects.all()
    return render(request,'index.html',{'data':data})


def det(request):
    return render(request,'details.html')    

def rec(request):
    return render(request,'rep1.html')

def rec1(request):
    return render(request,'rep2.html')    
    
def rec2(request):
    return render(request,'rep3.html')    

def loggin(request):
    return render(request,'login1.html')    

def reggister(request):
    return render(request,'register1.html')    
    
def conttact(request):
    return render(request,'contact.html')  

 

def regdata(request):
    if request.method=="POST":
        fname=request.POST.get('fn')
        mname=request.POST.get('mn')
        lname=request.POST.get('ln')
        agee=request.POST.get('ag')
        add=request.POST.get('add')
        pnumber=request.POST.get('pn')
        data=Register(firstname=fname,middlename=mname,lastname=lname,age=agee,address=add,phonenumber=pnumber)
        data.save()
        return redirect('reggister')

def wel(request):
    return render(request,'welcome.html')

def memberlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('user')
        password_r = request.POST.get('pword')
        if Register.objects.filter(username=username_r,password=password_r).exists():
            data = Register.objects.filter(username=username_r,password=password_r).values('firstname','middlename','lastname','age','address','phonenumber','id',).first()
            request.session['fname'] = data['firstname']
            request.session['mname'] = data['middlename']
            request.session['lname'] = data['lastname']
            request.session['agee'] = data['age']
            request.session['add'] = data['address']
            request.session['pnumber'] = data['phonenumber']
            request.session['username'] = username_r
            request.session['password'] = password_r  
            request.session['uid'] = data['id']
            return redirect('check1')
        else:
            return render(request,'login1.html',{'msg':'INVALID INFO'})
    else:
        return render(request,'login1.html')


def logoutt(request):
    del request.session['fname']
    del request.session['mname']
    del request.session['lname']
    del request.session['agee']
    del request.session['add']
    del request.session['pnumber']
    del request.session['username']
    del request.session['password']    
    del request.session['uid']
    return redirect('check1') 


def jquery(request):
    return render(request,'j1.html')