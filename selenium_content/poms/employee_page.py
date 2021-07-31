class EmployeePage:
    view_btn_id = 'reimbursements_view'
    make_btn_id = 'reimbursement_request'

    def __init__(self, driver):
        self.driver = driver

    def click_view_past_reimbursement_requests(self):
        self.driver.find_element_by_id(self.view_btn_id).click()


    def click_make_a_reimbursement_request(self):
        self.driver.find_element_by_id(self.make_btn_id).click()
