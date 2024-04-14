# =====================================
# generator=datazen
# version=3.1.4
# hash=cee723d0532fd5ddc88fda62d2b068ac
# =====================================

"""
amtools - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from amtools_bootstrap.setup import setup  # type: ignore

# internal
from amtools import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Amber Dahlberg",
    "email": "mmbrea@hotmail.com",
    "username": "mmbrea",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.8",
        "3.9",
        "3.10",
        "3.11",
    ],
}
setup(
    pkg_info,
    author_info,
)
