def test_sample(browser):
    browser.get("http://www.google.com")
    title = "Google"
    assert title == browser.title