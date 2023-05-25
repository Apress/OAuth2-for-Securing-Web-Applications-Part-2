# Apress Source Code

This repository accompanies [*OAuth2 for Securing Web Applications: Part 2: OpenID Connect and Keycloak*] by Matthew Baker (Apress, 2023).


Download the files as a zip using the green button, or clone the repository to your machine using Git.

## Releases

Release v1.0 corresponds to the code in the published video course, without corrections or updates.

## Contributions

See the file Contributing.md for more information on how you can contribute to this repository.

## Prerequisites

You will need Python installed to follow these exercises, though no knowledge of Python is needed.

## Instructions for the Authorization Code Flow with Keycloak example

### Start the server

The directory "server" contains a Flask application with two endpoints that are used
in the Authorization Code Flow Keycloak example. To run it on Mac or Linux, enter the following in a command line terminal:

```
cd server
virtualenv venv
source venv/bin/activate
pip -r requirements.txt
flask run -p 5000
```
of if port 5000 is not available, choose a port which is.

On Windows, replace `source venv/bin/activate` with `venv\scripts\activate`

### URLs for the exercise

1. Get an authorization code.  Enter this in a browser:

   ```
   http://localhost:8080/realms/myrealm/protocol/openid-connect/auth?client_id=myclient&response_type=code&state=myrandomstate&scope=api&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcb
   ```

2. Get the access token.  Send a POST request to

   ```
   http://localhost:8080/realms/myrealm/protocol/openid-connect/token
   ```

   with the following parameters:

   |Name             |Value                       |
   |-----------------|----------------------------|
   |``grant-type``   |``authorization_code``      |
   |``CODE``         |*YOURAUTHORIZATIONCODE*     |
   |``redirect_uri`` |``http://127.0.0.1:5000/cb``|
   |``client_id``    |``myclient``                |
   |``client_secret``|*YOURCLIENTSECRET*          |

   substitute the authorization code from ste 1 for *YOURAUTHORIZATIONCODE*.  Substitute your Client Secret from the Keycloak Client Credentials tab for *YOURCLIENTSECRET*

   If you're using curl, the command will be

   ```
   curl http://localhost:8080/realms/myrealm/protocol/openid-connect/token -X POST -d grant_type=authorization_code -d code=YOURAUTHORIZATIONCODE -d redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcb -d client_id=myclient -d client_secret=YOURCLIENTSECRET
   ```

3. URL for getting RSA public key.  You can do this in a browser or curl.

   ```
   http://localhost:8080/realms/myrealm
   ```

   When pasting your key into jwt.io, remember to insert it between these marks:

   ```
   -----BEGIN RSA PUBLIC KEY-----
   YOUR KEY
   -----END RSA PUBLIC KEY-----
   ```

4. Accessing a resource.  Enter the following using curl (or the Postman equivalent):

   ```
   curl -H "Authorization: Bearer YOURACCECSSTOKEN" http://127.0.0.1:5000/myresource
   ```

## Instructions for the OIDC Authorization Code Flow with Keycloak example

1. Get an authorization code.  Enter this in a browser:

   ```
   http://localhost:8080/realms/myrealm/protocol/openid-connect/auth?client_id=myclient&response_type=code&state=myrandomstate&scope=openid+api&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcb
   ```

2. Get the access token.  Send a POST request to

   ```
   http://localhost:8080/realms/myrealm/protocol/openid-connect/token
   ```

   with the following parameters:

   |Name             |Value                       |
   |-----------------|----------------------------|
   |``grant-type``   |``authorization_code``      |
   |``CODE``         |*YOURAUTHORIZATIONCODE*     |
   |``redirect_uri`` |``http://127.0.0.1:5000/cb``|
   |``client_id``    |``myclient``                |
   |``client_secret``|*YOURCLIENTSECRET*          |

   substitute the authorization code from ste 1 for *YOURAUTHORIZATIONCODE*.  Substitute your Client Secret from the Keycloak Client Credentials tab for *YOURCLIENTSECRET*

   If you're using curl, the command will be

   ```
   curl http://localhost:8080/realms/myrealm/protocol/openid-connect/token -X POST -d grant_type=authorization_code -d code=YOURAUTHORIZATIONCODE -d redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcb -d client_id=myclient -d client_secret=YOURCLIENTSECRET
   ```

## Instructions for the JavaScript client example

### Start the development web server 

A JavaScript Keyclock client is in the "client" directory.  To start it,

```
cd server
virtualenv venv
source venv/bin/activate
python -m http.server
```

The serer runs on port 8000 by default.  To run the client. visit the following URL in a web browser:

```
http://localhost:8000
```



