import pytest


class TestMockResults:
    def test_pass(self):
        assert True

    def test_fail(self):
        assert False

    @pytest.mark.skip
    def test_skip(self):
        assert True

    @pytest.mark.xfail
    def test_xfail_fail(self):
        pytest.fail()

    @pytest.mark.xfail
    def test_xfail_pass(self):
        assert True
