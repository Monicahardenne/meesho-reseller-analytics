def alias_for(reseller_id: str) -> str:
    """
    Convert reseller ID to alias.
    Example:
    RS019 -> ALIAS-19
    RS006 -> ALIAS-06
    """
    return f"ALIAS-{reseller_id[3:]}"


def assert_no_raw_names_leak(text: str, reseller_names: list[str]) -> bool:
    """
    Return False if any reseller name appears in text.
    """

    for name in reseller_names:
        if name in text:
            return False

    return True


# Positive test

narrative = """
Top performing reseller in West region was ALIAS-19.
Further review is recommended.
"""

reseller_names = [
    "Mumbai Reseller 1",
    "Mumbai Reseller 4"
]

print(
    "Positive Test:",
    assert_no_raw_names_leak(
        narrative,
        reseller_names
    )
)


# Negative test

bad_narrative = """
Top performing reseller was Mumbai Reseller 1.
"""

print(
    "Negative Test:",
    assert_no_raw_names_leak(
        bad_narrative,
        reseller_names
    )
)


print(alias_for("RS019"))
print(alias_for("RS006"))