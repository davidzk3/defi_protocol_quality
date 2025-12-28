import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import pandas as pd

BASE_URL = "https://api.llama.fi"
RAW_DIR = Path("data/raw")


def get_json(url: str, retries: int = 3, sleep_s: int = 2):
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            last_err = e
            print(f"Request failed attempt {attempt}/{retries}: {e}")
            time.sleep(sleep_s * attempt)
    raise RuntimeError(f"Failed after {retries} retries. Last error: {last_err}")


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    run_ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    protocols = get_json(f"{BASE_URL}/protocols")

    raw_path = RAW_DIR / f"protocols_{run_ts}.json"
    raw_path.write_text(json.dumps(protocols), encoding="utf-8")

    df = pd.DataFrame(protocols)
    keep = [c for c in ["name", "slug", "tvl", "chain", "category"] if c in df.columns]
    clean = df[keep].copy()

    parquet_path = RAW_DIR / f"protocols_clean_{run_ts}.parquet"
    clean.to_parquet(parquet_path, index=False)

    print("Saved:", raw_path)
    print("Saved:", parquet_path)
    print("Rows:", len(clean))


if __name__ == "__main__":
    main()
