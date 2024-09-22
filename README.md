

# Credit Card Fraud Detection

This project implements a credit card fraud detection system using machine learning techniques. The system aims to identify fraudulent transactions by analyzing transaction data and using classification algorithms to predict fraud.

## Features

- **Data Preprocessing**: Clean and prepare credit card transaction data for modeling.
- **Fraud Detection**: Classify transactions as fraudulent or legitimate using machine learning models.
- **Model Evaluation**: Evaluate the performance of different classification models.
- **Visualization**: Visualize the results and performance metrics.

## Prerequisites

- Python 3.x
- Flask (for web application interface)
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook (for exploratory data analysis)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/coding4vinayak/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Set up environment variables if needed.

## Usage

### Data Preprocessing

1. **Load and clean the data**:
   - Prepare the dataset by handling missing values, encoding categorical variables, and scaling features.
   
2. **Split the data**:
   - Divide the data into training and testing sets for model evaluation.

### Training and Evaluation

1. **Train Models**:
   - Implement and train various classification algorithms (e.g., Logistic Regression, Random Forest, XGBoost).

2. **Evaluate Models**:
   - Assess model performance using metrics like accuracy, precision, recall, F1-score, and AUC-ROC.

3. **Visualize Results**:
   - Create visualizations to analyze model performance and the distribution of fraud in the dataset.

### Running the Flask Application

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the web interface for submitting transactions and viewing fraud detection results.

## Code Overview

- **app.py**: Main Flask application script.
  - **index()**: Renders the main page.
  - **predict()**: Handles the prediction of fraudulent transactions based on user input.
  
- **model.py**: Contains the implementation of machine learning models and evaluation.
  - **train_models()**: Trains different classification models.
  - **evaluate_models()**: Evaluates the performance of trained models.
  - **predict_fraud()**: Predicts whether a transaction is fraudulent or not.

- **data_preprocessing.py**: Handles data loading, cleaning, and preprocessing.

- **requirements.txt**: Lists the Python packages required for the project.

- **notebooks/**: Contains Jupyter Notebooks for exploratory data analysis and model training.

## Configuration

- **MODEL_PATH**: Path to the trained model file if loading from disk.
- **FLASK_APP_PORT**: Port for the Flask application (default: 5000).

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

---
[coding4vinayak](https://vinayakss.vercel.app/)


