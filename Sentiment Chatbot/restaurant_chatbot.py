from textblob import TextBlob

intents = {
        "menu": {
        "keywords": ["menu", "food", "dishes", "items"],
        "response": "Here's a quick look at our menu:\n\n🍽️ *Starters:*\n- Garlic Bread – ₹99\n- Crispy Chicken Wings – ₹199\n- Veg Spring Rolls – ₹149\n\n🍛 *Main Course:*\n- Butter Chicken with Naan – ₹349\n- Paneer Tikka Masala – ₹299\n- Spaghetti Aglio e Olio – ₹279\n\n🍔 *Burgers & Sandwiches:*\n- Classic Chicken Burger – ₹199\n- Veg Club Sandwich – ₹179\n\n🍰 *Desserts:*\n- Chocolate Brownie with Ice Cream – ₹149\n- Gulab Jamun – ₹99\n\n🥤 *Beverages:*\n- Masala Lemonade – ₹69\n- Cold Coffee – ₹99\n- Fresh Lime Soda – ₹59"
    },
    "hours":{
        "keywords":["hours","open","close"],
        "response":"We are open from 9 AM to 5 PM, Monday through Friday."
    },
    "return":{
        "keywords":["refund","money_back","return"],
        "response":"I'd be happy to help you with a return. Let me transfer you to our customer service team."
    },
    "reservation": {
        "keywords": ["reserve", "booking", "reservation", "table"],
        "response": "Sure! You can make a reservation by calling us or booking online here: [Insert Reservation Link]."
    },
    "location": {
        "keywords": ["location", "address", "where"],
        "response": "We’re located at 123 Foodie Street, Flavor Town. Come visit us!"
    },
    "delivery": {
        "keywords": ["delivery", "deliver", "order online"],
        "response": "Yes, we offer delivery through Zomato, Swiggy, and our own app: [Insert Link]."
    },
    "takeout": {
        "keywords": ["takeout", "pickup", "carryout"],
        "response": "Absolutely! You can place a takeout order online or call us directly."
    },
    "vegan_options": {
        "keywords": ["vegan", "vegetarian", "plant-based"],
        "response": "Yes, we have a variety of vegan and vegetarian options available. Just ask your server!"
    },
    "allergies": {
        "keywords": ["allergy", "allergies", "gluten-free", "nut-free"],
        "response": "We take food allergies seriously. Please let our staff know and we'll guide you through safe choices."
    },
    "catering": {
        "keywords": ["cater", "catering", "event", "party"],
        "response": "Yes, we offer catering services for events and parties. Contact us here: [Insert Contact Link]."
    },
    "wifi": {
        "keywords": ["wifi", "internet", "wi-fi"],
        "response": "Yes, we offer free Wi-Fi to all our guests. Ask your server for the password."
    },
    "specials": {
        "keywords": ["specials", "offers", "deals", "discounts"],
        "response": "Check out our daily specials and offers here: [Insert Offers Link]!"
    },
    "feedback": {
        "keywords": ["feedback", "complaint", "suggestion", "review"],
        "response": "We’d love to hear your feedback! Please fill out our feedback form here: [Insert Feedback Link]."
    },
    "return": {
        "keywords": ["refund", "money_back", "return"],
        "response": "If there's an issue with your order, please contact our manager or customer care here: [Insert Contact Info]."
    },
    "greeting": {
        "keywords": ["hi", "hello", "hey", "greetings"],
        "response": "Hello! How can I assist you today?"
    }
}

def get_response(message):
    message = message.lower()
    for intent in intents.values():
        if any(word in message for word in intent["keywords"]):
            return intent["response"]
        sentiment = TextBlob(message).sentiment.polarity
    if sentiment > 0:
        return "That's so great to hear!"
    elif sentiment < 0:
        return "I'm sorry to hear that."
    else:
        return "I see. Can you tell me more about it?"
    
def chat():
    print("Welcome to the chatbot! Type 'exit' to end the chat.")
    while (user_input := input("You: ").strip().lower()) not in ["exit","quit","bye"]:
        response = get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()