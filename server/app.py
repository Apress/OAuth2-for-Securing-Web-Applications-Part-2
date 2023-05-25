from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
import jwt
import logging

public_key = b'''
-----BEGIN RSA PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2MxMJvhdansw5xdIYKEZwqv6/VIMTW2trfOM20itaj22yGQtV+Gjg8ZtGp2UnI+gu5i5rjx7fNoWeZGWLI0SBJdPsjlzDYsn0c7Yj18k9olbI41v8YZyrNymoT4t3IzMSFh3ndY845E3njK/uMtfXKNRgw+MDk5RMeO0OwzYDwrycaFE/cucKxQOvHEq3UuDgub1ZipCfTfY1RVNiij8eJRo1DJ3JXaI45hrdxEFI60Z91cYPzjmWx1kDLpB596GewCz3jbRI3Amj0o2Netqq65mQSha0Gw1c+MsvPBi4hp04Tu/Lt9LJCkuRRlh/1YMhTLD4GqwrFvoTxz8MCqMuwIDAQAB
-----END RSA PUBLIC KEY-----'''

logging.getLogger('flask_cors').level = logging.DEBUG

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/cb', methods=['GET'])
def cb():
    html = '''
    <html>
        <head><title>OAuth2 Callback</title></head>
        <body>
            <h1>OAuth2 Request URI Callback</h1>

            <p>This has been called from the OAuth2 Authorization Server in order to return
            the authorization code to the Client application.
            </p>
            <p>The authorization code is:
            <pre>
            %s
            </pre>
            </p>
        </body>
    </html>
    ''' % format(request.args['code'])
    return Response(html, mimetype='text/html')

@app.route('/myresource', methods=['GET'])
def myresource():
    auth = request.headers.get('Authorization')
    print(auth)
    try:
        (token_type, access_token) = auth.split(" ")
        access_token_json = jwt.decode(access_token, public_key, algorithms = ['RS256'], 
                                       audience="account")
    except Exception as e:
        print(e)
        return Response('403 Forbidden', status=403)
    return Response('{"message": "It worked!"}', mimetype='application/json')

