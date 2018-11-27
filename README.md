# places_api
a proxy to query google places API
we use <a href="https://falcon.readthedocs.io/en/stable/user/index.html"> falcon </a> framework to implement the proxy

## how-to
- build/list/run image:
```shell
    docker build -t ykang/places_api:latest  .
    docker image ls
    docker run -v $(pwd):/oakridge -it -p 8000:80 --name places_api ykang/places_api:latest bash
```
- detach/attach to docker:
```shell
    docker attach places_api            # from host shell, attach
    ctrl-p ctrl-q                       # from inside docker, detach
    docker exec -it <running_container> bash # run bash inside container interactively
```
- run gunicorn inside docker to serve the api:
```shell
    gunicorn --reload --bind 0.0.0.0:80 src.server:api
```
gunicorn don't support ``src/server:api``, has to use ``src.server:api`` if the module is not in current directory  
A more debug friendly gunicorn:
```shell
DEBUG=0 gunicorn --reload --bind 0.0.0.0:80 src.server:api --access-logfile /tmp/gunicorn.access.log --error-logfile /tmp/gunicorn.error.log
```
## Note
On deployment, must add google API key into ``src/places.py`` to make it work
