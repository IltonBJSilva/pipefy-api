import requests
from flask import Flask, jsonify
from tkhash import hashsecret
from piptoken import piptoken

# Exemplo de uso
main = Flask(__name__)

url = "https://api.pipefy.com/graphql"

#payload = { "query": "{ me { id email } }" }


#payload = { "query": "{    phase(id: 323248106){     name   } }" }

payload = { "query": "{   phase(id: 323248106){     cards{       nodes{         title       }     }   } }" }



headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer "+piptoken
}

response = requests.post(url, json=payload, headers=headers)

@main.route("/email", methods=["GET"])
def return_respo():
    return jsonify(response.text)



main.run(port=5000, host='localhost', debug=True)
