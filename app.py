from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']
    return ip


def ip_to_latlong(ip):
    return

@app.route('/')
def index():
    # Get the public IP address
    user_ip = get_public_ip()

    try:
        # Convert IP to latitude and longitude
        latitude, longitude = ip_to_latlong(user_ip)
    except:
        latitude, longitude = 0, 0

    return render_template('index.html', ip=user_ip, latitude=latitude, longitude=longitude)


if __name__ == '__main__':
    app.run(debug=True)
