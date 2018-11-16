# places_api
Query place addressed  
we use <a href="https://falcon.readthedocs.io/en/stable/user/index.html"> falcon </a> framework to implement the api

## how-to
1. build/list/run image:
```shell
    docker build -t ykang/places_api:latest  .
    docker image ls
    docker run -v $(pwd)/src:/oakridge -it -p 8000:80 --name places_api ykang/places_api:latest bash
```
2. detach/attach to docker:
```shell
    docker attach places_api            # from host shell, attach
    ctrl-p ctrl-q                       # from inside docker, detach
```
