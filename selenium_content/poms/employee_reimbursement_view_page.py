class EmployeeReimbursementViewPage:
    reason_value = 'reimbursements_view'
    amount_value = 'sojf'

    def __init__(self, driver):
        self.driver = driver

    def get_amount_reason_value(self):
        allParagraphs = self.driver.find_element_by_xpath('//*[@id="1234 some reason"]')
        if allParagraphs:
            return 'true'
        else:
            return 'false'
