import subprocess

import pytest


def test_behave():
    subprocess.run(["behave"], check=True)
