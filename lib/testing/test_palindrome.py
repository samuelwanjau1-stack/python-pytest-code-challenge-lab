import pytest
from palindrome import longest_palindromic_substring

@pytest.mark.parametrize("input_str, expected", [
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a", "c"]),
    ("racecar", ["racecar"]),
    ("", [""]),
])
def test_longest_palindromic_substring(input_str, expected):
    result = longest_palindromic_substring(input_str)
    assert result in expected
