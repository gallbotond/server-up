This is a [simple website](https://gallbotond.github.io/server-up/) to check if a server is up by being hosted from the said machine. 
It uses **https** and a **self-signed certificate**. The multithreaded server is written in Python.

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
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -config ./openssl.cnf
```

4. Start the https server with `server-up.py`

```
python3 server-up.py
```

## Extras 

It will display basic information about the client's browser and operating system.  

![on google chrome](https://github.com/user-attachments/assets/cb52a2fa-5566-4ab2-991e-c3ecf4b088a4)

If it doesn't, it means the browser is privacy respecting, and blocked the requests.

![on librewolf (based on firefox)](https://github.com/user-attachments/assets/64f25ebd-f2eb-4e10-bf26-adc1a35fd7ea)

