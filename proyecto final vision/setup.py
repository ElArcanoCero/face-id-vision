# -- coding: utf-8 --
from distutils.core import setup
import py2exe

setup(
    name="Bot Industries",
    version="1.0",
    description="interface de registro",
    author="grupo de trabajo Bot Industries",
    scripts=["interface.py"],
    console=["interface.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)