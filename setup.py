# =====================================
# generator=datazen
# version=3.1.4
# hash=7e3e6c60fb0b6f9b94ae16da55f35fb1
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
        "3.11",
        "3.12",
    ],
}
setup(
    pkg_info,
    author_info,
)
