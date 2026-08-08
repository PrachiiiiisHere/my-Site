from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
# Create your views here.
def index(requests):
    #getting items from DB
    item_list=Item.objects.all()
    #creating context object
    context={
        'item_list':item_list

    }
    #passing context to render method along with template
    return render (requests,"myApp/index.html",context)

def detail(request, id):
    item=Item.objects.get(id=id)
    context={
        'item':item
    }
    return render(request,'myApp/detail.html',context)


def create_item(request):
    form=ItemForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('myApp:index')

    context={
        'form':form
    }
    return render(request,'myApp/item-form.html',context)

def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('myApp:index')
    context={
        'form':form
    }
    return render(request,'myApp/item-form.html',context)

def delete_item(request, id):
    item=Item.objects.get(id=id)
    if request.method=="POST":
        item.delete()
        return redirect('myApp:index')
    return render(request,'myApp/item-delete.html') #why don't we need context here?
    