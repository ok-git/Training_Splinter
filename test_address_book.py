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
        # init creation of group
        browser.find_by_name('new').click()
        # fill group form
        browser.fill('group_name', 'splinter_group')
        browser.fill('group_header', 'splinter_header')
        browser.fill('group_footer', 'splinter_footer')
        # submit creation
        browser.find_by_name('submit').click()
        # open groups page
        browser.click_link_by_partial_href('group.php')
        assert browser.is_text_present('splinter_group')

