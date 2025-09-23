# ML_OPS_LAB – Currency Converter (with Pytest & Unittest)

A simple, deterministic **currency converter** implemented in Python with
**unit tests (pytest + unittest)** and optional **GitHub Actions** CI.

The converter uses USD as the base:
> Rates are stored as: **1 USD = rate[currency]** (e.g., `EUR: 0.92` means 1 USD = 0.92 EUR)

---

## Features
- `convert(amount, src, dst, round_to=2)` – convert between currencies with banker's rounding
- Manage rates:
  - `list_currencies()`
  - `get_rate(code)`
  - `add_rate(code, per_usd)`
  - `set_rates({...})`
  - `reset_rates()`
- Tests in both **pytest** and **unittest**
- Ready for CI via **GitHub Actions**

---

## Project Structure
