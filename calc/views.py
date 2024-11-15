from django.shortcuts import render

def new(request):

    return render(request, 'home.html', {'name':'Gaurab'}, {'title': 'Gaurab Badu'})

