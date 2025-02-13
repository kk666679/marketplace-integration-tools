import requests
from sp_api.api import Orders
from sp_api.base import SellingApiException
from woocommerce import API
import time
import json

# Shopify API Configuration
SHOPIFY_STORE = "yourshop.myshopify.com"
SHOPIFY_ACCESS_TOKEN = "your_shopify_access_token"

# Amazon SP-API Configuration
AMAZON_SELLER_ID = "your_seller_id"
AMAZON_ACCESS_KEY = "your_access_key"
AMAZON_SECRET_KEY = "your_secret_key"

# eBay API Configuration
EBAY_APP_ID = "your_ebay_app_id"
EBAY_TOKEN = "your_ebay_oauth_token"

# WooCommerce API Configuration
wcapi = API(
    url="https://yourstore.com",
    consumer_key="your_consumer_key",
    consumer_secret="your_consumer_secret",
    version="wc/v3"
)


# Shopify: Fetch Products
def fetch_shopify_products():
    url = f"https://{SHOPIFY_STORE}/admin/api/2023-10/products.json"
    headers = {"X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN}
    response = requests.get(url, headers=headers)
    return response.json().get("products", [])


# Amazon: Fetch Orders
def fetch_amazon_orders():
    try:
        orders = Orders().get_orders(CreatedAfter="2024-01-01")
        return orders.payload
    except SellingApiException as e:
        print(f"Amazon API Error: {e.error_code}")
        return []


# eBay: Fetch Orders
def fetch_ebay_orders():
    url = "https://api.ebay.com/sell/fulfillment/v1/order"
    headers = {"Authorization": f"Bearer {EBAY_TOKEN}", "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json().get("orders", [])


# WooCommerce: Fetch Products
def fetch_woocommerce_products():
    return wcapi.get("products").json()


# Update eBay Inventory
def update_ebay_stock(product_id, new_stock):
    url = f"https://api.ebay.com/inventory/v1/inventory_item/{product_id}"
    headers = {"Authorization": f"Bearer {EBAY_TOKEN}", "Content-Type": "application/json"}
    data = {"availability": {"pickupAtLocationAvailability": {"
