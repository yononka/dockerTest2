def test_sample(browser):
    browser.get("http://www.google.com")
    title = "Google"
    print("yep, it's running...")
    # screenshot = browser.save_screenshot('test.png')
    assert title == browser.title
