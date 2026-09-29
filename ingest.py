"""Seed a Hindsight memory bank with the M&A integration demo data."""

import argparse
import asyncio
import time
from datetime import datetime

from hindsight_setup import get_client
from seed_data import SEED_MEETINGS

POLL_INTERVAL_SECONDS = 3
POLL_TIMEOUT_SECONDS = 60
FALLBACK_WAIT_SECONDS = 15


def _run_async(coro):
    """Run an async coroutine synchronously (mirrors hindsight_client's own helper)."""
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)


def _week_number(timestamp: str, start_date) -> int:
    dt = datetime.fromisoformat(timestamp).date()
    return (dt - start_date).days // 7 + 1


def ingest(bank_id: str) -> None:
    client = get_client()
    start_date = min(datetime.fromisoformat(note["timestamp"]) for note in SEED_MEETINGS).date()
    total = len(SEED_MEETINGS)

    for i, note in enumerate(SEED_MEETINGS, start=1):
        client.retain(
            bank_id=bank_id,
            content=note["content"],
            context=note["context"],
            timestamp=note["timestamp"],
        )
        week = _week_number(note["timestamp"], start_date)
        print(f"[{i}/{total}] Retained: {note['context']} - Week {week}")

    print(f"\nAll {total} notes retained into bank '{bank_id}'.")
    _wait_for_consolidation(client, bank_id)


def _wait_for_consolidation(client, bank_id: str) -> None:
    print(
        "Observations take a moment to consolidate after retain() "
        "(the server extracts and merges facts in the background)."
    )
    try:
        deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            response = _run_async(
                client.operations.list_operations(
                    bank_id=bank_id,
                    type="consolidation",
                    limit=100,
                    exclude_parents=True,
                )
            )
            in_flight = [op for op in response.operations if op.status in ("pending", "processing")]
            if not in_flight:
                print("Consolidation complete.")
                return
            print(f"  {len(in_flight)} consolidation operation(s) still in progress, waiting...")
            time.sleep(POLL_INTERVAL_SECONDS)
        print(
            f"Timed out after {POLL_TIMEOUT_SECONDS}s waiting for consolidation; "
            "it may still be finishing up in the background."
        )
    except Exception as exc:
        print(f"Could not poll the operations API ({exc}); falling back to a fixed wait.")
        time.sleep(FALLBACK_WAIT_SECONDS)
        print("Done waiting. Observations should now be consolidated.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed a Hindsight bank with M&A integration demo notes.")
    parser.add_argument(
        "--bank-id",
        default="manda-demo",
        help="Bank ID to retain notes into (default: manda-demo)",
    )
    args = parser.parse_args()
    ingest(args.bank_id)


if __name__ == "__main__":
    main()
