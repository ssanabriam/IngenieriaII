#pedido en pantalla
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

ORDERS_FILE = "orders.json"

def load_orders():
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as f:
            return json.load(f)
    return []

def save_orders(orders):
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f)

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/orders":
            orders = load_orders()
            self._send_response(200, orders)
        else:
            self._send_response(404, {"message": "Ruta no encontrada"})

    def do_PUT(self):
        if self.path.startswith("/orders/"):
            order_id = int(self.path.split("/")[-1])
            orders = load_orders()
            for order in orders:
                if order["id"] == order_id:
                    order["status"] = "listo"
                    save_orders(orders)
                    self._send_response(200, {"message": "Pedido marcado como listo"})
                    return
            self._send_response(404, {"message": "Pedido no encontrado"})
        else:
            self._send_response(404, {"message": "Ruta no encontrada"})

def run_server():
    server = HTTPServer(("", 8000), RequestHandler)
    print("Servidor en ejecución en el puerto 8000...")
    server.serve_forever()

if __name__ == "__main__":
    if not os.path.exists(ORDERS_FILE):
        save_orders([])
    server_thread = threading.Thread(target=run_server)
    server_thread.start()