from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pobierz', methods=['POST'])
def get_currency():
    waluta = request.form.get('waluta', '').upper()
    okres = request.form.get('okres')
    
    dzisiaj = datetime.now().date()
    
    dni_map = {
        '3dni': 3,
        'tydzien': 7,
        '3tygodnie': 21,
        'miesiac': 30,
        '3miesiace': 90,
        '6miesiecy': 180,
        'rok': 365
    }
    
    liczba_dni = dni_map.get(okres, 7)
    start_date = dzisiaj - timedelta(days=liczba_dni)

    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{start_date}/{dzisiaj}/?format=json"
    
    try:
        res = requests.get(url)
        if res.status_code == 200:
            dane = res.json()['rates']
            dane.reverse() 
            return render_template('index.html', dane=dane, waluta=waluta, wybrany_okres=okres)
        else:
            return render_template('index.html', blad=f"Brak danych dla {waluta} w tym okresie.")
    except Exception as e:
        return render_template('index.html', blad="Problem z połączeniem z API NBP.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)