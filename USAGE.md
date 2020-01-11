## Setup
Import the `Requester` class from the module. `presets` is optional, you only need them if you use the preset functions mentioned later.
```py
from connectbox import Requester, presets
```

```py
# IP address of your router
ip = "192.168.1.1"

# Password of your router
key = "12345678"
```

If you call a request without a valid sessionID, you will get a **302** status code, and no valid answer (login also fails if you use it as first request).

Because of this, you must make a request before doing anything else,
and use its returned sessionID to make valid request (this is already handled by the library) The function you call can be anything, it doesn't matter.
```py
r = Requester(ip)
r.get(1)
```

## Login
You can only use `getter` functions `1` and `3` without authentication.

You might also be able to use some `setter` functions
but I haven't tested them.

The default and the preset functions have a return value `Request` (except `login()`, which returns a `LoginRequest`), containing a status code and the returned text. 

```py
req = r.set(15, {
    # username is always admin
    "Username": "admin",
    "Password": key
})

{'status_code': 200, 'text': 'successful;SID=3250237944'}
```

There are also some preset wrapper functions:

`LoginRequest` is similar to `Request`, except that it has a `success` property, too.

```py
req = r.login(key)

{'status_code': 200, 'success': True, 'text': 'successful;SID=564378752'}
```

## Actual code...

You can find a list of all the available functions in `functions.txt`

```py
# get router status
req = r.get(5)
print(req.text)

# change language
r.changeLang("en")
# or
r.set(4, {"lang": "en"})
```

## Logout
Make sure to log out in the end since the router only allows one user to be authenticated at a time.
```py
r.logout()
# or
r.set(16)
```