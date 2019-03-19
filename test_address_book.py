from splinter import Browser


def test_add_group():
    with Browser() as browser:
        # open baseurl
        browser.visit('http://localhost/addressbook')
        # login
        browser.fill('user', 'admin')
        browser.fill('pass', 'secret')
        browser.find_by_value('Login').click()
        # open groups page
        browser.click_link_by_partial_href('group.php')

        pass
