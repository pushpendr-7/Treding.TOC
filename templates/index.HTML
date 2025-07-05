<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Stocks & Crypto Tracker</title>
    <style>
        :root {
            --primary-color: #4361ee;
            --green: #2ecc71;
            --red: #e74c3c;
            --text-color: #2c3e50;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --border-radius: 12px;
            --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 15px;
            background: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        .container {
            max-width: 100%;
            background: var(--card-bg);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px;
            margin-bottom: 20px;
        }

        h2 {
            color: var(--primary-color);
            font-size: 1.3rem;
            margin-top: 0;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 1px solid #eee;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .stock, .crypto {
            margin-bottom: 20px;
        }

        .ticker {
            font-weight: 600;
            color: var(--primary-color);
            font-size: 0.95rem;
        }

        .price {
            font-weight: 700;
            font-size: 1rem;
        }

        .up {
            color: var(--green);
        }

        .down {
            color: var(--red);
        }

        .volume {
            font-size: 0.8rem;
            color: #7f8c8d;
            margin-top: 2px;
        }

        .data-item {
            padding: 10px 0;
            border-bottom: 1px dashed #ecf0f1;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 8px;
        }

        .data-item:last-child {
            border-bottom: none;
        }

        .change-percent {
            font-size: 0.85rem;
            padding: 2px 6px;
            border-radius: 4px;
            background-color: rgba(46, 204, 113, 0.1);
        }

        .down .change-percent {
            background-color: rgba(231, 76, 60, 0.1);
        }

        @media (max-width: 600px) {
            body {
                padding: 10px;
            }
            
            .container {
                padding: 15px;
            }
            
            h2 {
                font-size: 1.1rem;
            }
            
            .price {
                font-size: 0.9rem;
            }
        }

        /* Loading animation */
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }

        #stocks.loading, #crypto.loading {
            animation: pulse 1.5s infinite;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>📊 Live Stock Prices (NSE/BSE) os.  </h2>
        <div id="stocks" class="stock loading">
            Loading stock data...
        </div>

        <h2>₿ Top 10 Cryptocurrencies</h2>
        <div id="crypto" class="crypto loading">
            Loading crypto data...
        </div>
    </div>

    <script>
        // Fetch Stock Data (Using Alpha Vantage API)
        async function fetchStocks() {
            const stocksElement = document.getElementById('stocks');
            stocksElement.classList.remove('loading');
            
            const symbols = ['RELIANCE.BSE', 'TCS.BSE', 'HDFCBANK.BSE', 'INFY.BSE', 'SBIN.BSE'];
            let html = '';
            
            for (const symbol of symbols) {
                try {
                    const response = await fetch(`https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=6AFY4VTCLQ050BBM`);
                    const data = await response.json();
                    const stock = data['Global Quote'];
                    
                    if (stock) {
                        const changePercent = parseFloat(stock['10. change percent'].replace('%', ''));
                        html += `
                            <div class="data-item">
                                <span class="ticker">${symbol.split('.')[0]}</span>
                                <span class="price ${changePercent >= 0 ? 'up' : 'down'}">₹${stock['05. price']}</span>
                                <span class="${changePercent >= 0 ? 'up' : 'down'} change-percent">${changePercent >= 0 ? '+' : ''}${changePercent}%</span>
                                <div class="volume">Volume: ${stock['06. volume']}</div>
                            </div>
                        `;
                    }
                } catch (error) {
                    console.error("Error fetching stock:", error);
                    html += `<div class="data-item">${symbol.split('.')[0]}: Data Error</div>`;
                }
            }
            
            stocksElement.innerHTML = html || "<div class='data-item'>Failed to load stocks. Try later.</div>";
        }

        // Fetch Crypto Data (Using CoinGecko API)
        async function fetchCrypto() {
            const cryptoElement = document.getElementById('crypto');
            cryptoElement.classList.remove('loading');
            
            try {
                const response = await fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10');
                const coins = await response.json();
                let html = '';
                
                coins.forEach(coin => {
                    const change = coin.price_change_percentage_24h;
                    html += `
                        <div class="data-item">
                            <span class="ticker">${coin.symbol.toUpperCase()}</span>
                            <span class="price ${change >= 0 ? 'up' : 'down'}">$${coin.current_price.toLocaleString()}</span>
                            <span class="${change >= 0 ? 'up' : 'down'} change-percent">${change >= 0 ? '+' : ''}${change.toFixed(2)}%</span>
                            <div class="volume">Vol: $${coin.total_volume.toLocaleString()}</div>
                        </div>
                    `;
                });
                
                cryptoElement.innerHTML = html;
            } catch (error) {
                cryptoElement.innerHTML = "<div class='data-item'>Failed to load crypto. Try later.</div>";
            }
        }

        // Initial fetch
        fetchStocks();
        fetchCrypto();
        
        // Refresh every 5 seconds (5000ms)
        setInterval(fetchStocks, 5000);
        setInterval(fetchCrypto, 5000);
    </script>
