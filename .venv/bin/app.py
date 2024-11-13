from flask import Flask, request, render_template

app = Flask(__name__)

'''
/login [GET, POST]
/register [GET, POST]
/logout [GET ? POST ?? DELETE]

/profile (/user, /me) [GET, PUT(PATCH), DELETE]
      ?  /favouties [GET, POST, DELETE, PATCH]
      ??  /favouties/<favourite_id> [DELETE]
      ?  /search_history [GET, DELETE]

/items [GET, POST]
/items/<item_id> [GET, DELETE]
/leasers [GET]
/leasers/<leaser_id> [GET]

/contracts [GET, POST]
/contracts/<contract_id> [GET, PATCH/PUT]

/search [GET, (POST)]

/complain [POST]
/compare [GET, PUT/PATCH]
'''

@app.route('/')

def hello_world():
    return "Hello World!"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        return 'POST'
    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        return 'POST'
    
@app.route('/logout', methods=['GET','POST','DELETE'])
def logout():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    if request.method == 'DELETE':
        return 'DELETE'
   
@app.route('/items', methods =['GET','POST'])
def items():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'DELETE':
        return 'DELETE'

@app.route('/items/<item_id>', methods=['GET', 'DELETE'])
def item_details(item_id):
    if request.method == 'GET':
        return f'GET {item_id}'
    if request.method == 'DELETE':
        return f'DELETE {item_id}'
    
@app.route('/leasers', methods=['GET'])
def leasers():   
    if request.method == 'GET':
        return 'GET'

@app.route('/leasers/<leaser_id>', methods= ['GET'])
def leaser_info(leaser_id):
    if request.method == 'GET':
        return f'GET {leaser_id}'

@app.route('/contracts', methods = ['GET', 'POST'])
def contracts():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    
@app.route('/contracts/<contract_id>', methods = ['GET', 'PATCH/PUT'])
def contracts_details(contract_id):
    if request.method == 'GET':
        return f'GET {contract_id}'
    if request.method == 'PATCH/PUT':
        return f'PATCH/PUT {contract_id}'
    
@app.route('/search', methods = ['GET', 'POST'])
def search():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    
@app.route('/complain', methods = ['POST'])
def complain():
    if request.method == 'POST':
        return 'POST'
    
@app.route('/compare', methods = ['GET', 'PUT'])
def compare(item_id,item_id2):
    if request.method == 'GET':
        return f'GET {item_id,item_id2}'
    if request.method == 'PUT':
        return f'PUT {item_id,item_id2}'

if __name__ == '__main__':
    app.run()
