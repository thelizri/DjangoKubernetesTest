const tempCtx = document.getElementById('tempChart').getContext('2d');
const humidityCtx = document.getElementById('humidityChart').getContext('2d');
const lightCtx = document.getElementById('lightChart').getContext('2d');
const packetList = document.getElementById("packetList");

var timeLabels = JSON.parse('{{ time_labels|safe }}');
var temperatures = JSON.parse('{{ temperatures|safe }}');
var humidity = JSON.parse('{{ humidity|safe }}');
var light = JSON.parse('{{ light|safe }}');

var tempChart = new Chart(tempCtx, {
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

var humidityChart = new Chart(humidityCtx, {
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

var lightChart = new Chart(lightCtx, {
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

socket.onmessage = function (event) {
  var data = JSON.parse(event.data);
  var message = data.message;

  // Assuming 'message' contains new data for each chart
  timeLabels.push(message.time);
  temperatures.push(message.temperature);
  humidity.push(message.humidity);
  light.push(message.light);
  // Update your chart using the message data
  // Update the charts
  updateChartData(tempChart, timeLabels, temperatures);
  updateChartData(humidityChart, timeLabels, humidity);
  updateChartData(lightChart, timeLabels, light);

  // Create a new <li> element
  var newListItem = document.createElement("li");
  newListItem.classList.add("list-group-item");
  newListItem.textContent = message.packet; // Or any other content/formatting you want

  // Append the new <li> to the <ul>
  packetList.prepend(newListItem); // Use prepend to add it as the first item, or use appendChild to add it to the end

};

socket.onclose = function (e) {
  console.error('Chat socket closed unexpectedly');
};

function updateChartData(chart, labelSet, dataSet) {
  chart.data.labels = labelSet;
  chart.data.datasets.forEach((dataset) => {
    dataset.data = dataSet;
  });
  chart.update();
}