import requests
import statistics

# Insert your eBay App ID here
EBAY_APP_ID = "YOUR_EBAY_APP_ID"
EBAY_ENDPOINT = "https://svcs.ebay.com/services/search/FindingService/v1"

def search_pokemon_cards(max_entries=100):
    params = {
        "OPERATION-NAME": "findItemsByKeywords",
        "SERVICE-VERSION": "1.0.0",
        "SECURITY-APPNAME": EBAY_APP_ID,
        "RESPONSE-DATA-FORMAT": "JSON",
        "REST-PAYLOAD": "",
        "keywords": "pokemon card",
        "paginationInput.entriesPerPage": max_entries,
        "itemFilter(0).name": "ListingType",
        "itemFilter(0).value": "FixedPrice"
    }
    resp = requests.get(EBAY_ENDPOINT, params=params)
    resp.raise_for_status()
    items = resp.json()["findItemsByKeywordsResponse"][0]["searchResult"][0].get("item", [])
    results = []
    for item in items:
        try:
            price = float(item["sellingStatus"][0]["currentPrice"][0]["__value__"])
            url = item["viewItemURL"][0]
            title = item["title"][0]
            results.append((price, url, title))
        except Exception:
            continue
    return results

def median_and_below(results):
    prices = [r[0] for r in results]
    if not prices:
        return None, []
    median_price = statistics.median(prices)
    below = [r for r in results if r[0] < median_price]
    return median_price, below

def main():
    print("Searching eBay for Pokémon cards...")
    results = search_pokemon_cards()
    median_price, below_median = median_and_below(results)
    if median_price is None:
        print("No results found.")
        return
    print(f"Median price: ${median_price:.2f}")
    print(f"Listings below median ({len(below_median)} found):")
    for price, url, title in below_median:
        print(f"${price:.2f}: {title}\n  {url}\n")

if __name__ == "__main__":
    main()