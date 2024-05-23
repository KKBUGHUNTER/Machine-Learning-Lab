from flask import Flask, jsonify
import pickle

app = Flask(__name__)

# Load the .pkl file
def load_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Define the route to access the model
@app.route('/model', methods=['GET'])
def get_model():
    model = load_model('Mini Project/Model.pkl')  # Replace 'example.pkl' with your file path
    # Convert the model to JSON and return
    return jsonify({"model": model})

if __name__ == '__main__':
    app.run(debug=True)
