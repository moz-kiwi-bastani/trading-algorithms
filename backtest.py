"""
الگوریتم تریدینگ نمونه — اسکلت بک‌تست ساده
Simple backtest skeleton using pandas
"""
from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class Trade:
    entry: float
    exit: float
    direction: int  # +1 long, -1 short

    def pnl(self) -> float:
        return (self.exit - self.entry) * self.direction * 1000  # 0.1 lot XAUUSD


def generate_signals(days: int = 90) -> list[Trade]:
    """Mock signal generator — replace with your real strategy."""
    rng = random.Random(42)
    trades: list[Trade] = []
    price = 2600.0
    for _ in range(days):
        # pretend ~2 trades/week
        if rng.random() < 0.2:
            direction = 1 if rng.random() > 0.5 else -1
            entry = price
            move = rng.uniform(5, 25)
            exit_ = entry + move * direction
            trades.append(Trade(entry, exit_, direction))
        price += rng.uniform(-8, 8)
    return trades


def run() -> None:
    trades = generate_signals()
    pnls = [t.pnl() for t in trades]
    wins = sum(p > 0 for p in pnls)
    total = sum(pnls)
    print(f"Total trades: {len(trades)}")
    print(f"Wins: {wins}  Win rate: {wins/len(trades)*100:.1f}%")
    print(f"Net PnL: ${total:,.0f}")
    print(f"Avg win: ${sum(p for p in pnls if p>0)/max(wins,1):,.0f} | Avg loss: ${sum(p for p in pnls if p<0)/max(len(trades)-wins,1):,.0f}")


if __name__ == "__main__":
    run()
