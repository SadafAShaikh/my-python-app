import signal
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

# Function to handle graceful shutdown
def shutdown_signal_handler(sig, frame):
    print('Shutting down gracefully...')
    # Perform any cleanup tasks here if needed
    sys.exit(0)

# Register the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, shutdown_signal_handler)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
