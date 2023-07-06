from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Define a route that will return a JSON response
@app.route('/', methods=['GET'])
def example_route():
    return render_template("index.html")

# Handle the "Not Found" error
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found'}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

