from selenium import webdriver


class initial_functionality:

    def __init__(self, driver):
        self.driver = driver

    def go_to_demo_admin(self):
        self.driver.find_element_by_link_text("View Demo").click()

    def admin_login_username(self, username):
        self.driver.find_element_by_id("input-username").clear()
        self.driver.find_element_by_id("input-username").send_keys(username)

    def admin_login_password(self, password):
        self.driver.find_element_by_id("input-password").clear()
        self.driver.find_element_by_id("input-password").send_keys(password)

    def admin_login_button(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
    def admin_logout_button(self):
        self.driver.find_element_by_id("//a[@href='https://demo.opencart.com/admin/index.php?route=common/logout&user_token=fxEEzcF5fEFbiVPCkehbdhCEoTu9PqCc']").click()

    
    def checking_profile(self):
        self.driver.find_element_by_xpath("//*[@href='#']").click() #demo demo dropdown


    def select_profile_method(self):
        self.driver.find_element_by_link_text("Your Profile").click()  #profile editing in demo demo.

    def admin_profile_editing_username(self):
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys("demo")
    
    def admin_profile_editing_first_name(self):
        self.driver.find_elements_by_id("input-firstname").clear()
        self.driver.find_elements_by_id("input-firstname").send_keys("demo")
    def admin_profile_editing_last_name(self):
        self.driver.find_elements_by_id("input-lastname").clear()
        self.driver.find_elements_by_id("input-lastname").send_keys("demo")
    def admin_profile_editing_first_name(self):
        self.driver.find_elements_by_id("input-email").clear()
        self.driver.find_elements_by_id("input-email").send_keys("demo@opencart.com")
    def admin_profile_editing_password(self):
        self.driver.find_element_by_name("password").clear()
        admin_password = self.driver.find_element_by_name("password").send_keys("demo")
        return admin_password
    def admin_profile_editing_confirm_password(self):
        self.driver.find_element_by_name("confirm").clear()
        admin_confirm_password = self.driver.find_element_by_name("confirm").send_keys("demo")
        return admin_confirm_password

    def save_admin_profile(self):
        self.driver.find_element_by_xpath("//i[@class='fa fa-save']").click()
    
    def discard_edit_profile(self):
        self.driver.find_elements_by_xpath("//a[@href='https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token=DiV07pw1MYRgscv24HICdZ8SbWvDnwyC']").click()




    def select_your_store(self):
        self.driver.find_elements_by_link_text("Your Store").click()
    def your_store_search_box(self, search_values):
        self.driver.find_element_by_name("search").send_keys(search_values)
    def open_cart_homepage(self):
        self.driver.find_element_by_xpath("//a[@href='http://docs.opencart.com']")
    
    def demo_documentation(self):
        self.driver.find_element_by_xpath("//a[@href='http://docs.opencart.com']")
    def support_forum(self):
        self.driver.find_element_by_xpath("//a[href='http://forum.opencart.com']")
    