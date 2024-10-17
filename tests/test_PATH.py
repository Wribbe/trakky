import pytest
import tempfile

from pathlib import Path

from trakky.main import PATH


@pytest.fixture(scope="session")
def tempdir():
    with tempfile.TemporaryDirectory() as tempdir:
        yield Path(tempdir)


def test_file_gets_created(tempdir):
    path_file = tempdir / 'test.txt'
    assert not path_file.exists()
    PATH(path_file)
    assert path_file.exists()


def test_single_dir_gets_created(tempdir):
    path_dir = tempdir / "test_dir"
    assert not path_dir.exists()
    PATH(path_dir)
    assert path_dir.exists()
    assert path_dir.is_dir()


def test_nested_dir_gets_created(tempdir):
    dirs = [tempdir / 'a']
    for name in ['b','c','d']:
        dirs.append(dirs[-1] / name)
    for path in dirs:
        assert not path.exists()

    PATH_LAST = PATH(dirs[-1])
    assert PATH_LAST.exists()
    assert PATH_LAST.is_dir()

    for path in dirs:
       assert path.exists()
       assert path.is_dir()
