#
#  This file is part of Financio Test Utilities
#
# This module provides helpers for automation testing of Financio
# with Playwright & Pytest.
#
def login(page, login_url, userid, password):
    page.goto(login_url)

    # Fill input[name="email"]
    page.fill('input[name="email"]', userid)

    # Fill input[name="password"]
    page.fill('input[name="password"]', password)

    # Click text="LOGIN"
    with page.expect_navigation():
        page.click('text="LOGIN"')