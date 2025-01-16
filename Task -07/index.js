
const iconElement = document.querySelector(".weather-icon");
const tempElement = document.querySelector(".temperature-value p");
const descElement = document.querySelector(".temperature-description p");
const locationElement = document.querySelector(".location p");
const notificationElement = document.querySelector(".notification");
const searchInput = document.querySelector("#search-input");
const searchButton = document.querySelector("#search-button");

const weather = {};
weather.temperature = {
  unit: "celsius",
};

const KELVIN = 273;
const key = "82005d27a116c2880c8f0fcb866998a0";

// Check if browser supports geolocation
if ("geolocation" in navigator) {
  navigator.geolocation.getCurrentPosition(setPosition, showError);
} else {
  notificationElement.style.display = "block";
  notificationElement.innerHTML = "<p>Browser doesn't support geolocation</p>";
}

// Set user position
function setPosition(position) {
  let latitude = position.coords.latitude;
  let longitude = position.coords.longitude;

  getWeatherByCoords(latitude, longitude);
}

// Show error if geolocation fails
function showError(error) {
  notificationElement.style.display = "block";
  notificationElement.innerHTML = `<p>${error.message}</p>`;
}

// Fetch weather using latitude and longitude
function getWeatherByCoords(latitude, longitude) {
  let api = `http://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${key}`;

  fetchWeather(api);
}

// Fetch weather using city name
function getWeatherByCity(city) {
  let api = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${key}`;

  fetchWeather(api);
}

// Fetch weather data from API
function fetchWeather(api) {
  fetch(api)
    .then((response) => response.json())
    .then((data) => {
      if (data.cod === "404") {
        notificationElement.style.display = "block";
        notificationElement.innerHTML = `<p>City not found!</p>`;
        return;
      }
      notificationElement.style.display = "none";
      weather.temperature.value = Math.round(data.main.temp - KELVIN);
      weather.description = data.weather[0].description;
      weather.iconId = data.weather[0].icon;
      weather.city = data.name;
      weather.country = data.sys.country;

      displayWeather();
    })
    .catch((error) => {
      notificationElement.style.display = "block";
      notificationElement.innerHTML = `<p>Error fetching data</p>`;
    });
}

// Display weather to UI
function displayWeather() {
  iconElement.innerHTML = `<img src="icons/${weather.iconId}.png"/>`;
  tempElement.innerHTML = `${weather.temperature.value}°<span>C</span>`;
  descElement.innerHTML = weather.description;
  locationElement.innerHTML = `${weather.city}, ${weather.country}`;
}

// Search functionality
searchButton.addEventListener("click", () => {
  const city = searchInput.value.trim();
  if (city) {
    getWeatherByCity(city);
  }
});

document.addEventListener("DOMContentLoaded", () => {
  updateTime("time");
});

// Update the clock
function updateTime(timeClass) {
  const timeElement = document.querySelector(`.${timeClass}`);

  function setTime() {
    const now = new Date();
    const formattedTime = now.toLocaleTimeString();
    timeElement.textContent = ` ${formattedTime}`;
  }

  setTime();
  setInterval(setTime, 1000);
}
