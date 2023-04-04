from django.shortcuts import render,redirect
from.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def display(request):
    return render(request,"productdata.html")

def hello(request):
    return render(request,'adminindex.html')  

def sdata(request):
    if request.method=="POST":
        recname=request.POST.get("recipename")
        recprice=request.POST.get("recipeprice")
        recing=request.POST.get("recipeingredients")
        image_a=request.FILES["img"]  
        data=Recipe(recipename=recname,recipeprice=recprice,recipeingredients=recing,image=image_a)
        data.save()
        return redirect('display')


def check(request):
    data=Recipe.objects.all()
    return render(request,'viewproduct.html',{'data':data})


def edit(request,id):
    data=Recipe.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})   

def update(request,id):
    if request.method=="POST":
        recname=request.POST.get("recipename")
        recprice=request.POST.get("recipeprice")
        recing=request.POST.get("recipeingredients")
        image_a=request.FILES["img"]  

        try:
            image_a = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(image_a.name, image_a)
        except MultiValueDictKeyError:
            file = Recipe.objects.get(id=id).img
        Recipe.objects.filter(id=id).update(recipename=recname,recipeprice=recprice,recipeingredients=recing,image=file)
        return redirect('check')

def delete(request,id):
    Recipe.objects.filter(id=id).delete()
    return redirect('check')

def sam(request):
    return render(request,'sample.html')    

def dem(request):
    return render(request,'demo.html')

def log(request):
    return render(request,'login.html')    

def adlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            request.session['username_abc'] = username
            request.session['password_abc'] = password
            request.session['uid'] = user['id']
            return redirect('display')
        else:
            return render(request,'login.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')


def adlogout(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(username=username1,password=password1)
        if user is not None:
            login(request, user)
            request.session['username_abc'] = username1
            request.session['password_abc'] = password1
            #request.session['uid'] = user['id']
            return redirect('log')
        else:
            return render(request,'logout.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request,'logout.html')


def cat1(request):
    return render(request,'categorydetail.html')

def cat2(request):
    if request.method=="POST":
        catname=request.POST.get('cname')
        catimage=request.FILES['cimage']
        data=Category(categoryname=catname,categoryimage=catimage)
        data.save()
        return redirect('cat1')

def cattable(request):
    data=Category.objects.all()
    return render(request,'categoryview.html',{'data':data})

def edit1(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'categoryedit.html',{'data':data})

def update1(request,id):
    if request.method=="POST":
        catname=request.POST.get("cname")
        catimage=request.FILES["cimage"]  

        try:
            catimage = request.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(catimage.name, catimage)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).cimage
        Category.objects.filter(id=id).update(categoryname=catname,categoryimage=catimage)
        return redirect('cattable')

def delete1(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('cattable')

def hello(request):
    return render(request,'productdetails.html')

def pdata(request):
    if request.method=="POST":
        proname=request.POST.get('pname')
        proimage=request.FILES['pimage']
        proprice=request.POST.get('pprice')
        cat=request.POST.get('pcat')
        data=Product(productname=proname,productimage=proimage,productprice=proprice,category=cat)
        data.save()
        return redirect('hello')

def protable(request):
    data=Product.objects.all()
    return render(request,'productview.html',{'data':data})

def edit2(request,id):
    data=Product.objects.filter(id=id)
    return render(request,'productedit.html',{'data':data})

def update2(request,id):
    if request.method=="POST":
        proname=request.POST.get("pname")
        proimage=request.FILES["pimage"]
        proprice=request.POST.get('pprice')
        cat=request.POST.get('pcat') 
        try:
            proimage = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(proimage.name, proimage)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).pimage
        Product.objects.filter(id=id).update(productname=proname,productimage=file,productprice=proprice,category=cat)
        return redirect('protable')

def delete2(request,id):
    Product.objects.filter(id=id).delete()
    return redirect('protable')
