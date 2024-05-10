from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY"

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and display weather
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'].capitalize()
        }
        return render_template('weather.html', weather_data=weather_data)
    else:
        error_message = f"Error: {data['message']}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

