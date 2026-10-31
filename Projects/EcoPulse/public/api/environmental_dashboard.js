
import { getAirQuality } from "./environmental_service.js";

const statusElement = document.getElementById("airQualityStatus");
const indexElement = document.getElementById("airQualityIndex");
const labelElement = document.getElementById("airQualityLabel");
const pm25Element = document.getElementById("airPm25");
const pm10Element = document.getElementById("airPm10");
const refreshButton = document.getElementById("refreshAirQuality");

const aqiLabels = {
  1: "Good",
  2: "Fair",
  3: "Moderate",
  4: "Poor",
  5: "Very Poor"
};

async function loadAirQuality() {
  refreshButton.disabled = true;
  statusElement.textContent = "Getting your location...";
  labelElement.textContent = "Loading air-quality readings";

  try {
    if (!navigator.geolocation) {
      throw new Error("Geolocation is not supported by this browser.");
    }

    const position = await new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject, {
        enableHighAccuracy: false,
        timeout: 10000,
        maximumAge: 300000
      });
    });

    statusElement.textContent = "Fetching air-quality data...";

    const data = await getAirQuality({
      latitude: position.coords.latitude,
      longitude: position.coords.longitude
    });

    const reading = data?.list?.[0];
    const aqi = reading?.main?.aqi;
    const components = reading?.components;

    if (
      !reading ||
      !Number.isInteger(aqi) ||
      !aqiLabels[aqi] ||
      !Number.isFinite(components?.pm2_5) ||
      !Number.isFinite(components?.pm10)
    ) {
      throw new Error("The service returned incomplete air-quality data.");
    }

    indexElement.innerHTML = `${aqi} <small>AQI (1–5)</small>`;
    labelElement.textContent = aqiLabels[aqi];
    pm25Element.textContent = components.pm2_5.toFixed(2);
    pm10Element.textContent = components.pm10.toFixed(2);
    statusElement.textContent = "Air-quality data loaded successfully.";
  } catch (error) {
    indexElement.innerHTML = `-- <small>AQI (1–5)</small>`;
    labelElement.textContent = "Data unavailable";
    pm25Element.textContent = "--";
    pm10Element.textContent = "--";

    if (error.code === 1) {
      statusElement.textContent =
        "Location permission denied. Allow location access and try again.";
    } else if (error.code === 3) {
      statusElement.textContent =
        "Location request timed out. Please try again.";
    } else {
      statusElement.textContent = error.message || "Unable to load air-quality data.";
    }
  } finally {
    refreshButton.disabled = false;
  }
}

refreshButton.addEventListener("click", loadAirQuality);
loadAirQuality();
