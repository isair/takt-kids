from django.shortcuts import render, redirect


def index(request):
    if not request.user.is_authenticated():
        return redirect('/login')

    if request.user.groups.filter(name='Jury').count():
        return redirect('/cosplay/dashboard')

    if request.user.is_staff:
        return redirect('/')

    return render(request, 'reception/index.html', {
        'username': request.user.username
    })
