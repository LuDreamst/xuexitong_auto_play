import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

driver = uc.Chrome()
#打开登录页面
driver.get( "https://passport2.chaoxing.com/login" )

# 账号输入框
element_phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "phone"))
)
# 密码输入框
element_pwd = driver.find_element(By.ID, "pwd")
# 登录按钮
element_login_button = driver.find_element(By.ID, "loginBtn")

print( "登录界面加载完成" )

# 键入账号密码并按下登录按钮
actions = ActionChains(driver)
actions.send_keys_to_element(element_phone,"10000000000")
actions.send_keys_to_element(element_pwd,"e9th**********BY")
actions.click(element_login_button)
actions.perform()

print( "登录完成" )
# 等待页面刷新
WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.ID, "frame_content"))
)

# 切换frame到 "我学的课" iframe id=frame_content name=frame_content
driver.switch_to.frame("frame_content")
# 获取课程列表(RawHTML形式）
element_course_list = driver.find_element(By.ID, "courseList")
# 处理 RawHTML
course_list = BeautifulSoup(element_course_list.get_attribute('innerHTML'), features="html.parser")
# 处理结果
cook_course_list = []
# 元组 (name, url)
# 处理过程,提取课程信息
for course in course_list.findAll(name = "li", recursive = False):
  name = course.find("span", attrs={"class": "course-name overHidden2"})["title"]
  url = course.find("a", attrs={"class": "color1"})["href"]
  # TODO: 处理其他信息
  # time = course.find("p", attrs={"class": "margint10 line2"})["title"]
  # teacher = course.find("p", attrs={"class": "line2"})["title"]
  # clazz = course.find("p", attrs={"class": "overHidden1"})
  cook_course_list.append((name, url))

print(cook_course_list)
quit = False

while True:
  time.sleep(1.0)
  if ( quit ):
      break
