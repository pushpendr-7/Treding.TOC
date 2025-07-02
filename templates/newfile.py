<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Live Stock Trend Checker</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-white font-sans p-6">
  <div class="max-w-xl mx-auto">
    <h1 class="text-3xl font-bold text-center mb-6">📈 Stock Trend Detector (India)</h1>

    <div class="bg-gray-800 p-4 rounded-2xl shadow-md">
      <label class="block mb-2">Enter Stock Symbol (like RELIANCE.BSE or INFY.NSE):</label>
      <input id="symbol" class="w-full p-2 rounded bg-gray-700 text-white mb-4" placeholder="Example: TCS.BSE" />

      <button onclick="fetchStock()" class="bg-blue-600 px-4 py-2 rounded hover:bg-blue-700">🔍 Check Trend</button>

      <div id="result" class="mt-6 text-lg"></div>
    </div>
  </div>

  <script>
    async function fetchStock() {
      const symbol = document.getElementById('symbol').value.trim();
      const apiKey = "2I0V5VZB35SNU33G"; // ✅ Your personal Alpha Vantage API Key
      const url = `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=${symbol}&apikey=${apiKey}`;

      const resultBox = document.getElementById("result");
      resultBox.innerHTML = "⏳ Fetching data...";

      try {
        const res = await fetch(url);
        const data = await res.json();

        if (!data["Time Series (Daily)"]) {
          resultBox.innerHTML = "❌ Symbol not found or API limit exceeded. Try again later.";
          return;
        }

        const series = data["Time Series (Daily)"];
        const dates = Object.keys(series);
        const today = series[dates[0]];
        const yesterday = series[dates[1]];

        const closeToday = parseFloat(today["4. close"]);
        const closeYesterday = parseFloat(yesterday["4. close"]);
        const change = closeToday - closeYesterday;
        const percentChange = ((change / closeYesterday) * 100).toFixed(2);

        let trend = change > 0 ? "📈 Uptrend" : "📉 Downtrend";
        let reason = Math.abs(change) >= 1.5 ? "🔍 Strong move — possibly news or volume spike" : "📊 Regular daily fluctuation";

        resultBox.innerHTML = `
          <p><strong>📦 Symbol:</strong> ${symbol}</p>
          <p><strong>📅 Date:</strong> ${dates[0]}</p>
          <p><strong>💰 Current Close:</strong> ₹${closeToday}</p>
          <p><strong>📉 Previous Close:</strong> ₹${closeYesterday}</p>
          <p><strong>📊 Change:</strong> ₹${change.toFixed(2)} (${percentChange}%)</p>
          <p><strong>📡 Trend:</strong> ${trend}</p>
          <p><strong>🧠 Reason:</strong> ${reason}</p>
        `;
      } catch (error) {
        resultBox.innerHTML = "❌ Error: Unable to fetch data.";
      }
    }
  </script>
</body>
</html>
