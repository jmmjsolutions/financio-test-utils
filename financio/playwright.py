#
#  This file is part of Financio Test Utilities
#
# This module provides helpers for automation testing of Financio
# with Playwright & Pytest.
#
def login(page, login_url, userid, password):
    page.goto(login_url)

    page.wait_for_selector('input[name="email"]')
    # Fill input[name="email"]
    page.fill('input[name="email"]', userid)

    page.click('input[name="password"]')
    # Fill input[name="password"]
    page.fill('input[name="password"]', password)

    # Click text="LOGIN"
    with page.expect_navigation():
        page.click('text="LOGIN"')


def evolve_login(page, login_url, userid, password):
    if "demo" in login_url:
        evolve_demo_login(page, login_url, userid)
    else:
        evolve_app_login(page, login_url, userid, password)


def evolve_app_login(page, login_url, userid, password):
    page.goto(login_url)

    page.wait_for_selector('input[name="email"]')
    # Fill input[name="email"]
    page.fill('input[name="email"]', userid)

    page.click('input[name="password"]')
    # Fill input[name="password"]
    page.fill('input[name="password"]', password)

    # Click text="Login"
    with page.expect_navigation():
        page.click("//span[normalize-space(.)='Login']")


def evolve_demo_login(page, login_url, country):
    page.goto(login_url)

    page.click("[aria-label=\"Select\"]")
    page.click(f"text={country}")
    page.click("[aria-label=\"Login\"]")