# 1.Rest API Assignment: CRUD Operations Handling 
## 

## About

This Rest API assignment is made using Python and flask.
This API handles GET, DELETE, PUT, and POST requests from the user and sends responses to them.


 
## Working & Instrcutions

When you'll run the code basic server will run on: `http://127.0.0.1:5000`\

### For GET  operation:
When you'll add `/cart` to the URL it will show shopping carts of all the available users and their cart content. Further to get cart details of any specific user you have 2 ways either by `/user_id` or `/user_name`.\
For e.g. `http://1227.0.0.1/cart/1`\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`http://1227.0.0.1/cart/user1`

### For PUT & DELETE operation:
Make sure you've installed all the dependencies manually or by requirements.txt 

TO execute PUT/DELETE operation run the following command in your CMD    `curl -i -H "Content-Type:Application/json -X <put/delete> HTTP://127.0.0.1:5000/cart/user_id`\
After executing the command, the code asks you an `input` to update or delete the specific item details present in the cart.

### For POST operation:
Make sure you've installed all the dependencies manually or by requirements.txt

To execute the operation run `curl -i -H "Content-Type:Application/json -X POST HTTP://127.0.0.1:5000/cart/user_id` in your CMD \

And you'll notice an extra item in the defined user cart from the `add_product` function

## Dependencies

This project uses the following dependencies in Python (install using `pip`):

* `flask`
* `curl`

## Installation

1. Install `Python` (Any 3.x.x version)
2. Install `flask`
3. Install `curl` 
	
## Error Handling:
The server will return error 404 if it is unable to locate specified `user_id`, `user_name`, or `item_to_delete in DELETE operation`

#

# 2. Critical API Suggestions:

* Live classes > Upcoming classes take more time to show results...
* In RECIPES: when you click on the `FIND MY DISH ` button 3/5 times it gave me an internet connectivity error(Check Provided Screenshot in GITHUB repo)... only 2/5 times gave me results I wanted

* In general any search query is talking longer to respond than usual.

