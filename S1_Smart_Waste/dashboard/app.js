async function fetchBinStatus() {
    try {
        const response = await fetch('/api/bin_status');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        document.getElementById('fill-level').textContent = data.fill_level.toFixed(2);
    } catch (error) {
        console.error('Error fetching bin status:', error);
    }
}

document.getElementById('refresh-data').addEventListener('click', fetchBinStatus);
fetchBinStatus();