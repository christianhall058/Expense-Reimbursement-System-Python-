class ManagerReimbursementViewPage:
    approve_btn_id = 'approve_1'
    disapprove_btn_id = 'disapprove_1'
    manager_response_tb_id = 'textbox_1'
    status_id = 'disapprove_2'

    def __init__(self, driver):
        self.driver = driver

    def click_approve(self):
        self.driver.find_element_by_id(self.approve_btn_id).click()

    def click_disapprove(self):
        self.driver.find_element_by_id(self.disapprove_btn_id).click()

    def enter_manager_response(self):
        self.driver.find_element_by_id(self.manager_response_tb_id).send_keys('something')

    def check_status(self):
        status = self.driver.find_element_by_id(self.status_id)

        if status:
            return 'true'
        else:
            return 'false'