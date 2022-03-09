import shopify
import json
import requests

# Set APIKey, APIPass and Token in config.py
from config import *

# Start the session
shopify.Session.setup(api_key=APIKey, secret=APIPass)
session = shopify.Session(shop_url, api_version, access_token)
shopify.ShopifyResource.activate_session(session)



# Get the Store ID
shop = shopify.Shop.current()

print(shop)

# Get the Products Id
productsId = shopify.Product.find()

print(productsId)


