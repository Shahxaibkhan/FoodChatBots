import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    intent = data['queryResult']['intent']['displayName']

    if intent == "Menu Intent":
        response = {"fulfillmentText": "Here is our menu: Veggie Pizza, Grilled Salmon, etc."}
    elif intent == "Deals Intent":
        response = {"fulfillmentText": "Today's deals: 20% off on pizzas!"}
    else:
        response = {"fulfillmentText": "Sorry, I didn't understand that."}
    
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT variable provided by Railway
    app.run(host="0.0.0.0", port=port, debug=False)  # Disable debug mode in production
