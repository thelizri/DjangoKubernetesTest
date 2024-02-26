const tempCtx = document.getElementById('tempChart').getContext('2d');
const humidityCtx = document.getElementById('humidityChart').getContext('2d');
const lightCtx = document.getElementById('lightChart').getContext('2d');

var timeLabels = JSON.parse('{{ time_labels|safe }}');
var temperatures = JSON.parse('{{ temperatures|safe }}');
var humidity = JSON.parse('{{ humidity|safe }}');
var light = JSON.parse('{{ light|safe }}');

new Chart(tempCtx, {
  type: 'line',
  data: {
    labels: timeLabels,
    datasets: [{
      label: 'Temperature (F)',
      data: temperatures,
      borderWidth: 1,
      borderColor: 'rgb(255, 99, 132)', // Example color
      backgroundColor: 'rgba(255, 99, 132, 0.2)', // Example color
    }]
  },
  options: {
    scales: {
      y: {
        suggestedMin: 25,
        suggestedMax: 125
      },
      x: {
        ticks: {
          autoSkip: true,
          maxTicksLimit: 10, // Adjust this number based on your preference
          maxRotation: 50,
          minRotation: 50
        }
      },

    },
  }
});

new Chart(humidityCtx, {
  type: 'line',
  data: {
    labels: timeLabels,
    datasets: [{
      label: 'Humidity (%)',
      data: humidity,
      borderWidth: 1,
      borderColor: 'rgb(54, 162, 235)', // Example color
      backgroundColor: 'rgba(54, 162, 235, 0.2)', // Example color
    }]
  },
  options: {
    scales: {
      y: {
        suggestedMin: 15,
        suggestedMax: 85
      },
      x: {
        ticks: {
          autoSkip: true,
          maxTicksLimit: 10, // Adjust this number based on your preference
          maxRotation: 50,
          minRotation: 50
        }
      },
    }
  }
});

new Chart(lightCtx, {
  type: 'line',
  data: {
    labels: timeLabels,
    datasets: [{
      label: 'Light (Lux)',
      data: light,
      borderWidth: 1,
      borderColor: 'rgb(255, 206, 86)', // Example color
      backgroundColor: 'rgba(255, 206, 86, 0.2)', // Example color
    }]
  },
  options: {
    scales: {
      y: {
        suggestedMin: 10,
        suggestedMax: Math.max(...light) + 100
      },
      x: {
        ticks: {
          autoSkip: true,
          maxTicksLimit: 10, // Adjust this number based on your preference
          maxRotation: 50,
          minRotation: 50
        }
      },
    }
  }
});

// Asynchronous data retrieval
var socket = new WebSocket('ws://' + window.location.host + '/ws/chart/');

socket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data.message;
    // Update your chart using the message data
};

socket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
