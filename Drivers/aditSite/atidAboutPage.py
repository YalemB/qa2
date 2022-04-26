from atidSetUp import *

driver = setUp("about")
# def test_iu_section1():
#     headlight = driver.find_element(By.TAG_NAME, "h1").text
#     assert headlight == "About Us"
#
#     driver.quit()
#
# def test_iu_section2():
#     headlight = driver.find_element(By.XPATH, "//h2[contains(text(),'Who We Are')]").get_attribute("innerText")
#     assert headlight == "Who We Are"
#
#     paragraph = driver.find_element(By.XPATH, "//p[contains(text(),'ATID Demo Store was created by ATID College dedica')]").get_attribute("innerText")
#
#     assert paragraph == "ATID Demo Store was created by ATID College dedicated employees. " \
#                         "This is a complete demo site for practicing QA & Test Automation methodologies." \
#                         " Don't think for a second you can actually buy here something cause you can't ! " \
#                         "This Demo Store contains software bugs which were put intentionally and your job" \
#                         " is to locate them Good luck falks, Yoni Flenner - ATID College"

def test_ui_section3():

    blus_line = driver.find_element(By.XPATH,
                                    "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]")
    blus_line.is_displayed()

    opening = driver.find_element(By.XPATH, "//h4[contains(text(),'A Few Words About')]").get_attribute("innerText")

    assert opening == "A Few Words About"

    team_title = driver.find_element(By.XPATH,"//h2[contains(text(),'Our Team')]").get_attribute("innerText")

    assert team_title == "Our Team"

    paragraph = driver.find_element(By.XPATH, "//p[contains(text(),'We have the best team ever everybody who is somebo')]").get_attribute("innerText")

    assert paragraph == "We have the best team ever everybody who is somebody wants to work with us, " \
                        "so we can afford cherry-picking them, one by one..."

    sec = driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]")
    team = sec.find_elements(By.TAG_NAME, "section")
    # members of the team lists
    x = team[0].text.split("\n")
    y = team[1].text.split("\n")
    l = x + y
    # create dict of member + title
    member_title = {}
    for i in range(0,len(l),2):
        member_title[l[i]] = l[i+1]

    # check if matching to these lists
    names = ['Yoni Flenner', 'Albert Einstein', 'Steve Jobs', 'Bill Gates', 'Kim Kardashian', 'Madonna']
    titles = ['Founder - CEO', 'COO', 'Marketing Head', 'Lead Developer', 'Intern Designer', 'Head of Fun']
    assert  list(member_title.keys()) == names
    assert list(member_title.values()) == titles



    driver.quit()





