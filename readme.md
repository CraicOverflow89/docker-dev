Docker Update
=============

Command line tool for updating all relevent repositories for your current docker requirements.

### Usage

Place an executable `docker-dev` file on PATH pointing to a script like this;

```
from docker_update import DockerUpdate

DockerUpdate.update()
```

Simplty invoke `$ docker-dev` when in a repository, where `docker-compose.yml` is in the parent, to update all of the related projects to the latest version of develop.