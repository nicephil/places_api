# places_api
Query place addresses  
we use <a href="https://falcon.readthedocs.io/en/stable/user/index.html"> falcon </a> framework to implement the api

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
```
- run gunicorn to serve the api:
```shell
    gunicorn --reload --bind 0.0.0.0:80 src.server:api
```
gunicorn don't support ``src/server:api``, has to use ``src.server:api`` if the module is not in current directory
