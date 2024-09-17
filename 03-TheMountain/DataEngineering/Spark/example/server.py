from websocket import create_connection, WebSocketConnectionClosedException
import json
import socket

# Set Coinbase websocket URL
coinbase_url = "wss://ws-feed.exchange.coinbase.com"

# Set localhost socket parameters
localhost = "127.0.0.1"
local_port = 8776

# Create local socket
local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_socket.bind((localhost, local_port))
local_socket.listen(1)
print(f"Listening for local connections on {localhost}:{local_port}...")

# Connect to Coinbase websocket
try:
    ws = create_connection(coinbase_url)
    print("Connected to Coinbase WebSocket.")
except Exception as e:
    print(f"Failed to connect to Coinbase WebSocket: {e}")
    exit(1)

# Subscribe to desired channels and products
subscribe_message = {
  "type": "subscribe",
  "product_ids": ["ETH-USD", "ETH-EUR"],
  "channels": [
    "level2",
    "heartbeat",
    {
      "name": "ticker",
      "product_ids": ["ETH-BTC", "ETH-USD"]
    }
  ]
}

ws.send(json.dumps(subscribe_message))

# Wait for connection from local client
# !!! Will block until connection is made !!!
local_socket.settimeout(60)  # Timeout after 60 seconds if no connection
try:
    conn, addr = local_socket.accept()
    print("Connected by", addr)
except socket.timeout:
    print("No client connected within the timeout period.")
    ws.close()
    local_socket.close()
    exit(1)

# Forward stream from Coinbase websocket to local socket
try:
    while True:
        try:
            data = ws.recv()
            conn.send(bytes(data + "\n", "ascii"))
        except WebSocketConnectionClosedException as e:
            print(f"WebSocket connection closed: {e}")
            break
        except Exception as e:
            print(f"Error receiving or forwarding data: {e}")
            break
finally:
    ws.close()
    local_socket.close()
    print("Connections closed.")
