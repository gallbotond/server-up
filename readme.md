This is a simple website to check if a server is up.

## How to use

1. Clone the repository

```
git clone https://github.com/gallbotond/server-up.git
```

2. At the root of the project create a `/secrets` folder, and open it

```
mkdir secrets
cd secrets
```

3. Create and edit the `openssl.cnf` with your own data

```
[req]
distinguished_name = req_distinguished_name
x509_extensions = v3_req
prompt = no

[req_distinguished_name]
C = US
ST = California
L = San Francisco
O = My Company
OU = My Department
CN = localhost

[v3_req]
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
```

3. Before running the server, generate an **SSL certificate** and a **private key**

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -config ../openssl.cnf
```

4. Start the https server with `server-up.py`

```
python3 server-up.py
```
