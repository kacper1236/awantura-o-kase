# Awantura o kasę
Projekt jest w oparciu o teleturniej "Awantura o kasę". Napisany jest za pomocą Python i Django

## Nieaktualna sekcja, projekt jest w fazie zmiany na inny framework 

Aby uruchomić aktualny projekt, pobierz flask oraz sqlalchemy

# Uruchomienie aplikacji

## Wymagania
Python (testowany na wersji 3.10.X)
Django (najnowszy)
django-cors-headers (najnowszy)

## Uruchomienie
W terminalu należy napisać
```
cd .\awantura_o_kase\
py manage.py runserver
```
Lub pod konkretną wersję pythona
```
py -3.X manage.py runserver
```
Jeżeli 1 raz uruchamiasz projekt to należy wpisać aby móc skorzystać z reacta
```
cd .\stream_overlay\
npm install
```

Przy zmianie CSS lub dodaniu nowych klas z Tailwind'a, w terminalu należy użyć
```
npx tailwindcss -i ./panel_admin/static/admin_panel_style.css -o ./panel_admin/static/tailwind-output.css --watch
```

## Korzystanie

localhost:8000 - admin panel
localhost:8000/stream_panel/ - stream panel 
localhost:5173 - glowny overlay na stream'a
localhost:5173/niebiescy-info - strona informacyjna druzyny niebieskich
localhost:5173/zieloni-info - strona informacyjna druzyny zielonych
localhost:5173/zolci-info - strona informacyjna dla druzyny zoltych
localhost:5173/mistrzowie-info - strona informacyjna dla druzyny mistrzow
localhost:5173/ibisz-info - strona informacyjna dla prowadzacego, pokazuje odpowiedz do pytania
localhost:5173/1na1 - overlay na osobny monitor do pokazania kategorii podczas '1 na 1'

## Dodawanie użytkowników

Aby dodać użytkownika admin należy wpisać
```
py manage.py createsuperuser
```
I wpisać dla user: admin, hasło dowolne

Aby dodać użytkowników do gry (test lub stream) nalezy wpisać
```
py manage.py shell

from django.contrib.auth.models import User
user = User.objects.create_user(username = <user>, password = <password>)
user.save()
#Można ponownie wywołać 2 ostatnie linie aby dodać więcej użytkowników wymaganych
exit()
```
