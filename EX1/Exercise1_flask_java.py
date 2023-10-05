from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
     curr_time = datetime.datetime.now()
     return render_template('Exercise1_flask.html', curr_time)


if __name__ == '__main__':
# Running the application and leaving the debug mode ON
    app.run(debug=True)