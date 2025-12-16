from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# --- Routes ---

@app.route('/')
def index():
    """
    Renders the welcome page (index.html).
    """
    return render_template('index.html')

@app.route('/main')
def main_form():
    """
    Renders the main grievance form page (main.html).
    """
    return render_template('main.html')

# --- Run the App ---

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible on your local network
    # debug=True automatically reloads the server on code changes
    app.run(host='0.0.0.0', port=5000, debug=True)
