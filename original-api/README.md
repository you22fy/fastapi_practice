# ドキュメント

## このディレクトリで作成されるもの
### Twitter API
- CRUD
  - ツイートの取得
  - ツイートの投稿
  - ツイートの削除
  - ツイートの編集
- ユーザー関連
  - ユーザーの取得
  - ユーザーの登録
  - ユーザーの削除
  - ユーザーの編集
  - login
  - logout
- いいね関連
  - いいねの取得
  - いいねの登録
  - いいねの削除
- コメント関連
  - コメントの取得
  - コメントの登録
  - コメントの削除

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


## fastapiのディレクトリ構成
```
api
├── cruds # Create, Read, Update, Delete
│   ├── __init__.py
├── models # データベースのモデル
│   ├── __init__.py
├── routers # ルーティング
│   ├── __init__.py
├── schemas # リクエストとレスポンスのスキーマ
│   ├── __init__.py
├── main.py
```