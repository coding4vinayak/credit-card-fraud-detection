from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model_path = 'app2/credit.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Extract JSON data from the request
            data = request.json

            # Convert to DataFrame with the correct column names
            input_df = pd.DataFrame([data])

            # Predict using the model
            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1]

            # Return the result as JSON
            result = {
                'prediction': 'Fraudulent' if prediction == 1 else 'Not Fraudulent',
                'probability': probability
            }
            return jsonify(result)

        except Exception as e:
            # Handle errors and provide feedback
            return jsonify({'error': str(e)}), 400

    # Render the HTML form for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
