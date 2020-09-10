from django.shortcuts import render
from .forms import BurgerForms,MultipleBurgerForms
from django.forms import formset_factory
from .models import Burger

# Create your views here.
def home(request):
    return render (request, 'burger/home.html')

def order(request):
    multiple_form = MultipleBurgerForms()
    if request.method == "POST":
        filled_form = BurgerForms(request.POST)
        if filled_form.is_valid():
            created_burger = filled_form.save()
            created_burger_pk = created_burger.id
            note = " Thank you for ordering %s %s and %s Burger. Expect arrival soon" %(filled_form.cleaned_data['size'],filled_form.cleaned_data['topping1'],filled_form.cleaned_data['topping2'])
            filled_form = BurgerForms()

        else:
            created_burger_pk = None
            note = "Burger Order Failed."
        return render (request, 'burger/order.html', {'created_burger_pk': created_burger_pk,'burgerform' : filled_form, 'note' : note, 'multiple_form':multiple_form})
    else:
        form = BurgerForms()
        return render (request, 'burger/order.html', {'burgerform' : form, 'multiple_form':multiple_form})

def burgers(request):
    number_of_burgers = 2
    filled_multiple_burger_form = MultipleBurgerForms(request.GET)
    if filled_multiple_burger_form.is_valid():
        number_of_burgers = filled_multiple_burger_form.cleaned_data['number']
    burgerFormSet = formset_factory(BurgerForms, extra=number_of_burgers)
    formset = burgerFormSet()
    if request.method == "POST":
        filled_formset = burgerFormSet(request.POST)
        if(filled_formset.is_valid()):
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Burgers have been ordered!'
        else:
            note = 'Order was not created, please try again'
        return render (request, 'burger/burger.html', {'note':note, 'formset':formset})
    else:
        return render (request, 'burger/burger.html', {'formset':formset})

def edit_order(request, pk):
    burger = Burger.objects.get(pk=pk)
    form = BurgerForms(instance=burger)
    if request.method == "POST":
        filled_form = BurgerForms(request.POST,instance=burger)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated.'
            return render(request, 'burger/edit_order.html', {'note':note, 'burgerform':form,'burger':burger})
    return render (request, 'burger/edit_order.html', {'burgerform':form, 'burger': burger})
    