import http.server
import ssl
from socketserver import ThreadingMixIn

class ThreadingSimpleServer(ThreadingMixIn, http.server.HTTPServer):
    pass

# Define the server address and port
server_address = ('localhost', 4443)

# Use the SimpleHTTPRequestHandler, which serves files from the current directory
handler = http.server.SimpleHTTPRequestHandler

# Set up the server
httpd = ThreadingSimpleServer(server_address, handler)

# Create an SSL context and wrap the HTTP server's socket
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='./secrets/cert.pem', keyfile='./secrets/key.pem')

# Wrap the socket with the SSL context
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

# Start the server
print(f"Serving on https://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
