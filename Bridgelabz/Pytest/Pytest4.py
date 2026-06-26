#Markers 
import pytest 
import sys
@pytest.mark.skipif(sys.platform == "win32", reason="This test is skipped on Windows")
class Testclass:
    def test_example(self):
        "The test will not run under Windows OS" 

import pytest
import sys
@pytest.mark.skip(reason="This test is skipped unconditionally")
def test_example():
    "This test will always be skipped regardless of the platform" 

import pytest
import sys
@pytest.mark.xfail(sys.platform == "win32", reason="This test is expected to fail on Windows")
def test_example():
    "This test is expected to fail on Windows OS"

class TestClass:
    def test_method(self):
        "This test method is expected to fail on Windows OS"

