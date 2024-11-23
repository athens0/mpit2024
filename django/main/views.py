from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Match, Team, Prediction
from datetime import date, timedelta

def index(request):
    return render(request, 'main/index.html')

def analytics(request):
    data = dict()
    ms = Prediction.objects.filter(date__year='2024', date__month='11')
    cur = date(2024, 11, 1)
    rows = []
    while (cur.weekday != 0):
        cur -= timedelta(days=1)
    while cur.month != 11:
        rows.append((cur.day, "hide", -1))
        cur += timedelta(days=1)
    for day in ms:
        if cur.weekday == 6:
            rows.append((cur.day, "red", day.result))
        else:
            rows.append((cur.day, "", day.result))
        cur += timedelta(days=1)
    while cur.weekday != 1:
        if cur.weekday == 6:
            rows.append((cur.day, "hide red", -1))
        else:
            rows.append((cur.day, "hide", -1))
        cur += timedelta(days=1)

    return render(request, 'main/analytics.html', data)

def teams(request):
    data = dict()
    ms = Team.objects.first()
    if ms:
        data["team"] = [i.split(',') for i in ms.staff.split(';')]
    return render(request, 'main/teams.html', data)

def matches(request):
    data = dict()
    ms = Match.objects.all()
    ms_front = []
    for match in ms:
        current = [match.date, match.team1, f"{match.score1} : {match.score2}", match.team2, match.place]
        ms_front.append(current)
    data["matches"] = ms_front
    return render(request, 'main/matches.html', data)

def profile(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')
    if request.method == 'POST':
        pass
    else:
        data = {
            'date_joined': request.user.date_joined.strftime('%d.%m.%y'),
            'last_login': request.user.last_login.strftime('%I:%M %d.%m.%y')
        }
        return render(request, 'main/profile.html', data)

def login_def(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        tp = request.POST.get('type')
        if tp == '0':
            form = UserRegisterForm(request.POST)
        
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            
            data = dict()
            if form.is_valid():
                User.objects.create_user(username, email, password)
                data['message'] = 'Ваш аккаунт успешно создан. Теперь вы можете войти.'
            else:
                data['form'] = form
                
            return render(request, 'main/login.html', data)
        elif tp == '1':
            username = request.POST.get('username')
            password = request.POST.get('password1')
            print(tp, username, password)
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return render(request, 'main/index.html')
            else:
                data = {
                    'error': 'Введенные имя пользователя или пароль неверные'
                }
                return render(request, 'main/login.html', data)
        else:
            pass
    else:
        return render(request, 'main/login.html')

def log_out(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))