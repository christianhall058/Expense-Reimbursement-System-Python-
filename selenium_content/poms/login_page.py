class LoginPage:
    username_box_id = 'loginUser'
    password_box_id = 'loginPassword'
    login_button_id = 'submitbtn'

    def __init__(self, driver):
        self.driver = driver

    def enter_employee_credentials(self):
        self.driver.find_element_by_id(self.username_box_id).send_keys('catman')
        self.driver.find_element_by_id(self.password_box_id).send_keys('catman')

    def enter_manager_credentials(self):
        self.driver.find_element_by_id(self.username_box_id).send_keys('batman')
        self.driver.find_element_by_id(self.password_box_id).send_keys('batman')

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()

