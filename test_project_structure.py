import os

VERSION = '0.0.1'


def make_path(*args):
    """Creates an absolute path within the project folder"""

    return os.path.join(os.path.realpath(os.path.dirname(__file__)), *args)


def path_exists(*args):
    """Determines if the specified path exists"""

    return os.path.exists(make_path(*args))


def test_required_files_present():
    """Required files should exist"""
    assert path_exists('README.md')
    assert path_exists('.gitignore')
    assert path_exists('.gitlab-ci.yml')
    assert path_exists('requirements.txt')
    assert path_exists('.coafile')
    assert path_exists('.coveragerc')
