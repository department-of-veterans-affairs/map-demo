# MAP Demo

This is a demo of an _obviously fake_ crypto coin mining application written in Python, JavaScript, and Ruby that runs as five separate services on a single server orchestrated by Docker Compose with an `nginx` web server in front. Each service has its own Dockerfile. The `api` service calls the `rng_service` and the `hash_service` to produce hashes. Results are stored in the `redis` service. The `web_frontend` is the view into the hashing and mining of coins. 

*** Note: Does not actually mine cryptocurrency, this is for an orchestration demo :stuck_out_tongue_winking_eye: ***

## Steps to install application

1. install docker and docker compose
2. clone this repo with `git clone https://github.com/department-of-veterans-affairs/map-demo.git`
3. then build services with `docker-compose build`
4. then run the build with `docker-compose run` 
5. then access web frontend at `localhost` (standard port 80)
6. :tada:

## TO DO

~~1. Stand up nginx web server for ingress~~
2. Add Vue.js to the front end?
