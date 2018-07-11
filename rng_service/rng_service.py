# produces an octet stream of desired size on get to /<num_of_bytes>
# 1. sudo docker build -t rng:latest .
# 2. sudo docker run -p 5000:80 rng
# 3. curl localhost:5000/32 returns random octets
# 

from flask import Flask, Response
import os
import socket
import time

app = Flask(__name__)

hostname = socket.gethostname()

# get urandom
urandom = os.open("/dev/urandom", os.O_RDONLY)

@app.route("/")
def index():
    return "rng_service running on {}\n".format(hostname)


@app.route("/<int:how_many_bytes>")
def rng(how_many_bytes):
    # Delay
    time.sleep(0.1)
    return Response(
        os.read(urandom, how_many_bytes),
        content_type="application/octet-stream")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
