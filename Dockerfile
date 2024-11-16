# ベースイメージとして公式のPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# ポートを公開
EXPOSE 8000

# 環境変数の設定
ENV PYTHONPATH="/app"
ENV LANG ja_JP.utf8

# アプリケーションを起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]