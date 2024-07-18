"""Test Framework template"""

import main


def test_main():
    """Test Main Python File"""
    greet = main.Greeting()

    assert greet.greet() == "Hello vscode!!!"
