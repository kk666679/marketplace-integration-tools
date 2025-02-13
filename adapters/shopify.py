# adapters/shopify.py
import requests

class ShopifyAdapter:
    def __init__(self, vendor):
        self.access_token = vendor.shopify_access_token
        self.shop_name = vendor.shopify_store_name

    def get_products(self):
        url = f"https://{self.shop_name}.myshopify.com/admin/api/2024-01/products.json"
        headers = {"X-Shopify-Access-Token": self.access_token}
        response = requests.get(url, headers=headers)
        return response.json()
