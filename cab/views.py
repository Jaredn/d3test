from django.shortcuts import render

# Create your views here.


def cabtest(request):
    context = {}

    return render(request, 'cabtest.html', context=context)
