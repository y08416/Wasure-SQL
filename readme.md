🚀 開発環境の構築
# セットアップ手順

## プロジェクトのクローン

```bash
git clone <repository-url>
cd wasure-sql
```

## 環境変数の設定

`.env`ファイルをプロジェクトルートに作成：

```env
DATABASE_URL=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```

## アプリケーションの起動

```bash
# コンテナのビルドと起動
docker-compose up -d

# ログの確認
docker-compose logs -f
```

📝 **動作確認**

- APIドキュメント: [http://localhost:8000/docs](http://localhost:8000/docs)
- データベース接続確認:

```bash
docker exec -it wasure-sql-wasure-sql-1 psql -U postgres -d wasure_db
```

⚠️ **トラブルシューティング**

データベース接続エラーが発生する場合：

```bash
# コンテナとボリュームを削除して再起動
docker-compose down -v
docker-compose up -d
```