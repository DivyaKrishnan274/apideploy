from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://open-weather13.p.rapidapi.com/city/landon/EN"
HEADERS = {
    "x-rapidapi-key": "09720d47e1msh294d1bfc94be7b4p1d2280jsn1924b50801db",
    "x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

@app.route('/', methods=['GET'])
def index():
    location = request.args.get('location', default='landon')
    url = f"https://open-weather13.p.rapidapi.com/city/{location}/EN"
    response = requests.get(url, headers=HEADERS)
    weather_data = response.json()
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
