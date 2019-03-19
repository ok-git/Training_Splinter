from splinter import Browser


def test_add_group_addressbook():
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


def test_add_addressbook_in_mh():
    with Browser() as browser:
        # open url
        browser.visit('https://bulk.boomware.com/login')
        # login
        browser.fill('email', 'test@svyazcom.ru')
        browser.fill('password', '123456Test')
        browser.find_by_tag('button').click()
        # enter token
        browser.fill('code', '978896')
        browser.find_by_tag('button').click()
        # open AB page
        browser.click_link_by_partial_href('address_book')
        # init AB creation
        browser.find_by_css('button.btn.btn-primary.modal_add').click()
        # fill AB form
        browser.fill('name', 'Splinter book15')
        # submit AB creation
        browser.find_by_xpath("//button[@type ='submit']").click()
        browser.is_element_not_present_by_css('div.modal-dialog', wait_time=5)
        # init AB creation
        browser.find_by_css('button.btn.btn-primary.modal_add').click()
        # fill AB form
        browser.fill('name', 'Splinter book16')
        # submit AB creation
        browser.find_by_xpath("//button[@type ='submit']").click()
        browser.is_element_not_present_by_css('div.modal-dialog', wait_time=5)
        # logout
        browser.find_by_css('li.dropdown.user').click()
        browser.click_link_by_partial_href('logout')
    pass

