# NGINX-intro
This repository is part of the course https://www.udemy.com/course/nginx-crash-course

## Section 6 - External auth
The idea of this section is to create an external authentication service.

In the auth service we only check if the authorization header is present and if the token is equal to a fixed one, the idea is to check how nginx works, no to create an authentication service

Also, in the configuration we added the cors snippets.

### Configuration explanation

1) Create the `/auth` upstream service 

```conf
    upstream auth {
        server auth:8000;       # External authentication service
    }
```

2) Add the `/auth` location for just internal use

```conf
        location /auth {
            internal;
            proxy_pass http://auth;
            proxy_set_header Content-Length "";
            proxy_pass_request_headers off;
            proxy_pass_request_body off;
            proxy_set_header X-Original-URI $request_uri;
            proxy_set_header Authorization $http_authorization;
            proxy_set_header X-Request-ID $http_x_request_id;
        }

```

Here we set it as internal.

Also here we are preventing to pass all headers comming from the client, instead we are setting `proxy_pass_request_headers off` as well as `proxy_pass_request_body off` to avoid sending all headers. Then we set the required headers with `proxy_set_header`

3) Add the authentication service in the secured route

```conf
            # Delegate JWT validation to auth service
            auth_request /auth;
```