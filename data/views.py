from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Record, High_school, Accolade, College
from .forms import PlayerForm
from django.http.response import JsonResponse
import simplejson as json
# Create your views here.


def soccer(request):
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'index.html', context)

def search(request):
    if request.method == "POST":

        form = PlayerForm(request.POST)
        players = Player.objects.all()

        league_id = request.POST['League']
        position_id = request.POST['Positions']
        year_id = request.POST['Starter_Year']
        all_id = request.POST['All_Conference_Year']

        if position_id and position_id != '0':
            players = players.filter(id__in=Record.objects.filter(
                Position1=int(position_id)).values_list('Player_id'))

        if league_id and league_id != '0':
            players = players.filter(
                College__College_League=int(league_id)).order_by('id')

        if year_id and year_id != '0':
            from django.db.models import Count
            starter_record = Record.objects.filter(Is_starter=True).values(
                'Player_id').annotate(total=Count('Player_id')).filter(total=year_id)
            players = players.filter(
                id__in=starter_record.values_list('Player_id'))

        if all_id and all_id != '0':
            from django.db.models import Count
            all_acc = Accolade.objects.values('Player_id').annotate(
                total=Count('Player_id')).filter(total=all_id)
            players = players.filter(id__in=all_acc.values_list('Player_id'))

        hs = High_school.objects.filter(id__in=players.values_list('High_School_id'))
        college = College.objects.filter(id__in=players.values_list('College_id'))

        hs_json = json.dumps(list(hs.values()), use_decimal=True)
        players_json = json.dumps(list(players.values()), use_decimal=True)
        college_json = json.dumps(list(college.values()), use_decimal=True)

        context = {
            'players': players,
            'form': form,
            'hs_json': hs_json,
            'players_json': players_json,
            'college_json': college_json
        }

        return render(request, 'search.html', context)
    form = PlayerForm()
    return render(request, 'search.html', {'form': form})
