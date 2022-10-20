import math

from django.shortcuts import render, redirect

from gamesplay.games_play import forms, models
from gamesplay.games_play.forms import ProfileModelForm

def base_view(request):
    pass

def base_html(request):
    profile = models.ProfileModel.objects.first()
    context = {'profile': profile}
    return render(request, 'base.html', context)


def home_page(request):
    profile = models.ProfileModel.objects.first()
    context = {'profile': profile}
    return render(request, 'home-page.html', context=context)


def dashboard_page(request):
    games = models.GameModel.objects.all()
    all_stars = []
    for game in games:
        ceil_stars = math.ceil
        all_stars.append(ceil_stars)
    context = {'games': games, 'all_stars': all_stars}
    return render(request, 'dashboard.html')


def create_profile(request):
    if request.method == "POST":
        form = forms.ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = forms.ProfileModelForm
    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = models.ProfileModel.objects.first()
    all_games = models.GameModel.objects.all()
    total_games = len(all_games)
    try:
        average_rating = sum(game.rating for game in all_games) / total_games
    except ZeroDivisionError:
        average_rating = 0
    context = {'profile': profile, 'average_rating': average_rating, 'total_games': total_games}

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = models.ProfileModel.objects.first()
    if request.method == "GET":
        context = {'form': forms.ProfileEditForm(initial=profile.__dict__)}
        return render(request, 'edit-profile.html', context=context)
    else:
        form = forms.ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')
        else:
            context = {'form': form}
            return render(request, 'edit-profile.html', context=context)


def delete_profile(request):
    profile = models.ProfileModel.objects.first()
    games = models.GameModel.objects.all()
    if request.method == "POST":
        profile.delete()
        games.delete()
        return redirect('home-page')

    return render(request, 'delete-profile.html')


def create_game(request):
    if request.method == "POST":
        form = forms.GameModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
    else:
        form = forms.GameModelForm
    context = {'form': form}
    return render(request, 'create-game.html', context=context)


def details_game(request, pk):
    game = models.GameModel.objects.get(pk=pk)
    context = {'game': game}
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = models.GameModel.objects.get(pk=pk)
    if request.method == "GET":
        context = {'form': forms.GameModelForm(initial=game.__dict__)}
        return render(request, 'edit-game.html', context)
    else:
        form = forms.GameModelForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
        else:
            context = {'form': form}
            return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = models.GameModel.objects.get(pk=pk)
    if request.method == "POST":
        game.delete()
        return redirect('dashboard-page')
    form = forms.GameDeleteForm(instance=game)
    context = {'form': form}
    return render(request, 'delete-game.html', context)
