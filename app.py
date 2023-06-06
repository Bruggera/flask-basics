from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 10
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    requested_data = request.get_json()
    new_store = {"name": requested_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    requested_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": requested_data["name"], "price": requested_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404
     

@app.route('/')
def index():
    return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'