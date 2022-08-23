from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath ="//*[@id='login']"
    player_count_xpath = "//div[contains(text(),'Players count')]"
    dev_team_contact_xpath = "//span[contains(text(),'Dev team contact')]"
    super_man_xpath = "//span[contains(text(),'super man')]"
    polski_xpath = "//span[contains(text(),'Polski')]"
    sing_out_xpath = "//span[contains(text(),'Sign out')]"
    scouts_panels_xpath = "//h6[contains(text(),'Scouts Panel')]"
    players_xpath = "//span[contains(text(),'Players')]"
    add_player_xpath = "//span[contains(text(),'Add player')]"
    events_count_xpath = "//div[contains(text(),'Events count')]"
    main_page_xpath = "//span[contains(text(),'Main page')]"
    super_man_xpath = "//span[contains(text(),'super man')]"
    report_count_xpath = "//div[contains(text(),'Reports count')]"
    
