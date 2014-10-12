from cosplay.models import Cosplayer, JuryVote
from django.shortcuts import render, redirect
from main.models import get_current_event


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
        jury_votes = JuryVote.objects.filter(jury_member=request.user)
    except:
        jury_votes = None

    return render(request, 'cosplay/dashboard.html', {
        'cosplayers': Cosplayer.objects.filter(ticket__event=get_current_event()),
        'selected_cosplayer': cosplayer,
        'jury_votes': jury_votes
    })


def juryvote(request):
    if not request.user.is_authenticated():
        return redirect('/cosplay/login')

    if not request.user.groups.filter(name='Jury').count():
        return redirect('/reception')

    if request.method != 'POST':
        return redirect('/cosplay/dashboard')

    # Check if selected cosplayer is provided and is valid.
    selected_cosplayer_id = request.POST.get('selected_cosplayer', None)

    if not selected_cosplayer_id:
        print('selected cosplayer id not provided')
        return redirect('/cosplay/dashboard')

    try:
        selected_cosplayer = Cosplayer.objects.get(id=selected_cosplayer_id)
    except:
        selected_cosplayer = None

    if not selected_cosplayer:
        print('selected cosplayer not found')
        return redirect('/cosplay/dashboard')

    # Check if vote points is provided and is valid.
    vote_points = request.POST.get('vote_points', None)

    if not vote_points:
        print('vote points not provided')
        return redirect('/cosplay/dashboard')

    vote_points = int(vote_points)

    if vote_points < 0:
        vote_points = 0
    elif vote_points > 10:
        vote_points = 10

    # Check if there is already a vote given to this contestant in this event.
    try:
        jury_vote = JuryVote.objects.get(jury_member=request.user, contestant=selected_cosplayer)
    except:
        jury_vote = None

    # Add vote to system.
    if not jury_vote:
        jury_vote = JuryVote(jury_member=request.user, contestant=selected_cosplayer, vote_points=vote_points)
    else:
        jury_vote.vote_points = vote_points

    try:
        jury_vote.save()
    except:
        print('error while saving vote')
        return redirect('/cosplay/dashboard?cosplayer=' + request.POST.get('selected_cosplayer', None))

    return redirect('/cosplay/dashboard?cosplayer=' + request.POST.get('selected_cosplayer', None))


def top_cosplayers(request):
    jury_vote_averages = []
    cosplayers = Cosplayer.objects.filter(ticket__event=get_current_event())

    if cosplayers:
        for cosplayer in cosplayers:
            jury_votes = JuryVote.objects.filter(contestant=cosplayer)

            if jury_votes:
                jury_votes_average = 0
                jury_votes_count = 0
                for jury_vote in jury_votes:
                    jury_votes_average += jury_vote.vote_points
                    jury_votes_count += 1
                jury_votes_average /= jury_votes_count
                jury_vote_averages.append((jury_votes_average, cosplayer))
        jury_vote_averages = reversed(sorted(jury_vote_averages, key=lambda x: x[1]))

        return render(request, 'cosplay/top.html', {
            'jury_vote_averages': jury_vote_averages
        })
    else:
        return render(request, 'cosplay/top.html')
