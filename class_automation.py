import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

#Subjects and Subjest codes
subjets = {1: {'name': 'APPLICATION SECURITY', 'number': '2', 'id': 'course-link-_5721_1'},
           2: {'name': 'APPLICATION SECURITY LAB', 'number': '3', 'id': 'course-link-_5741_1'},
           3: {'name': 'APTITUDE-WORKSHOP', 'number': '4', 'id': 'course-link-_9760_1'},
           4: {'name': 'APTITUDE', 'number': '5', 'id': 'course-link-_6420_1'},
           5: {'name': 'COMPUTER NETWORKS', 'number': '6', 'id': 'course-link-_5724_1'},
           6: {'name': 'COMPUTER NETWORKS LAB', 'number': '7', 'id': 'course-link-_5743_1'},
           7: {'name': 'SECURITY AND CRPYTOGRAPHY', 'number': '8', 'id': 'course-link-_5722_1'},
           8: {'name': 'SECURITY AND CRPYTOGRAPHY LAB', 'number': '9', 'id': 'course-link-_5740_1'},
           9: {'name': 'SECURITY INTELLGENCE', 'number': '10', 'id': 'course-link-_5723_1'},
           10: {'name': 'SECURITY INTELLGENCE LAB', 'number': '11', 'id': 'course-link-_5742_1'},
           11: {'name': 'SOFT SKILLS', 'number': '12', 'id': 'course-link-_5738_1'},
           12: {'name': 'SYSTEM PROGRAMMING', 'number': '13', 'id': 'course-link-_5720_1'},
           13: {'name': 'SYSTEM PROGRAMMING LAB', 'number': '14', 'id': 'course-link-_5739_1'},
           14: {'name': 'SOFT SKILLS-WORKSHOP', 'number': '15', 'id': 'course-link-_9639_1'}}
#Timings of the classes
shedule_time = ['09:45:00','10:45:00','11:45:00','12:45:00','13:30:00','20:00:00','20:30:00', '15:35:00']

#Path to the Browser
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.maximize_window()

def blackboard():
	#Login for the BlackBoard
	driver.get("https://cuchd.blackboard.com/")
	time.sleep(1)
	driver.find_element_by_class_name("button-1").click()
	driver.find_element_by_id("user_id").send_keys('18BCS3523')
	driver.find_element_by_id("password").send_keys('9007@Tjc10')
	driver.find_element_by_id("entry-login").click()
	time.sleep(3)

def start_class(time_table):
    # Attending the classes
    # Path upto classes -------------------------/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/----v-/bb-base-course-card/div[1]/div[2]/a/h4
    for x in range(0,7):
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time >= shedule_time[x] and current_time <= shedule_time[x + 1] and time_table[x] != 0:
            class_path = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[" +
                subjets[time_table[x]]['number'] + "]/bb-base-course-card/div[1]/div[2]/a/h4")
            driver.execute_script("arguments[0].scrollIntoView(true)", class_path)
            time.sleep(3)
            class_path = driver.find_element_by_xpath("//*[@id='" + subjets[time_table[x]]['id'] + "']/h4")
            driver.execute_script("arguments[0].scrollIntoView(true)", class_path)
            class_path.click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="sessions-list-dropdown"]/span').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="sessions-list"]/li[1]/a/span').click()
            time.sleep(200)
            driver.switch_to.alert.accept()  # This will allow the access
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[2]/button').click()
            time.sleep(3)
            driver.switch_to.alert.accept()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[2]/button').click()
            while True:
                time.sleep(1)
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                if current_time >= shedule_time[x + 1] and time_table[x] != 3 and time_table[x] != 14:
                    time.sleep(10)
                    break;
                elif current_time >= shedule_time[x + 2]:
                    time.sleep(10)
                    break;
            driver.switch_to.window(driver.window_handles[1])
            driver.close()


  
if __name__=="__main__":
    print("//////////////////////////////////")
    print("////// --CLASS AUTOMATION-- //////")
    print("//////////////////////////////////\n\n")
    print("S.No     Subjects")
    for x in range(1, 15):
        print(" {:<7} {:<8}".format(x, subjets[x]['name']))
    print("\n\nEnter the Shedule~~~~~~~~~~vvvvvvvvv")
    list = [int(item) for item in input("Enter the list items : ").split()] 
    print("Today's Shedule : ")
    for x in list:
        if x != 0:
            print(subjets[x]['name'])
    blackboard()
    start_class(list)