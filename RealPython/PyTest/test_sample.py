import pytest


class SampleClass:
    def test_always_pass(self):
        assert True

    @pytest.mark.xfail
    def test_always_fail(self):
        assert False
