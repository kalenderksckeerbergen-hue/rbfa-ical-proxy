
# RBFA iCal Proxy Server

Deze Flask-app biedt aangepaste iCal-feeds voor 8 RBFA-teams met correcte ploegnamen.

## Installatie

1. Maak een GitHub repository aan en voeg deze bestanden toe.
2. Ga naar [Render](https://render.com) en kies "New Web Service".
3. Kies "Deploy from GitHub" en selecteer je repository.
4. Stel de build en start command in:
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `gunicorn app:app`

## Gebruik

Na het deployen kun je aangepaste feeds gebruiken via:
- `/ical/eerste`
- `/ical/dames`
- `/ical/reserven`
- `/ical/u11`
- `/ical/u13`
- `/ical/u17`
- `/ical/u6u7`
- `/ical/u9`

Voeg deze URLs toe aan Google Agenda via "Via URL toevoegen".
