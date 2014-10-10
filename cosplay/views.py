from django.shortcuts import render, redirect


def login(request):
    if request.user.is_authenticated():
        return redirect('/cosplay/wait')

    return render(request, 'cosplay/login.html')


def wait(request):
    if not request.user.is_authenticated():
        return redirect('/cosplay/login')

    # TODO: Check if user is in jury group.

    return render(request, 'cosplay/wait.html')


def dashboard(request):
    if not request.user.is_authenticated():
        return redirect('/cosplay/login')

    # TODO: Check if user is in jury group.

    return render(request, 'cosplay/dashboard.html')
