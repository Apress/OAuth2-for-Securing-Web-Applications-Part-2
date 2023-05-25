# URLs for OpenID Connect Flows

## OIDC Authorization Code Flow with and without PKCE

Client to Authorization Server:
```
GET http://auth-server.com/authorize?response_type=code&client_id=<CLIENT_ID>&redirect_uri=<REDIRECT_URI>&scope=openid&state=<HASHED_CHALLENGE>
```

For PKCE, add
```
code_challenge=<RANDOM_STRING>&code_challenge_method=<METHOD>
```
Example `<METHOD>` is `S256`

Authorization Server to Client:
```
GET https://<REDIRECT_URI>?code=<AUTH_CODE>&state=<STATE>
```

Client to Authorization Server:
```
POST https://auth-server.com/token

  grant_type=authorization_code
  &code=<AUTH_CODE>
  &redirect_uri=<REDIRECT_URI>
  &client_id=<CLIENT_ID>
  &client_secret=<CLIENT_SECRET>
```

For PKCE, add
```
code_verifier=<UNHASHED_CHALLENGE>
```

Authorzation Server to Client:

```
{
    "access_token": "<ACCESS_TOKEN>", 
    "refresh_token": "<REFRESH_TOKEN>",  
    "token_type": "Bearer", 
    "expires_in": <SECONDS>, 
    "id_token": "<ID_TOKEN>"
}
```

Client to Resource Server:

```
GET https://res-server.com/resource

  Authorization: Bearer <ACCESS_TOKEN>
```

## OIDC Hybrid Flow

Client to Authorization Server:
```
GET http://auth-server.com/authorize?response_type=token+id_token
&client_id=<CLIENT_ID>&redirect_uri=<REDIRECT_URI>&scope=openid
&state=<RANDOM_STRING>&nonce=<NONCE>
```

Authorization Server to Client:
```
GET https://<REDIRECT_URI>#access_token=<ACCESS_TOKEN>&state=<STATE>&id_token=<ID_TOKEN>&token_type=Bearer&expires_in=<SECONDS>
```

Client to Resource Server:
```
GET https://res-server.com/resource 

  Authorization: Bearer <ACCESS_TOKEN>
```

## Hybrid Flow

Client to Authorization Server:
```
GET http://auth-server.com/authorize?response_type=code+id_token
&client_id=<CLIENT_ID>&redirect_uri=<REDIRECT_URI>&scope=openid
&state=<RANDOM_STRING>&nonce=<NONCE>
```

Resource Server to Client:
```
GET https://<REDIRECT_URI>#code=<AUTHORIZATION_CODE>&state=<STATE>&id_token=<ID_TOKEN>&token_type=Bearer&expires_in=<SECONDS>
```

Client to Resource Server:
```
POST https://auth-server.com/token

  grant_type=authorization_code
  &code=<AUTH_CODE>
  &redirect_uri=<REDIRECT_URI>
  &client_id=<CLIENT_ID>
  &client_secret=<CLIENT_SECRET>
```

Resource Server to Client:
```
{
    "access_token": "<ACCESS_TOKEN>", 
    "refresh_token": "<REFRESH_TOKEN>",
    "token_type": "Bearer", 
    "expires_in": <SECONDS>,
    "id_token": "<ID_TOKEN>"
}
```

