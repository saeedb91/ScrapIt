from selenium import webdriver

# Open up a Firefox browser and navigate to web page.
driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in")

#Get the username and password field element
username = driver.find_element_by_xpath('//input[@id="session_key-login"]')
password = driver.find_element_by_xpath('//input[@id="session_password-login"]')

#IMPORTANT
username.send_keys('Enter Your Username Here')
password.send_keys('Enter Your Password Here')

#click on the submit button
driver.find_element_by_xpath('//input[@id="btn-primary"]').click()

#Get the job, names and country field element
job = driver.find_elements_by_xpath('//p[@class="subline-level-1 Sans-15px-black-85% search-result__truncate"]')
names = driver.find_elements_by_xpath('//span[@class="name actor-name"]')
country = driver.find_elements_by_xpath('//p[@class="subline-level-2 Sans-13px-black-55% search-result__truncate"]')

#Print all the list for each of job, names and country
num_page_items = len(names)
for i in range(num_page_items):
    print(names[i].text + " : " + job[i].text + " : " + country)

# Clean up (close browser once completed task).
#driver.close()
