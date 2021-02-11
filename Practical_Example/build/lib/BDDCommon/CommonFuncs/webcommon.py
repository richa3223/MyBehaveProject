from selenium import webdriver


def go_to(url, browser_type=None):
    if not browser_type:
        driver = webdriver.Chrome()
    elif browser_type.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f" The browser type {browser_type} is nor supported")
    url = url.strip()
    driver.get(url)
    return driver


def assert_page_title(context, expected_title):
    actual_title = context.driver.title
    print(f"Actual title is {actual_title}")
    print(f"Expected title is {expected_title}")
    assert actual_title == expected_title, f"Title does not match with the expected title, title is :{actual_title}"
    print("Page title is expected.")


def assert_currenturl(context, expected_url):
    current_url = context.driver.current_url
    if not expected_url.startswith('http'):
        expected_url = 'https://' + expected_url + '/'

    print(f"Actual url is {current_url}")
    print(f"Expected url is {expected_url}")
    assert current_url == expected_url, f"Url does not match with the expected one, current_url:" \
                                        f" {current_url}, expected_url: {expected_url}"
    print()