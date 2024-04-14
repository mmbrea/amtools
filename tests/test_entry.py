"""
amtools - Test the program's entry-point.
"""

# built-in
from subprocess import check_output
from sys import executable
from unittest.mock import patch

# module under test
from amtools import PKG_NAME
from amtools.entry import main as amtools_main


def test_entry_basic():
    """Test basic argument parsing."""

    args = [PKG_NAME, "noop"]
    assert amtools_main(args) == 0

    with patch("amtools.entry.entry", side_effect=SystemExit(1)):
        assert amtools_main(args) != 0


def test_package_entry():
    """Test the command-line entry through the 'python -m' invocation."""

    check_output([executable, "-m", "amtools", "-h"])
