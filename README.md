# MAP Demo

This is a demo _obviously fake_ crypto coin mining application written in Python, JavaScript, and Ruby that runs as five separate services on a single server orchestrated by Docker Compose with `nginx` as a web server in front (tbd). Each service has its own Dockerfile. The `api` service calls the `rng_service` and the `hash_service` to produce hashes. Results are stored in the `redis` service. The `web_frontend` is the view into the hashing and mining of coins. 

***Note: Does not actually mine cryptocurrency, this is for an orchestration demo :D ***

## Steps to install application

1. install docker and docker compose
2. git clone this repo
3. to build services run `docker-compose build`
4. to run the build run `docker-compose run`
5. access web frontend at `localhost:8080`

## TO DO

1. Stand up nginx web server for ingress
2. Add Vue.js to the front end?
