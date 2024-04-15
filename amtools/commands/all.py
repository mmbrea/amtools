# =====================================
# generator=datazen
# version=3.1.4
# hash=de631bc43b999bfd6958510f26d3200e
# =====================================

"""
A module aggregating package commands.
"""

# built-in
from typing import List as _List
from typing import Tuple as _Tuple

# third-party
from vcorelib.args import CommandRegister as _CommandRegister

# internal
from amtools.commands.pdf import add_pdf_cmd
from amtools.commands.sheets import add_sheets_cmd


def commands() -> _List[_Tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "pdf",
            "Dissecting PDFs",
            add_pdf_cmd,
        ),
        (
            "sheets",
            "Interacting with Google Sheets",
            add_sheets_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
