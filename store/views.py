from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Item
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required
def get(request):

    user = User.objects.get(username=request.user.username)
    items =  Item.objects.exclude(owner=request.user.id).exclude(status=True)
    
    data = {"user": user, "items": items}
    return render(request, 'get.html', data)


@login_required
def give(request):

    user = User.objects.get(username=request.user.username)
    items =  Item.objects.filter(owner=request.user.id)
    data = {"user": user, "items": items}
    return render(request, 'give.html', data)


@login_required
def itemView(request,pk):

    user = User.objects.get(username=request.user.username)
    item =  Item.objects.get(id=pk)
    data = {"user": user, "item": item}
    return render(request, 'itemView.html', data)



@login_required
def itemAdd(request):

    if (request.method == 'POST'):
        _, file = request.FILES.popitem()
        file = file[0]
        name = request.POST['pname']
        description = request.POST['pdes']
        price = request.POST['pcost']
        digital = False
        item,created = Item.objects.get_or_create(name=name, description=description, item_pic=file, owner=request.user, price=price, digital=digital, status=False)
        if(created):
            messages.success(request, 'Item listed successfully')
            return redirect('give')
        else:
            messages.error(request, 'Item already exists')
            return redirect('give')

    else:
        user = User.objects.get(username=request.user.username)
        data = {"user": user}
        return render(request, 'itemAdd.html', data)



@login_required
def itemDelete(request,pk):
    
    try:
        item = Item.objects.get(id=pk)
        item.delete()
        messages.success(request, 'Item deleted successfully')
        return redirect('give')
    except:
        messages.error(request, 'Item does not exist')
        return redirect('give')


@login_required
def itemEdit(request,pk):
    
    if (request.method == 'POST'):
        
        item = Item.objects.get(id=pk)
        item.name = request.POST['name']
        item.description = request.POST['description']
        if(len(request.FILES)):
            _, file = request.FILES.popitem()
            file = file[0]
            item.item_pic = file
        item.price = request.POST['price']
        item.save()
        messages.success(request, 'Item edited successfully')
        return redirect('itemEdit',pk=pk)
    
    else:
        try:
            user = User.objects.get(username=request.user.username)
            item =  Item.objects.get(id=pk)
            data = {"user": user, "item": item}
            return render(request, 'edit.html', data)
        except Exception as e:
            print(e)
            messages.error(request, 'Item does not exist')
            return redirect('give')
        


@login_required
def itemSearch(request):

    pk = request.GET['search']
    items = Item.objects.filter(Q(name__icontains=pk)|Q(description__icontains=pk)).distinct().exclude(owner=request.user.id)
    user = User.objects.get(username=request.user.username)
    data = {"user": user, "items": items}
    return render(request, 'searchItem.html', data) 


