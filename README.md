# Minimal fastapi+mongodb app

(Just for testing.)

You can populate the mongodb with GET requests using the `insert` parameter like

```
http://127.0.0.1:8000/?insert=example
```

and get all the inserted data from the root path:

```
http://127.0.0.1:8000/
```

Note: FastAPI automatically also adds the `docs` endpoint: http://127.0.0.1:8000/docs

## Publish a new docker image

```
git tag v0.1.0
git push --tags
```
