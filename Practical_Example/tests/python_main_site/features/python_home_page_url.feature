Feature: verifying the home page url goes to the right place

  Scenario: The python home page should have correct title
    Given I go to the site www.python.org
   Then The page title should be Welcome to Python.org

  Scenario: The python home page should have correct url
    Given I go to the site www.python.org
    Then the current url should be www.python.org