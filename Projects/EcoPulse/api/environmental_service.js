/*
 * EcoPulse Environmental Service
 * Fetches air-quality data from a backend API endpoint.
 * The backend is responsible for securely calling the external provider.
 */

const ENVIRONMENTAL_API_URL = "/api/environmental/air-quality";

/**
 * Fetch current air-quality data for a location.
 * @param {{ latitude: number, longitude: number }} location
 * @returns {Promise<object>}
 */
export async function getAirQuality({ latitude, longitude }) {
  if (!Number.isFinite(latitude) || latitude < -90 || latitude > 90) {
    throw new TypeError("Latitude must be between -90 and 90.");
  }

  if (!Number.isFinite(longitude) || longitude < -180 || longitude > 180) {
    throw new TypeError("Longitude must be between -180 and 180.");
  }

  const url = new URL(ENVIRONMENTAL_API_URL, window.location.origin);
  url.searchParams.set("latitude", latitude);
  url.searchParams.set("longitude", longitude);

  let response;

  try {
    response = await fetch(url, {
      method: "GET",
      headers: { Accept: "application/json" },
      signal: AbortSignal.timeout(10000)
    });
  } catch (error) {
    if (error.name === "TimeoutError") {
      throw new Error("The environmental service timed out.");
    }
    throw new Error("Unable to connect to the environmental service.");
  }

  if (!response.ok) {
    throw new Error(`Environmental service returned HTTP ${response.status}.`);
  }

  const data = await response.json();

  if (!data || typeof data !== "object") {
    throw new Error("The environmental service returned invalid data.");
  }

  return data;
}
