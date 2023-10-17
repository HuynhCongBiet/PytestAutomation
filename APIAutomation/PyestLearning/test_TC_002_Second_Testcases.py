import pytest
# Test case must be written inside a method
# Method name must ben started with test word

@pytest.mark.Smoke
def test_tc_003_Registration_Testing():
    print("This is testcase 003: Smoke test case...")

@pytest.mark.Sanity
def test_tc_004_Login_Logout_Validate():
    print("This is testcase 004: Sanity test case...")