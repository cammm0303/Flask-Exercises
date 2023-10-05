# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Instantiate Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Result route when form is submitted
@app.route('/result', methods=['GET'])
def result():
    # Check if query parameter is included
    if 'number' in request.args:
        # Get the entered number from the query parameter
        number = request.args['number']
        # Check if the entered number is an integer
        if number.isdigit():
            # Convert the number to an integer
            number = int(number)
            # Check if the number is even or odd
            if number % 2 == 0:
                result = "Even number"
            else:
                result = "Odd number"
            # Render the result template with the appropriate message
            return render_template('result.html', result=result)
        # If the entered number is not an integer, display an error message
        else:
            return render_template('result.html', result="Not an integer")
    # If no query parameter is included, display error message
    else:
        return render_template('result.html', result="This is probably not a number")

# Link to go back to the home page
@app.route('/home')
def home():
    return redirect(url_for('index'))