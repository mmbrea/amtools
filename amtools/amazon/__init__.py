"""
A module for working with Amazon PDF documents.
"""

# built-in
from collections import defaultdict
from contextlib import suppress
from os import linesep
from pathlib import Path
import re
from typing import NamedTuple

# third-party
from vcorelib import DEFAULT_ENCODING
from vcorelib.logging import LoggerMixin, LoggerType


class OrderData(NamedTuple):
    """A container for raw order data."""

    quantities: list[int]
    descriptions: list[str]
    prices: list[float]

    lines: list[str]

    def audit(self, order: str, logger: LoggerType) -> bool:
        """Ensure data matches."""

        len_q = len(self.quantities)
        len_d = len(self.descriptions)
        len_p = len(self.prices)

        result = len_q == len_d == len_p

        if not result:
            logger.error(
                "%s: quantities=%d, descriptions=%d, prices=%d.",
                order,
                len_q,
                len_d,
                len_p,
            )

            max_val = max(len_q, len_d, len_p)
            for idx in range(max_val):
                quant = "MISSING"
                desc = quant
                price = quant

                with suppress(IndexError):
                    quant = str(self.quantities[idx])
                with suppress(IndexError):
                    desc = self.descriptions[idx]
                with suppress(IndexError):
                    price = str(self.prices[idx])

                logger.info(
                    "quantity=%s price=%s description=%.20s",
                    quant,
                    price,
                    desc,
                )

        return result

    @staticmethod
    def create() -> "OrderData":
        """Create new order data."""
        return OrderData([], [], [], [])


class OrderAssembler(LoggerMixin):
    """A class for assembling invoice lines into coherent data structures."""

    def __init__(self) -> None:
        """Initialize this instance."""

        super().__init__()
        self.curr_order: str = ""
        self.orders: dict[str, OrderData] = defaultdict(OrderData.create)

    def order_number(self, number: str) -> None:
        """Handle order number."""

        self.logger.debug("Order number: %s.", number)
        self.curr_order = number

    def quantity_description(self, quantity: int, description: str) -> None:
        """Handle quantity and description."""

        self.logger.debug("%d count of '%s'.", quantity, description)

        assert self.curr_order
        self.orders[self.curr_order].quantities.append(quantity)
        self.orders[self.curr_order].descriptions.append(description)

    def price(self, cost: float) -> None:
        """Handle a price value."""

        self.logger.debug("Price: %.2f.", cost)
        self.orders[self.curr_order].prices.append(cost)

    def handle_line(self, line: str) -> None:
        """Handle a line from an Amazon invoice."""

        # Handle 'grand total' lines.
        if line.startswith("Grand Total: $"):
            line = line.replace("Grand Total: $", "")
            match = re.search(r"\d+\.\d\d", line)
            assert match is not None

            line = line.replace(match.group(0), "")

        # Get the overall order number.
        if "Final Details for Order #" in line:
            self.order_number(
                line.replace("Final Details for Order #", "").strip()
            )

        # Parse unit quantity.
        match = re.search(r"^(\d) of: ", line)
        if match:
            desc = line.replace(match.group(0), "").replace('"', "'")

            # Sanity check.
            assert "$" not in desc, desc
            self.quantity_description(int(match.group(1)), desc)

        # Parse price.
        if line.startswith("Condition: ") and "$" in line:
            _, price = line.split("$")
            self.price(float(price))

        # Keep track of raw lines.
        if self.curr_order:
            self.orders[self.curr_order].lines.append(line)

    def dump(self, output: Path) -> None:
        """Dump order results."""

        total = 0.0

        with output.open("w", encoding=DEFAULT_ENCODING) as path_fd:
            # Audit order data.
            for name, order in self.orders.items():
                if order.audit(name, self.logger):

                    for name, quantity, price in zip(
                        order.descriptions, order.quantities, order.prices
                    ):
                        total += quantity * price
                        self.logger.info(
                            "%s: %d * %.2f.", name, quantity, price
                        )

                        path_fd.write(
                            ",".join([f'"{name}"', str(quantity), str(price)])
                        )
                        path_fd.write(linesep)

        self.logger.info("Total: %.2f.", total)
