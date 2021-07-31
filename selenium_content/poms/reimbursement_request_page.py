class ReimbursementRequestPage:
    reason_tb_id = 'reason'
    amount_tb_id = 'amount'
    submit_btn_id = 'submit_request'

    def __init__(self, driver):
        self.driver = driver

    def enter_reason(self):
        self.driver.find_element_by_id(self.reason_tb_id).send_keys('some reason')

    def enter_amount(self):
        self.driver.find_element_by_id(self.amount_tb_id).send_keys('1234')

    def click_submit(self):
        self.driver.find_element_by_id(self.submit_btn_id).click()