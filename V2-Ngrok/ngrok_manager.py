import subprocess
import time
import requests

def start_ngrok(port):
    # Start ngrok process
    ngrok_process = subprocess.Popen(['ngrok', 'tcp', str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Give ngrok some time to start
    time.sleep(5)
    
    # Fetch the public URL from ngrok API
    try:
        tunnel_url = requests.get('http://localhost:4040/api/tunnels').json()['tunnels'][0]['public_url']
    except Exception as e:
        ngrok_process.terminate()
        raise RuntimeError("Failed to get ngrok tunnel URL: " + str(e))

    return tunnel_url, ngrok_process
