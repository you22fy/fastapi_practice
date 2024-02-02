# ドキュメント

## docker の設定

`docker-compose.yaml`と`Dockerfile`を作成する

- docker image を作成する

```
docker-compose build
```

- docker container を起動する

```
docker-compose up
```

## poetry の設定

docker-composeを動かしておく.
```
docker-compose up
```

- poetry をインストールする
```
docker-compose run \
  --entrypoint "poetry init \
    --name app \
    --dependency fastapi \
    --dependency uvicorn[standard] \
    --dependency sqlalchemy \
    --dependency aiomysql" \
  app
```
poetry.toml が作成される。

- 依存パッケージをインストールする
```
docker-compose run --entrypoint "poetry install --no-root" app
```

- 再ビルドする時はこれ
```
docker-compose build --no-cache
```

