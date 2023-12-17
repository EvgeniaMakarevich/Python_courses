#AUTH

USERNAME_FIELD = '//input[@data-test="username"]'
PASSWORD_FIELD = '//input[@data-test="password"]'
LOGIN_BUTTON = '//input[@data-test="login-button"]'


# СART
add_to_cart_button_backpack = '//button[@data-test="add-to-cart-sauce-labs-backpack"]'
remove_button_backpack = '//button[@data-test="remove-sauce-labs-backpack"]'
shopping_cart_badge_1 = '//span[@class="shopping_cart_badge"]'
shopping_cart_link = '//a[@class="shopping_cart_link"]'
continue_button = "//input[@data-test = 'continue']"
cancel_button = "//button[@data-test = 'cancel']"



# BACKPACK
item_name_before_cart_backpack = "a#item_4_title_link > div.inventory_item_name"
description_backpack = '//div[@class="inventory_item_desc"]'
price_backpack_loc = '//div[@class="inventory_item_price"]'
item_name_backpack = "//div[@class = 'inventory_item_name']"

# CHECKOUT
checkout_button = '//button[@id = "checkout"]'
checkout_title = "//span[@class='title']"
first_name_input = "//*[@id='first-name']"
last_name_input = "//*[@id='last-name']"
zip_input = "//*[@id='postal-code']"
text_error = "//h3[@data-test = 'error']"
svg_cross = '#checkout_info_container svg.svg-inline--fa.fa-times-circle.fa-w-16.error_icon'
error_fields = "//input[@class='input_error form_input error']"
error_message_container = "//div[@class='error-message-container error']"
error_button = '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3/button'
error_message_anscestor = "./ancestor::div[@class='error-message-container error']"
item_total = "//div[@class = 'summary_subtotal_label']"
item_full_total = "//div[@class = 'summary_info_label summary_total_label']"
taxes = "//div[@class = 'summary_tax_label']"


