// Initialize Chart.js
let predictionChart = null;

// Function to validate input
function validateInput(input, min, max) {
    const value = parseFloat(input.value);
    if (isNaN(value) || value < min || value > max) {
        input.style.borderColor = 'var(--error-color)';
        return false;
    }
    input.style.borderColor = 'var(--border-color)';
    return true;
}

// Function to predict admission chance
async function predict() {
    try {
        // Get and validate input values
        const inputs = {
            gre: { element: document.getElementById('gre'), min: 260, max: 340 },
            toefl: { element: document.getElementById('toefl'), min: 0, max: 120 },
            university: { element: document.getElementById('university'), min: 1, max: 5 },
            sop: { element: document.getElementById('sop'), min: 1, max: 5 },
            lor: { element: document.getElementById('lor'), min: 1, max: 5 },
            cgpa: { element: document.getElementById('cgpa'), min: 0, max: 10 },
            research: { element: document.getElementById('research') }
        };

        let isValid = true;
        const data = {};

        // Validate all inputs
        for (const [key, { element, min, max }] of Object.entries(inputs)) {
            if (key === 'research') {
                if (!element.value) {
                    element.style.borderColor = 'var(--error-color)';
                    isValid = false;
                } else {
                    element.style.borderColor = 'var(--border-color)';
                    data[key] = parseInt(element.value);
                }
            } else {
                if (!validateInput(element, min, max)) {
                    isValid = false;
                } else {
                    data[key] = parseFloat(element.value);
                }
            }
        }

        if (!isValid) {
            throw new Error('Please enter valid values for all fields');
        }

        // Prepare data for API request
        const formattedData = {
            'GRE Score': data.gre,
            'TOEFL Score': data.toefl,
            'University Rating': data.university,
            'SOP': data.sop,
            'LOR': data.lor,
            'CGPA': data.cgpa,
            'Research': data.research
        };

        // Show loading state
        const resultDiv = document.getElementById('result');
        resultDiv.className = 'loading';
        resultDiv.textContent = 'Predicting...';
        resultDiv.classList.add('show');

        // Make API request
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(formattedData)
        });

        // Check if response is ok
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error || `Server error: ${response.status}`);
        }

        const result = await response.json();

        // Display result
        if (result.error) {
            resultDiv.className = 'error';
            resultDiv.textContent = result.error;
        } else {
            resultDiv.className = 'success';
            resultDiv.textContent = `chance: ${result.chance}%`;
            updateChart(result.chance);
        }
    } catch (error) {
        document.getElementById('result').className = 'error';
        document.getElementById('result').textContent = error.message;
    }
}

// Update the prediction chart
function updateChart(chance) {
    const ctx = document.getElementById('predictionChart').getContext('2d');
    const chartData = {
        labels: ['Admission Chance', 'Remaining Chance'],
        datasets: [{
            data: [chance, 100 - chance],
            backgroundColor: ['#16a34a', '#e5e7eb'],
            borderColor: ['#16a34a', '#e5e7eb'],
            borderWidth: 1
        }]
    };

    if (predictionChart) {
        predictionChart.data = chartData;
        predictionChart.update();
    } else {
        predictionChart = new Chart(ctx, {
            type: 'doughnut',
            data: chartData,
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: function(tooltipItem) {
                                return `${tooltipItem.label}: ${tooltipItem.raw}%`;
                            }
                        }
                    }
                }
            }
    });
}
}
