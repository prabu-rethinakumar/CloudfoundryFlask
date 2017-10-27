from flask import *
import os

app = Flask(__name__)

port = int(os.environ.get("PORT", 3000))

@app.route('/')
def run_job():
	return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
