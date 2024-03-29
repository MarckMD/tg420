import telebot
import os

bot = telebot.TeleBot(os.environ[6328510710:AAGr5F5JllAWPSqLdFTMq9zzqMG0qgxWVfI])

# This dictionary will store the products that are available in the shop
products = {
    'product1': {'name': 'Product 1', 'price': 9.99},
    'product2': {'name': 'Product 2', 'price': 19.99},
    'product3': {'name': 'Product 3', 'price': 29.99},
}

# This dictionary will store the items that users have added to their cart
carts = {}

# This handler will be called when the user sends the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Welcome to the Digital Shop!')

# This handler will be called when the user sends the /catalog command
@bot.message_handler(commands=['catalog'])
def show_catalog(message):
    catalog_text = 'Here is our catalog:\n\n'
    for product_id, product in products.items():
        catalog_text += f'{product_id}: {product["name"]} - ${product["price"]}\n'
    bot.send_message(message.chat.id, catalog_text)

# This handler will be called when the user sends the /add command
@bot.message_handler(commands=['add'])
def add_to_cart(message):
    # Split the message into the command and the product ID
    parts = message.text.split()
    if len(parts) != 2:
        bot.send_message(message.chat.id, 'Invalid command. Use /add [product_id] to add an item to your cart.')
        return
    product_id = parts[1]
    if product_id not in products:
        bot.send_message(message.chat.id, 'Invalid product ID. Use /catalog to see a list of available products.')
        return
    if message.chat.id not in carts:
        carts[message.chat.id] = []
    carts[message.chat.id].append(product_id)
    bot.send_message(message.chat.id, f'{products[product_id]["name"]} added to your cart!')

# This handler will be called when the user sends the /cart command
@bot.message_handler(commands=['cart'])
def show_cart(message):
    if message.chat.id not in carts:
        bot.send_message(message.chat.id, 'Your cart is empty.')
        return
    cart_text = 'Here is what is in your cart:\n\n'
    total_price = 0
    for product_id in carts[message.chat.id]:
        product = products[product_id]
        cart_text += f'{product["name"]} - ${product["price"]}\n'
        total_price += product['price']
    cart_text += f'\nTotal: ${total_price}'
    bot
