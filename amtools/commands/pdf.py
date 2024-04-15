"""
An entry-point for the 'pdf' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from pathlib import Path
from typing import Iterator

# third-party
from pypdf import PdfReader
from vcorelib.args import CommandFunction as _CommandFunction

# internal
from amtools.amazon import OrderAssembler


def pdf_lines(path: Path) -> Iterator[str]:
    """Yield lines of text from a path to a PDF document."""

    for page in PdfReader(path).pages:
        yield from page.extract_text().splitlines()


def pdf_cmd(args: _Namespace) -> int:
    """Execute the pdf command."""

    assembler = OrderAssembler()

    # Gather all lines from PDF documents.
    for pdf in args.pdfs:
        for line in pdf_lines(pdf):
            assembler.handle_line(line)

    # Dump results.
    assembler.dump(Path("amazon_out.csv"))

    return 0


def add_pdf_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add pdf-command arguments to its parser."""

    parser.add_argument("pdfs", type=Path, nargs="*", help="pdfs to process")

    return pdf_cmd
