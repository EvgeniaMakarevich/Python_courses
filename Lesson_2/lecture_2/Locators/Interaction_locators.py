from selenium.webdriver.common.by import By


# class Interactionslocators:
#     DRAG = (By.XPATH,'//*[@id="draggable"]')
#     DROP = (By.XPATH,'//*[@id="droppable"]')
#     DROP_TEXT = (By.XPATH,'//*[@id="droppable"]/p')

class Interactionslocators:
    DRAG = (By.XPATH, '//*[@id="draggable"]')
    DROP = (By.XPATH, '//*[@id="droppable"]')
    DROP_TEXT = (By.CSS_SELECTOR, '#droppable > p')
    ACCEPT  = (By.XPATH, '//*[@id="acceptable"]')
    NOT_ACCEPT = (By.XPATH, '//*[@id="notAcceptable"]')
    DROP_1 = (By.XPATH, '//*[@id="droppable"]')
