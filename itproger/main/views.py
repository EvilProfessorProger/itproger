from django.shortcuts import render


def index(request):
    data = {
    'title': 'Головна сторінка',
    'values': ['Hi','Antosha','Dodik'],

    'obj':{
        'car':'You',
        'age': 'love',
        'hobby': 'WoT'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

