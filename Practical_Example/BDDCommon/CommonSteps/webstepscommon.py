from behave import given, when, then
from BDDCommon.CommonFuncs import webcommon


@given("I go to the site {url}")
def go_to_url(context, url):
    print(f"navigation to the site: {url}")
    context.driver = webcommon.go_to(url)


@then("The page title should be {expected_title}")
def verify_homepage_title(context, expected_title):
    print("Verifying title")
    webcommon.assert_page_title(context, expected_title)


@then("the current url should be {expected_url}")
def verify_current_url(context, expected_url):
    print("Verifying expected url")
    webcommon.assert_currenturl(context, expected_url)
