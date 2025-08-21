from flask import Flask, Response
import requests
import re

app = Flask(__name__)

teams = {
    "eerste": ("https://calendar.google.com/calendar/ical/8qr1rkt3kvh3kjg8o2cm2cvsne9mp3rr%40import.calendar.google.com/public/basic.ics", "KFC MERCHTEM - KSC KEERBERGEN"),
    "dames": ("https://calendar.google.com/calendar/ical/u06g58mvqdl0dvd8s4qor4h4a51n1hai%40import.calendar.google.com/public/basic.ics", "KFC MERCHTEM DAMES - KSC KEERBERGEN DAMES"),
    "reserven": ("https://calendar.google.com/calendar/ical/hvpngee0v9tvu4d7ss4d3ai1u9sfank5%40import.calendar.google.com/public/basic.ics", "KFC MERCHTEM RESERVEN - KSC KEERBERGEN RESERVEN"),
    "u11": ("https://calendar.google.com/calendar/ical/svkveka59ja15cj7hucl25j4pvhmbmeu%40import.calendar.google.com/public/basic.ics", "KFC MERCHTEM U11 - KSC KEERBERGEN U11"),
    "u13": ("https://calendar.google.com/calendar/ical/38ju8c4hf1647kd8tnvqqadpp1kbt66g%40import.calendar.google.com/public/basic.ics", "KFC MERCHTEM U13 - KSC KEERBERGEN U13"),
    "u17": ("https://calendar.google.com/calendar/ical/t7eovqaddp3jj50ilccrc0g4mc140t2t%40import.calendar.google.com/public/basic.ics", "KFC MERCHTEM U17 - KSC KEERBERGEN U17"),
    "u6u7": ("https://calendar.google.com/calendar/ical/lgdnpbsg6310hjq45aubr0c78nb10u0g%40import.calendar.google.com/public/basic.ics", "KFC MERCHTEM U6/U7 - KSC KEERBERGEN U6/U7"),
    "u9": ("https://calendar.google.com/calendar/ical/ekbkik295i8c6pjc3sbdorp9ornl19ro%40import.calendar.google.com/public/basic.ics", "KFC MERCHTEM U9 - KSC KEERBERGEN U9")
}

@app.route("/ical/<team>")
def serve_ical(team):
    url, name = teams.get(team, (None, None))
    if not url:
        return "Team niet gevonden", 404
    try:
        data = requests.get(url).text
        # Verwijder bestaande X-WR-CALNAME regels
        data = re.sub(r'X-WR-CALNAME:.*', '', data)
        # Voeg correcte ploegnaam toe
        data = data.replace("BEGIN:VCALENDAR", "BEGIN:VCALENDAR\nX-WR-CALNAME:" + name)
        return Response(data, mimetype="text/calendar")
    except Exception as e:
        return "Fout bij ophalen van kalender: " + str(e), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
