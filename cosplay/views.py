from cosplay.models import Cosplayer, JuryVote
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

    cosplayer_id = request.GET.get('cosplayer', None)

    if cosplayer_id:
        cosplayer = Cosplayer.objects.get(id=cosplayer_id)
    else:
        cosplayer = None

    try:
        jury_votes = JuryVote.objects.get(jury_member=request.user)
    except:
        jury_votes = None

    return render(request, 'cosplay/dashboard.html', {
        'cosplayers': Cosplayer.objects.all(),
        'selected_cosplayer': cosplayer,
        'jury_votes': jury_votes
    })


def juryvote(request):
    return redirect('/cosplay/dashboard')
