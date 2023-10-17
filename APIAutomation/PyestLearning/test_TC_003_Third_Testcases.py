import pytest
# Test case must be written inside a method
# Method name must ben started with test word

@pytest.fixture(scope="module")
def fixtures_code():
    print("this is our Fixtures Code will execute before testcase")
    print("----------------------------------------------------")
    yield
    print("Close DB connection after executing testcase")
    print("----------------------------------------------------")

@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_005_Verify_Text_Testing(fixtures_code):
    print("This is testcase 005: Smoke and Regression test case ...")

@pytest.mark.Sanity
def test_tc_006_Verify_Element_InvalidCreadentials(fixtures_code):
    print("This is testcase 006: Sanity test case...")
