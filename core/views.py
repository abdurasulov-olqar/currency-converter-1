from core import app
from flask import request, jsonify

usd = 11380.7 # 1 USD = 11380.7 UZS

@app.route('/api/to-usd', methods=['GET','POST'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    data=request.args.get("amount",0)
    
    return jsonify({"amount": data,
                    "currency": "UZS",
                    "converted": int(data)/usd,
                    "convertedCurrency": "USD"})

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    data = request.args["amount"]
    
    return jsonify({"amount": data,
                    "currency": "USD",
                    "converted": int(data)*usd,
                    "convertedCurrency": "UZS"})
    