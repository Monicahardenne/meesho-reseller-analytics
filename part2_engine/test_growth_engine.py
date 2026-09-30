from growth_engine import (
    mom_growth,
    is_flagged,
    validate_feed
)

# TEST 1
growth = mom_growth(104520.77, 185107.61)

assert growth == 77.1
assert is_flagged(growth) == "flagged"

print("Test 1 Passed")


# TEST 2
growth = mom_growth(35542.11, 37559.07)

assert growth == 5.67
assert is_flagged(growth) == "not_flagged"

print("Test 2 Passed")


# TEST 3
growth = mom_growth(100000, 108000)

assert growth == 8.0
assert is_flagged(growth) == "escalate_exact_boundary"

print("Test 3 Passed")


# TEST 4
valid, errors = validate_feed(
    "part2_engine/fixtures/corrupted_feed.csv"
)

assert valid is False

expected_errors = [
    "line 3: negative revenue (-4200.0) for category=Western Wear",
    "line 4: missing category (month=July)",
    "line 6: missing revenue (category=Home & Kitchen)"
]

assert errors == expected_errors

print("Test 4 Passed")


# VALID FILE TEST

valid, errors = validate_feed(
    "part2_engine/fixtures/monthly_category_revenue.csv"
)

assert valid is True
assert errors == []

print("Valid Feed Test Passed")

print("\nALL TESTS PASSED")