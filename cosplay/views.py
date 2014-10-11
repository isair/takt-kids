from django.shortcuts import render, redirect


def login(request):
    if request.user.is_authenticated():
        return redirect('/reception')

    return render(request, 'cosplay/login.html')


def dashboard(request):
    if not request.user.is_authenticated():
        return redirect('/cosplay/login')

    if not request.user.groups.filter(name='Jury').count():
        return redirect('/reception')

    # TODO: Page data.

    return render(request, 'cosplay/dashboard.html')
