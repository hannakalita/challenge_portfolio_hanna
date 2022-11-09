from pages.base_page import BasePage


class Dashboard (BasePage):
   header_xpath = "//*[@id="__next"]/div[1]/header/div/h6"
   main_page_button_menu_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
   players_button_menu_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]"
   language_button_menu_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]"
   sign_out_button_menu_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]"
   players_count_display_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[1]/div"
   add_player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
   dev_team_contact_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a"
   activity_board_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div"
   matches_count_board_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[2]/div"
