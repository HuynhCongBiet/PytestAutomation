import pytest
# Test case must be written inside a method
# Method name must ben started with test word
@pytest.mark.Smoke
def test_tc_007_Verify_Table_Testing():
    print("This is testcase 007: Smoke test case...")

@pytest.mark.Sanity
def test_tc_008_Verify_String_InvalidCreadentials():
    print("This is testcase 008: Sanity test case...")
