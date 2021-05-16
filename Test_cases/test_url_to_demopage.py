from selenium import webdriver
from Objects_pages.url_to_demopage import initial_functionality
import pytest
import warnings


class Login:
    url = "https://www.opencart.com/index.php?route=common/home"
    username = "demo"
    password = "demo"
    
    
    
    
    
    
    def test_view_demo(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        actual_title = self.driver.title
        if actual_title == "OpenCart - Open Source Shopping Cart Solution":
            print("the fetched the url is successful so proceed ")
            assert True
        else:
            print("the fetched the url is unsuccessful so stop it ")
            assert False
        self.driver.close()


    def test_to_go_admin(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.admn_page = initial_functionality(self.driver)
        actual_title1 = self.driver.title

        if actual_title1 == "Administration":
            self.admn_page.admin_login_username(self.username)
            self.admn_page.admin_login_password(self.password)
            self.admn_page.admin_login_button()
            print(self.driver.title)

        elif actual_title1 != "Administration":
            self.driver.get("https://demo.opencart.com/admin/")
            self.admn_page.admin_login_username(self.username)
            self.admn_page.admin_login_password(self.password)
            self.admn_page.admin_login_button()
            title = self.driver.title

            if title == "Dashboard":
                assert True
            else:
                assert False
            self.driver.close()

    




        
            
