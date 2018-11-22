from django.shortcuts import render

def view_root(request):
    return render(
        request,
        'index.htm'
    )