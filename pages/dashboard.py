from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath ="//*[@id='login']"
    player_count_xpath = "//body/div[@id='__next']/div[1]/main[1]/div[2]/div[1]/div[1]"
    dev_team_contact_xpath = "//span[contains(text(),'Dev team contact')]"
    super_man_xpath = "//body[1]/div[1]/div[1]/main[1]/div[3]/div[3]/div[1]/div[1]/a[1]/button[1]/span[1]"
    polski_xpath = "//span[contains(text(),'Polski')]"
    sing_out_xpath = "//span[contains(text(),'Sign out')]"
    scouts_panels_xpath = "//h6[contains(text(),'Scouts Panel')]"
    players_xpath = "//span[contains(text(),'Players')]"
    add_player_xpath = "//span[contains(text(),'Add player')]"
    events_count_xpath = "//div[contains(text(),'Events count')]"
    main_page_xpath = "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/ul[1]/div[1]/div[1]"
    super_man_xpath = "//span[contains(text(),'super man')]"
    report_count_xpath = "//div[contains(text(),'Reports count')]"
    