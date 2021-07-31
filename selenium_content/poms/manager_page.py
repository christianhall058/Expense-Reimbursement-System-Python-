class ManagerPage:
    view_btn_id = 'reimbursements_view'
    stat_btn_id = 'statistics_view'

    def __init__(self, driver):
        self.driver = driver

    def click_view_manager_requests(self):
        self.driver.find_element_by_id(self.view_btn_id).click()

    def click_statistics(self):
        self.driver.find_element_by_id(self.stat_btn_id).click()
