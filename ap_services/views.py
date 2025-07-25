from django.shortcuts import render, redirect

from ap_courses.models import Course

from utils import list_courses

def card(request):
    value_total_cart = 0
    
    for course in list_courses:
        value_total_cart += course.price

    return render(request, 'ap_services/cart.html', context={
        'quantity': len(list_courses),
        'courses': list_courses,
        'value_total': value_total_cart
    })


def add_cart(request, pk):
    if Course.objects.get(pk=pk) not in list_courses:
        list_courses.append(Course.objects.get(pk=pk))

    return redirect(request.META.get('HTTP_REFERER'))


def remove(request, slug):
    for course in list_courses:
       if course.slug == slug:
           list_courses.remove(course)
    
    return redirect('cart')


def service_teach(request):
    return render(request, 'ap_services/service-teach.html', context={
         'quantity_cart': len(list_courses)
    })

