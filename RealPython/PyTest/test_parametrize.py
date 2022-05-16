import pytest

from .palindrome.is_palindrome import is_palindrome


@pytest.mark.parametrize("palindrome", ["", "a", "Bob", "Never odd or even"])
def test_palindrome(palindrome):
    assert is_palindrome(palindrome)


@pytest.mark.parametrize("palindrome", ["abc", "abab"])
def test_mot_palindrome(palindrome):
    assert not is_palindrome(palindrome)
