from flask import Flask, request
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

private_keys = {
    1:{"p":2,"q":5},
    2:{"p":7,"q":11},
}

def totiente(p,q):
    return (int(p)-1)*(int(q)-1)

def response_private_keys():
    return {"private_keys":list(private_keys.values())}

def encript_for_each_n(message, e, n):
    encripted_message = []
    for c in message:
        e_m = pow(int(c),int(e)) % int(n)
        encripted_message.append(e_m)
    return {"encripted_message":encripted_message}

def modular_exponenciation(e,phi):
    return pow(int(e),-1,int(phi))

def decript(p, q, e, message):
    d = modular_exponenciation(e,totiente(p,q))
    n = int(p)*int(q)
    decripted_message = []
    for num in message:
        m = pow(int(num),int(d),n)
        decripted_message.append(m)
    return {"dencripted_message":decripted_message}

@app.route("/")
def root():
    return '<h1>Hello, Word!</h1>'

@app.route("/private_keys")
def return_private_keys():
   return response_private_keys()

@app.route("/encript/create", methods=["POST"])
def encript_message():
    body = request.json
    return encript_for_each_n(body["message"],body["e"],body["n"])

@app.route("/decript", methods=["POST"])
def dencript_message():
    body = request.json
    return decript(body["p"],body["q"],body["e"], body["message"])

app.run(host='0.0.0.0', port=8000)
