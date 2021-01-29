def addoptions(parser):
    """Select the env file to use for the tests
    In root directory of the test suite there should be a file for each env to be tested.
    e.g.
        env.test.ini
        env.staging.ini
        env.live.ini
    These env file hold common test attributes like login_useid, home_url etc
    """
    parser.addoption("--env", action="store", default="test")


def configure_markers(config):
    config.addinivalue_line(
        "markers", "skip_if_headful: skip this test if running in headful mode."
    )
    config.addinivalue_line(
        "markers", "skip_if_headless: skip this test if running in headless mode."
    )
