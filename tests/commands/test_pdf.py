"""
Test the 'commands.pdf' command.
"""

# module under test
from amtools import PKG_NAME
from amtools.entry import main as amtools_main

# internal
from tests.resources import resource


def test_pdf_basic():
    """Test basic 'pdf' command invocations."""

    args = [
        PKG_NAME,
        "pdf",
        str(resource("Amazon.com - Order 111-0005087-4084226.pdf")),
    ]
    assert amtools_main(args) == 0

    # assert False
