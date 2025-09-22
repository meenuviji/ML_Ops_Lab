# src/calculator.py
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Good precision for money math
getcontext().prec = 28

# Base table: 1 USD = rate[currency]
DEFAULT_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 84.0,
    "GBP": 0.78,
    "JPY": 146.0,
    "AUD": 1.50,
    "CAD": 1.36,
    "SGD": 1.35,
}

_state = {"rates": DEFAULT_RATES.copy()}


def reset_rates():
    """Reset the in-memory rates to defaults."""
    _state["rates"] = DEFAULT_RATES.copy()


def set_rates(rates: dict):
    """
    Replace the entire rate table.
    rates: mapping like {"USD": 1.0, "EUR": 0.92, ...}
    """
    if not isinstance(rates, dict) or "USD" not in rates:
        raise ValueError("rates must be a dict and include 'USD'")
    cleaned = {}
    for k, v in rates.items():
        if not isinstance(k, str):
            raise ValueError("Currency codes must be strings.")
        if not isinstance(v, (int, float)) or v <= 0:
            raise ValueError(f"Rate for {k} must be a positive number.")
        cleaned[k.upper()] = float(v)
    if abs(cleaned["USD"] - 1.0) > 1e-12:
        raise ValueError("Rate for 'USD' must be 1.0 (base).")
    _state["rates"] = cleaned


def add_rate(code: str, per_usd: float):
    """Add or update a single currency: 1 USD = per_usd <code>."""
    if not isinstance(code, str):
        raise ValueError("Currency code must be a string.")
    if not isinstance(per_usd, (int, float)) or per_usd <= 0:
        raise ValueError("Rate must be a positive number.")
    _state["rates"][code.upper()] = float(per_usd)


def get_rate(code: str) -> float:
    """Return the 'per USD' rate for a currency code."""
    code = code.upper()
    if code not in _state["rates"]:
        raise ValueError(f"Unknown currency: {code}")
    return _state["rates"][code]


def list_currencies():
    """Return a sorted list of available currency codes."""
    return sorted(_state["rates"].keys())


def convert(amount, src: str, dst: str, round_to: int = 2) -> float:
    """
    Convert amount from src to dst using USD as base.
      amount_usd = amount / rate[src]
      result     = amount_usd * rate[dst]
    Rounds to `round_to` decimal places (ROUND_HALF_UP).
    """
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number.")

    src = src.upper()
    dst = dst.upper()
    rates = _state["rates"]

    if src not in rates:
        raise ValueError(f"Unknown currency: {src}")
    if dst not in rates:
        raise ValueError(f"Unknown currency: {dst}")

    # Same currency shortcut
    if src == dst:
        q = Decimal("1." + "0" * round_to)
        return float(Decimal(str(amount)).quantize(q, rounding=ROUND_HALF_UP))

    amt = Decimal(str(amount))
    src_rate = Decimal(str(rates[src]))
    dst_rate = Decimal(str(rates[dst]))

    usd_amount = amt / src_rate
    result = usd_amount * dst_rate

    if round_to is None:
        return float(result)

    q = Decimal("1." + "0" * round_to)
    return float(result.quantize(q, rounding=ROUND_HALF_UP))


if __name__ == "__main__":
    print("Currencies:", list_currencies())
    print("100 USD -> EUR:", convert(100, "USD", "EUR"))
    print("100 EUR -> INR:", convert(100, "EUR", "INR"))
