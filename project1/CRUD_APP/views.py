from django.shortcuts import render, redirect
from . forms import OrderForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Order

@login_required(login_url='loginform_url')
def orderview(request):
    form = OrderForm()
    template_name = 'CRUD_APP/orderform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showform_url')
    return render(request, template_name, context)

def showview(request):
    data = Order.objects.all()
    template_name = 'CRUD_APP/show.html'
    context = {'data': data}
    return render(request, template_name, context)


def updateview(request, id):
    obj = Order.objects.get(o_id = id)
    form = OrderForm(instance=obj)
    template_name = 'CRUD_APP/orderform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showorder_url')
    return render(request, template_name, context)

def deleteview(request, id):
    obj = Order.objects.get(o_id = id)
    template_name = 'CRUD_APP/confirmation.html'
    context = {}
    if request.method == 'POST':
        obj.delete()
        return redirect('showorder_url')
    return render(request, template_name, context)



