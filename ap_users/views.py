from django.shortcuts import render

from utils import list_courses

def create_user(request):
    return render(request, 'ap_users/register.html', context={
        'name_page': 'Faça login para continuar sua jornada de aprendizado |Udemy',
        'quantity_cart': len(list_courses)
    })


def login(request):
    return render(request, 'ap_users/login.html', context={
        'name_page': 'Faça login para continuar sua jornada de aprendizado |Udemy',
        'quantity_cart': len(list_courses)
    })
