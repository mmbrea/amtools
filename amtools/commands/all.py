# =====================================
# generator=datazen
# version=3.1.4
# hash=5e43a2766030a9bdc627bb963f62d72f
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


def commands() -> _List[_Tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "pdf",
            "Dissecting PDFs",
            add_pdf_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
