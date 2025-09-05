# eBay Pokémon Card Scanner

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/clellandblair-ui/Pokemon-flips.git
   cd Pokemon-flips
   ```

2. **Install Dependencies**:
   - Ensure you have Python 3 installed.
   - Install the required Python package:
     ```bash
     pip install requests
     ```

3. **Input eBay API Credentials**:
   - Open `scan_ebay.py` and replace `'YourAppID'` with your actual eBay App ID in the `SECURITY-APPNAME` field.

4. **Add Top Pokémon List**:
   - Ensure `top_200_pokemon.txt` is present in your repo (see below).

## How It Works
This script scans eBay for Pokémon cards among the top 200 Pokémon. If it finds cards listed below the median price, it prints an alert to your console.

## Customizing Median Prices
Edit the `median_prices` dictionary in `scan_ebay.py` to update median prices for the Pokémon you care about.

## Running the Application
To run:
```bash
python scan_ebay.py
```

---

*You may extend this script for notifications, logging, or integrating external sources for median prices in the future!*