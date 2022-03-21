from django.shortcuts import render, redirect


def Dashboard_View(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        username = request.user.username
        return render(request, 'dash.html', {"username": username})


def Chart_View(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        username = request.user.username
        return render(request, 'chartjs.html', {"username": username})
