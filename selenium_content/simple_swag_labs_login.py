# In order to use Python Selenium, we must place our WebDriver in our PATH (e.g. make sure that your PATH
# variable contains the location of your web driver exe).

# As I mentioned earlier, the WebDriver you choose depends on the browser you intend to use for your automated
# script. For example, I'm using Chrome, so I'll use the Chrome Driver. In order to access these drivers, let's
# import webdriver from selenium.

from selenium import webdriver
import time

# Of course we have to import the POMs

# Please come back and make your (Christina) packaging structure better for imports
from poms.swag_labs_login_page import SwagLabsLoginPage
from poms.inventory_page import InventoryPage
from poms.checkout_step_one_page import CheckoutStepOne
from poms.checkout_step_two_page import CheckoutStepTwo
from poms.cart import Cart

# We do have to import a few extras here to work with explicit waits:
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# If you do not add the driver executable to PATH, you can specify the location of the driver in the constructor
# for your webdriver.
driver = webdriver.Chrome()

# Sometimes we attempt to locate a web element with a correct id, class, etc. but find that we get a
# NoSuchElementException. In these cases, that does not mean that the element doesn't exist. It simply
# means that the element may not have been rendered yet. In these cases, we want to use "Selenium Waits".
# Selenium waits allow us to instruct the driver to wait a specified amount of time before attempting to
# grab and interact with a web element.

# The first type of wait we'll see is an "implicit wait". An implicit wait tells your driver to poll the DOM
# for a specified amount of time before trying to find any element that has not immediately been rendered.
# Please note that implicit waits are not preferred as you are specifying the wait for the lifetime of the driver
# and implicit waits apply to all web elements.

# Applying an implicit wait looks like so:
# The time_to_wait is in seconds, so this specifies an implicit wait of 5 seconds.
driver.implicitly_wait(5)

# Our second type of wait is an "explicit wait". An explicit wait specifies that we should wait for a certain
# condition to occur before grabbing and interacting with a web element. Note that an explicit applies only
# to the elements you specify.

# Creating an explicit wait looks like so:

element = WebDriverWait(driver, 5, 1).until(EC.visibility_of_element_located(By.CLASS_NAME('bot_column')))

# We are simply going to navigate to the home page of Swag Labs
driver.get('https://www.saucedemo.com/')

# We still need to login to SwagLabs, but this time we'll use our POMs.

sll_page = SwagLabsLoginPage(driver)
sll_page.enter_credentials()
sll_page.hit_enter_button_to_login()

# We are now theoretically on the inventory page. We can check this if you would like.

assert 'inventory' in driver.current_url

inv_page = InventoryPage(driver)
inv_page.add_backpack_to_cart()
inv_page.go_cart()

# Are we on the cart page? Let's find out.
assert 'cart' in driver.current_url

cart_page = Cart(driver)
cart_page.click_checkout_button()

# Are we on the checkout page? Let's find out.
assert 'checkout-step-one' in driver.current_url

cos1 = CheckoutStepOne(driver)
cos1.enter_personal_info()

# Are we on the second checkout page? Let's find out.

assert 'checkout-step-two' in driver.current_url

cos2 = CheckoutStepTwo(driver)
cos2.click_finish()

# Are we on the "checkout complete" page at the end of it all? Let's find out.
assert 'checkout-complete' in driver.current_url

# You get 5 seconds to see the pony.
time.sleep(5)

# Close the browser. This is effectively teardown.
driver.quit()