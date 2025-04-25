from flask import Flask, render_template, request
import requests
import datetime
import socket
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    try:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        local_ip = socket.gethostbyname(socket.gethostname())
        public_ip = requests.get('https://api.ipify.org').text
        container_hostname = socket.gethostname()
        service_fqdn = os.environ.get('SERVICE_FQDN', '')

        return render_template('index.html', current_time=current_time, local_ip=local_ip, public_ip=public_ip, container_hostname=container_hostname, service_fqdn=service_fqdn)
    except Exception as e:
        return "An error occurred while processing the request.", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
