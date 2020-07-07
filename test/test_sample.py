def test_sample(browser):
    browser.get("http://www.google.com")
    title = "Google"
    print("yep, it's running...")
    assert title == browser.title