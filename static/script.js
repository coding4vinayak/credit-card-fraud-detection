document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect form data
    const formData = new FormData(event.target);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Send data to the server
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').style.display = 'block';
        document.getElementById('prediction').textContent = result.prediction;
        document.getElementById('probability').textContent = result.probability.toFixed(4);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
