# Diffie-Hellman Key Exchange
> **University Projects:** Part C of HW2 in CS642-Information Security

In this part of the assignment you will receive a secret code from a secret server.

However, the code is very sensitive and the server does not want any network sniffer to be able to read the code intended for you.

So the server encrypts the message with a **Diffie-Hellman exchanged key** before sending. 

You have to establish a **shared secret key** using DH key exchange protocol using **HTTP messages**.

The APIs the server provides are:

1. `/dh?gx=<gx_str>` which takes one parameter gx. *This is the client-side part of the the DH key (g^x).*

In response, the server will send a *json object* with the following fields:
```
{
  'gy': <gy>,
  'c':  <ciphertext encrypted with the k = SHA256(gxy)
}
```
2. `/verify?code=<code_value> ` which takes a code and returns if the code is valid or not.

To access these APIs:

- Send **HTTP GET requests** to the server at the IP address `128.105.19.18:8080`. 
  - *Note: The server is only available from inside the university CS network*

Insight: In cryptography, "strings" are strings of bytes, and not of ASCII characters. 
For ease of sending them over network, and writing to files, we encode them into base64 format.
In this part of the assignment, all strings are **urlsafe_base64** encoded. 

In Python you can do so using **base64**:

`base64.urlsafe_b64encode(gx)` for *encoding* a bytestring into a base64 string
`base64.urlsafe_b64decode(gx_str)` for *decoding* a base64 string back into a bytestring.

Tasks:

1. For this part of the assignment, you must complete `dh_sol.py` so that it retrieves and decrypts the secret code from the secret server. Starter code is provided for you.

2. In `solutions.txt`, write down the secret code and briefly explain how your solution works.

