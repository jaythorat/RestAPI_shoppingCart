# Importing flask module
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to shopping cart REST API... Please put /cart in the url or /cart/user_id"

# Users Shopping Carts
shopping_cart = [{'user_id': 0, 'user_name': 'user1',
    'cart': [{'product': "Laptop",
        'product_id': '0',
        'price': 'RS.35,000.',
        'description': 'Best laptop if the DECADE'
        },
        {'product': "Phone",
            'product_id': '1',
            'price': 'RS.14,582.',
            'description': 'Best smartphone released till the date...'
            },
        {'product': "Television",
            'product_id': '2',
            'price': 'RS.1,50,000.',
            'description': 'ONe of the best smart TV available in the market...'
            }
        ]
    },
    {'user_id': 1, 'user_name': 'user2',
        'cart': [{'product': "Car",
            'product_id': '0',
            'price': 'RS.3,50,000.',
            'description': 'Type - SUV , Capacity - 5'
            },
            {'product': "Table",
                'product_id': '1',
                'price': 'RS.14,582.',
                'description': 'Dimensions = 18*10*7 , High Quality'
                },
            {'product': "Foot Massager",
                'product_id': '2',
                'price': 'RS.11,000.',
                'description': 'Budget foot massager '
                }
            ]
        }
    ]


# Returning cart of every user
@app.route('/cart', methods=['GET'])
def get():
    return jsonify({'shopping_cart': shopping_cart})


# Returning cart of user by User_name
@app.route('/cart/<string:user_name>', methods=['GET'])
def get_product_by_name(user_name):
    for i in range(len(shopping_cart)):
        if user_name == shopping_cart[i]['user_name']:
            return jsonify({'shopping_cart': shopping_cart[i]['cart']})
        else:
            i += 1
            if i not in range(len(shopping_cart)):
                abort(404, "User Not Found")
            else:
                continue


# Returning Cart content of users by user id
@app.route('/cart/<int:user_id>', methods=['GET'])
def get_product(user_id):
    if user_id < len(shopping_cart):
        return jsonify({'shopping_cart': shopping_cart[user_id]['cart']})
    else:
        abort(404, "User id not found")


# Adding new item to the cart with POST method
@app.route('/cart/<int:user_id>', methods=['POST'])
def add_product(user_id):
    cart = {'product': "Air Conditioner",
            'product_id': '3',
            'price': 'RS.75,000',
            'description': 'Air conditioner to add in a existing cart'
            }
    shopping_cart[user_id]['cart'].append(cart)
    return jsonify({'Product Added': True})


# Updating cart content with PUT method
@app.route('/cart/<int:user_id>', methods=['PUT'])
def cart_update(user_id):
    # Taking input of index number where we want to update given details
    index_to_update = int(input("Enter ID of product to update :"))
    # Updating Details
    shopping_cart[user_id]['cart'][index_to_update]['description'] = "This is updated Description for sample"
    return jsonify({'product': shopping_cart[user_id]['cart'][index_to_update]})


# Deleting cart item of a specific user from user_id
@app.route('/cart/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    id_to_delete = int(input("Enter the product id of product you want to delete :"))
    if id_to_delete in range(len(shopping_cart[user_id]['cart'])):
        del shopping_cart[user_id]['cart'][id_to_delete]
        return jsonify({'Result': True})
    else:
        abort(404, 'Not found')


# Run flask server
if __name__ == "__main__":
    app.run(debug=True)
