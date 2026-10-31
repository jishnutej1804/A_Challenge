import "dotenv/config";
import express from "express";
import path from "node:path";
import { fileURLToPath } from "node:url";

const app = express();
const PORT = process.env.PORT || 3000;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Serve the EcoPulse frontend files.
app.use(express.static(path.join(__dirname, "public")));

// Basic health check.
app.get("/api/health", (req, res) => {
  res.json({
    status: "ok",
    service: "EcoPulse Environmental API"
  });
});

// Retrieve air-quality data.
app.get("/api/environmental/air-quality", async (req, res) => {
  const latitude = Number(req.query.latitude);
  const longitude = Number(req.query.longitude);
  const apiKey = process.env.OPENWEATHER_API_KEY;

  if (!Number.isFinite(latitude) || latitude < -90 || latitude > 90) {
    return res.status(400).json({ error: "Invalid latitude." });
  }

  if (!Number.isFinite(longitude) || longitude < -180 || longitude > 180) {
    return res.status(400).json({ error: "Invalid longitude." });
  }

  if (!apiKey) {
    return res.status(500).json({
      error: "OpenWeather API key is not configured."
    });
  }

  try {
    const url = new URL(
      "https://api.openweathermap.org/data/2.5/air_pollution"
    );

    url.searchParams.set("lat", latitude);
    url.searchParams.set("lon", longitude);
    url.searchParams.set("appid", apiKey);

    const response = await fetch(url);

    if (!response.ok) {
      console.error("OpenWeather returned HTTP", response.status);
      return res.status(502).json({
        error: "Unable to retrieve air-quality data."
      });
    }

    const data = await response.json();
    return res.json(data);
  } catch (error) {
    console.error("Air-quality request failed:", error.message);
    return res.status(502).json({
      error: "The air-quality service is temporarily unavailable."
    });
  }
});

// Export the app so Vercel can handle incoming requests.
export default app;

// Start a local server only when this file is run directly.
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  app.listen(PORT, () => {
    console.log(`EcoPulse server running at http://localhost:${PORT}`);
  });
}