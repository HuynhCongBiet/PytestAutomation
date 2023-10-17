import pytest
# Test case must be written inside a method
# Method name must ben started with test word
# a = 101
actual_result = "dsadsa"
# @pytest.mark.skipif(a<100,reason="Skip as this feature is not working")
@pytest.mark.TopPriority
def test_tc_001_Login_Logout_Testing():
    print("This is testcase 001: Smoke test case...")
    assert actual_result == "Testing", "These 2 values must not be same"

@pytest.mark.TopPriority
def test_tc_002_Login_Logout_InvalidCreadentials():
    print("This is testcase 002: Sanity test case...")

# Print statement output display on console: -s
# To Display the test case name and status: -v
# To run testcase with select testcase from any text: -k
# To run test cases follows the tags: -m
# To run test and save the report use this command: pytest --alluredir D:\project\pythonProject\Reports .\APIAutomation\