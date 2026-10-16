"""15-digit IMEI format and Luhn check-digit validation; no network calls."""
from dataclasses import dataclass, asdict
import re

@dataclass(frozen=True)
class ValidationResult:
    input_value: str
    normalized: str
    digit_count: int
    is_15_digits: bool
    luhn_valid: bool | None
    expected_check_digit: int | None
    supplied_check_digit: int | None
    valid_format_and_checksum: bool
    note: str = "Checksum validity does not prove authenticity, TAC allocation, ownership, or blacklist status."
    def to_dict(self): return asdict(self)

def normalize(value):
    return re.sub(r"[^0-9]", "", str(value or ""))

def calculate_check_digit(first_14):
    if not re.fullmatch(r"[0-9]{14}", first_14): raise ValueError("Expected exactly 14 ASCII digits")
    total = 0
    for i, char in enumerate(reversed(first_14)):
        digit = int(char)
        if i % 2 == 0:
            digit *= 2
            if digit > 9: digit -= 9
        total += digit
    return (10 - total % 10) % 10

def validate_imei(value):
    digits = normalize(value); length_ok = len(digits) == 15
    expected = calculate_check_digit(digits[:14]) if len(digits) >= 14 else None
    supplied = int(digits[-1]) if length_ok else None
    luhn = (expected == supplied) if length_ok and expected is not None else None
    return ValidationResult(str(value or ""), digits, len(digits), length_ok, luhn, expected, supplied, bool(length_ok and luhn))
