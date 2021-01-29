import pytest
import os
import errno
from configparser import ConfigParser


@pytest.fixture(scope="session", autouse=True)
def env(pytestconfig):
    """Return the contents of the env file selected for the test run"""
    cfg_filename = f"env.{pytestconfig.getoption('env')}.ini"
    cfg = ConfigParser()
    cfg.read(cfg_filename)
    if len(cfg.sections()) == 0:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), cfg_filename)
    return cfg


@pytest.fixture
def head_mode(pytestconfig):
    headful = pytestconfig.getoption("--headful", default=False)
    if headful:
        return "headful"
    else:
        return "headless"


@pytest.fixture(autouse=True)
def skip_by_head_mode(head_mode, request):
    if request.node.get_closest_marker("skip_if_headful"):
        if head_mode == "headful":
            pytest.skip("skipped due to {} mode".format(head_mode))
    if request.node.get_closest_marker("skip_if_headless"):
        if head_mode == "headless":
            pytest.skip("skipped due to {} mode".format(head_mode))