</body>
</html>

<!--<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Stocks & Crypto Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 10px;
            background: #f5f5f5;
        }
        .container {
            max-width: 100%;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 10px;
        }
        h2 {
            color: #333;
            font-size: 16px;
            margin-top: 0;
        }
        .stock, .crypto {
            margin-bottom: 15px;
        }
        .ticker {
            font-weight: bold;
            color: #1a73e8;
        }
        .price {
            font-weight: bold;
        }
        .up {
            color: green;
        }
        .down {
            color: red;
        }
        .volume {
            font-size: 12px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>📊 Live Stock Prices (NSE/BSE)</h2>
        <div id="stocks" class="stock">
            Loading...
        </div>

        <h2>₿ Top 10 Cryptocurrencies</h2>
        <div id="crypto" class="crypto">
            Loading...
        </div>
    </div>

    <script>
        // Fetch Stock Data (Using Alpha Vantage API)
        async function fetchStocks() {
            const symbols = ['RELIANCE.BSE', 'TCS.BSE', 'HDFCBANK.BSE', 'INFY.BSE', 'SBIN.BSE'];
            let html = '';
            
            for (const symbol of symbols) {
                try {
                    const response = await fetch(`https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=6AFY4VTCLQ050BBM`);
                    const data = await response.json();
                    const stock = data['Global Quote'];
                    
                    if (stock) {
                        const changePercent = parseFloat(stock['10. change percent'].replace('%', ''));
                        html += `
                            <div>
                                <span class="ticker">${symbol.split('.')[0]}</span>: 
                                <span class="price ${changePercent >= 0 ? 'up' : 'down'}">₹${stock['05. price']}</span>
                                <span class="${changePercent >= 0 ? 'up' : 'down'}">(${changePercent}%)</span>
                                <div class="volume">Volume: ${stock['06. volume']}</div>
                            </div>
                        `;
                    }
                } catch (error) {
                    console.error("Error fetching stock:", error);
                    html += `<div>${symbol.split('.')[0]}: Data Error</div>`;
                }
            }
            
            document.getElementById('stocks').innerHTML = html || "Failed to load stocks. Try later.";
        }

        // Fetch Crypto Data (Using CoinGecko API)
        async function fetchCrypto() {
            try {
                const response = await fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10');
                const coins = await response.json();
                let html = '';
                
                coins.forEach(coin => {
                    const change = coin.price_change_percentage_24h;
                    html += `
                        <div>
                            <span class="ticker">${coin.symbol.toUpperCase()}</span>: 
                            <span class="price ${change >= 0 ? 'up' : 'down'}">$${coin.current_price.toLocaleString()}</span>
                            <span class="${change >= 0 ? 'up' : 'down'}">(${change.toFixed(2)}%)</span>
                            <div class="volume">Vol: $${coin.total_volume.toLocaleString()}</div>
                        </div>
                    `;
                });
                
                document.getElementById('crypto').innerHTML = html;
            } catch (error) {
                document.getElementById('crypto').innerHTML = "Failed to load crypto. Try later.";
            }
        }

        // Fetch data on page load and every 60 seconds
        fetchStocks();
        fetchCrypto();
        setInterval(fetchStocks, 60000);
        setInterval(fetchCrypto, 60000);
    </script>
</body>
</html>-->