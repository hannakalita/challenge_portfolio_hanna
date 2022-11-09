from pages.base_page import BasePage


class AddNewMatch (BasePage):
email_input_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
phone_input_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
date_of_birth_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
name_input_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
surname_input_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
weight_input_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
leg_input_xpath = "//*[@id="mui-component-select-leg"]"
main_position_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
level_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
add_language_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[15]/button"