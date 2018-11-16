# places_api

api for query places addresss

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
