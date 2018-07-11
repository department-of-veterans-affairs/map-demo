# produces a SHA hash on post to /
# 1. sudo docker build -t hash_service:latest .
# 2. sudo docker run -p 5000:80 hasher
# 3. curl -X POST localhost:5000 == random SHA1 hash

require 'digest'
require 'sinatra'
require 'socket'

set :bind, '0.0.0.0'
set :port, 80

post '/' do
    sleep 0.1
    content_type 'text/plain'
    "#{Digest::SHA1.new().update(request.body.read)}"
end

get '/' do
    "hash_service running on #{Socket.gethostname}\n"
end
