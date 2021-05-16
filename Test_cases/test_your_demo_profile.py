from selenium import webdriver
from Objects_pages.url_to_demopage import initial_functionality
import pytest
from Test_cases.test_url_to_demopage import Login



class test_your_profile:
    url = "https://www.opencart.com/index.php?route=common/home"
    username = "demo"
    password = "demo"

    def test_your_profile(self):
        self.driver = webdriver.Chrome()
        self.test_profile_obj_admin_page = initial_functionality(self.driver)
        self.driver.get("https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token=fxEEzcF5fEFbiVPCkehbdhCEoTu9PqCc")
        self.test_profile_obj_admin_page.admin_login_username(self.username)
        self.test_profile_obj_admin_page.admin_login_password(self.password)
        self.test_profile_obj_admin_page.admin_login_button()

        self.test_profile_obj_admin_page.checking_profile()
        self.test_profile_obj_admin_page.select_profile_method()
        self.test_profile_obj_admin_page.admin_profile_editing_username() # ryt now its demo for admin so values are predefined so we have jst checking the action method
        self.test_profile_obj_admin_page.admin_profile_editing_first_name()
        self.test_profile_obj_admin_page.admin_profile_editing_last_name()
        self.test_profile_obj_admin_page.admin_profile_editing_password()
        print(self.admin_password)
        self.test_profile_obj_admin_page.admin_profile_editing_confirm_password()
        print(self.admin_confirm_password)


        if self.admin_password != self.admin_confirm_password:
            element = self.driver.find_elements_by_xpath("//*[@id='form-user']/div[7]/div/div")
            print("when the given pswrd and confrm_pswrd wasn't same it should show {}: "  .format(element.is_enabled()) )
        elif self.admin_password == self.admin_confirm_password:
            element = self.driver.find_elements_by_xpath("//*[@id='form-user']/div[7]/div/div")
            print("when the given pswrd and confrm_pswrd was same it should show {}: " .format( element.is_enabled()) )
        


        self.test_profile_obj_admin_page.save_admin_profile()

        element_1 = self.driver.find_elements_by_xpath("//*[@id='content']/div[2]/div[1]/text()")

        if element_1.is_enabled() is True:
            print("the warning should displayed", element_1)
            assert True
        else:
            print("the warning was not displayed ", element_1)
            assert False
        
        self.test_profile_obj_admin_page.discard_edit_profile()
        
        dashboard_title = self.driver.title

        if dashboard_title == "Dashboard":
            print("when the discard the update demo admin profile it came to dashboard")
            assert True
        else:
            print("when the discard the update demo admin profile it wasn't came to dashboard")


        self.test_profile_obj_admin_page.admin_logout_button()

        if self.driver.title == "Administration":
            print("when logout from the dashboard it came to correct page ")
            assert True
        else:
            print("when logout from the dashboard it haven't came to correct page")
            assert False
        


    def test_your_store(self):
        self.driver = webdriver.Chrome()
        self.test_your_stores = initial_functionality(self.driver)
        self.driver.get("https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token=fxEEzcF5fEFbiVPCkehbdhCEoTu9PqCc")
        self.test_your_stores.admin_login_username(self.username)
        self.test_your_stores.admin_login_password(self.password)
        self.test_your_stores.admin_login_button()

        self.test_your_stores.checking_profile()
        self.test_your_stores.select_your_store()

        