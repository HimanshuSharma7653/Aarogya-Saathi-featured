"""Local development launcher. Use this file instead of app.py."""
import os
import secrets
from pathlib import Path

ROOT = Path(__file__).resolve().parent
instance = ROOT / "instance"
instance.mkdir(exist_ok=True)
secret_file = instance / "secret_key"
if not secret_file.exists():
    secret_file.write_text(secrets.token_hex(32), encoding="utf-8")
os.environ.setdefault("SECRET_KEY", secret_file.read_text(encoding="utf-8").strip())

from app import app, database  # noqa: E402

database.init_db()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=False)
