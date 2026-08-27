#!/usr/bin/env python3
"""Print Mon–Sun report periods (current + previous week)."""

from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta


def last_sunday(ref: date | None = None) -> date:
    ref = ref or date.today()
    # Most recent Sunday strictly before today if today is not Sunday past week end logic
    dow = ref.weekday()  # Mon=0 ... Sun=6
    days_since_sunday = (dow + 1) % 7
    if days_since_sunday == 0:
        days_since_sunday = 7
    return ref - timedelta(days=days_since_sunday)


def week_range(week_end: date) -> tuple[date, date]:
    start = week_end - timedelta(days=6)
    return start, week_end


def fmt(d: date) -> str:
    return d.isoformat()


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute SEO weekly report periods")
    parser.add_argument(
        "--week-end",
        help="Week ending Sunday YYYY-MM-DD (default: last completed Sunday)",
    )
    args = parser.parse_args()

    if args.week_end:
        y, m, d = map(int, args.week_end.split("-"))
        end = date(y, m, d)
    else:
        end = last_sunday()

    if end.weekday() != 6:
        print(
            f"WARNING: --week-end {fmt(end)} is not Sunday "
            f"(weekday={end.strftime('%A')}). Use the Sunday ending the Mon-Sun report week.",
            file=sys.stderr,
        )

    cur_start, cur_end = week_range(end)
    prev_end = cur_start - timedelta(days=1)
    prev_start, prev_end = week_range(prev_end)

    print(f"current:  {fmt(cur_start)} ~ {fmt(cur_end)}")
    print(f"previous: {fmt(prev_start)} ~ {fmt(prev_end)}")
    print(f"bundle_suffix: {fmt(cur_end)}")


if __name__ == "__main__":
    main()
