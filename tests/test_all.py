import pytest
import tempfile

from pathlib import Path

from trakky.main import PATH


@pytest.fixture
def tempdir():
    with tempfile.TemporaryDirectory() as tempdir:
        yield Path(tempdir)


def test_PATH(tempdir):
    breakpoint()
    assert False
