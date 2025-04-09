async function fetchSensorData() {
    try {
        const response = await fetch('/api/sensors'); 
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        // Update the frontend with sensor data
        document.getElementById('soil-moisture').textContent = data.soil_moisture.toFixed(2);
        document.getElementById('temperature').textContent = data.temperature.toFixed(2);
        document.getElementById('humidity').textContent = data.humidity.toFixed(2);
        document.getElementById('rainfall').textContent = data.rainfall.toFixed(2);
    } catch (error) {
        console.error('Error fetching sensor data:', error);
    }async function fetchSensorData() {
        const moistureEl = document.getElementById('soil-moisture');
        const tempEl = document.getElementById('temperature');
        const humidityEl = document.getElementById('humidity');
        const rainEl = document.getElementById('rainfall');
      
        // Optional: show loading animation
        moistureEl.textContent = '...';
        tempEl.textContent = '...';
        humidityEl.textContent = '...';
        rainEl.textContent = '...';
      
        try {
          const response = await fetch('/api/sensors'); // Update with your actual API endpoint
          if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
          
          const data = await response.json();
      
          // Display sensor values
          moistureEl.textContent = data.soil_moisture.toFixed(1);
          tempEl.textContent = data.temperature.toFixed(1);
          humidityEl.textContent = data.humidity.toFixed(1);
          rainEl.textContent = data.rainfall.toFixed(1);
        } catch (error) {
          console.error('🚨 Error fetching sensor data:', error);
          moistureEl.textContent = 'Error';
          tempEl.textContent = 'Error';
          humidityEl.textContent = 'Error';
          rainEl.textContent = 'Error';
        }
      }
      
      async function controlIrrigation(status) {
        try {
          const response = await fetch('/api/irrigation', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status })
          });
          if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      
          alert(`✅ Irrigation turned ${status ? 'ON' : 'OFF'}`);
        } catch (error) {
          console.error('🚨 Error controlling irrigation:', error);
          alert('❌ Failed to update irrigation status.');
        }
      }
      
      // Event listeners
      document.getElementById('irrigation-on').addEventListener('click', () => controlIrrigation(true));
      document.getElementById('irrigation-off').addEventListener('click', () => controlIrrigation(false));
      
      // Fetch sensor data every 5 seconds
      fetchSensorData(); // Initial call
      setInterval(fetchSensorData, 5000);
      
}


async function controlIrrigation(status) {
    try {
        const response = await fetch('/api/irrigation', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status })
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        alert(`Irrigation turned ${status ? 'ON' : 'OFF'}`);
    } catch (error) {
        console.error('Error controlling irrigation:', error);
    }
}


document.getElementById('irrigation-on').addEventListener('click', () => controlIrrigation(true));
document.getElementById('irrigation-off').addEventListener('click', () => controlIrrigation(false));


setInterval(fetchSensorData, 5000); // Update every 5 seconds