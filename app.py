from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# @app.route('/')

# def home():
#   return 'Hello world!!'

stores = [
  {
    'name': 'Nathphoenix stores',
    'items':[
      {
        'name': 'My items',
        'price': '20.00'
      }
    ]
  }
]

@app.route('/')
def home():
    return render_template('index.html')

#store url
#get store
#http://127.0.0.1/store
@app.route('/store')  
def get_stores():
  return jsonify({"stores": stores})
                #KEY      STORE NAME

#creating endpoint
#post store data {name}
@app.route('/store', methods=["POST"])
def create_store():
  request_data = request.get_json()   #this function get all daa and present on the browser
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store)

#create items in store
#post store
@app.route('/store/<string:name>/item', methods=["POST"])
def create_item(name):
  request_data = request.get_json()
  for shop in stores:
    # we define request_data here
      
      if shop['name'] == name:
        # create_new_item
        new_item = {
          'name': request_data['name'],
          'price': request_data['price'],
        }
        shop['items'].append(new_item)
        return jsonify(new_item)   #or return jsonify(shop)
    #  else:
    #     return jsonify({ "message": "Records not found"})
  return jsonify({ "message": "Items not found"})


#get store data {name}
@app.route('/store/<string:name>')  #http://127.0.0.1/store/some_name
def get_store(name):
  #iterate over store, if the store name matches return the store
  #if not reyurn an error message
  for shop in stores:
     if shop['name'] == name:
        return jsonify(stores)
    #  else:
    #     return jsonify({ "message": "Records not found"})
  return jsonify({ "message": "Records not found"})


#get all items in store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for shop in stores:
      if shop['name'] == name:
         return jsonify({"items": shop["items"]})
    #  else:
    #     return jsonify({ "message": "Records not found"})
    return jsonify({ "message": "Items not found"})

app.run(port=5000)