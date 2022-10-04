from ast import Import
from crypt import methods
from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]

# POST - Used to recieve data
# GET - Used to send data back only

# POST /store data : {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route ('/store/<string:name>', methods= ['GET']) #localhost:5000/store/anyname
def get_store(name):
    return name

# GET /store
@app.route('/store')
def get_stores():
    pass

# POST /store/<string:name>/item {name: price}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass