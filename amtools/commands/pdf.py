"""
An entry-point for the 'pdf' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from logging import getLogger
from pathlib import Path

# third-party
from pypdf import PdfReader
from vcorelib.args import CommandFunction as _CommandFunction

LOG = getLogger(__name__)


def pdf_cmd(args: _Namespace) -> int:
    """Execute the pdf command."""

    for pdf in args.pdfs:
        parsed = PdfReader(pdf)
        for page in parsed.pages:
            content = page.extract_text()
            # LOG.info(content)
            # LOG.info(content.split())
            lines = content.splitlines()
            for line in lines:
                # LOG.info(line)  # to print whole thing
                if "Final Details for Order #" in line:
                    LOG.info(line)
                if "1 of: " in line:
                    LOG.info(line)
                if "Condition: " in line:
                    if "Grand" in line:
                        print("no idea where this goes")  # skip it
                    else:
                        LOG.info(line)
                        LOG.info("next item: ")
                # if "tax" in line:
                # LOG.info(line) # could grab out tax prices.

    return 0


def add_pdf_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add pdf-command arguments to its parser."""

    parser.add_argument("pdfs", type=Path, nargs="*", help="pdfs to process")

    return pdf_cmd
