from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# Macros
add_1 = 1
el = 'https://en.wikipedia.org/wiki/List_of_UEFA_Cup_and_Europa_League_finals'

dictionary = {}

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

def extract_el_data(el_url):
	seasons = []
	winners = []
	runner_ups = []
	year_oldest_season = 2009
	year_oldest_season_str = str(year_oldest_season)
	current_year = 2022
	season_header = 'EL Season'
	club_header = 'EL Winner'
	runner_up_header = 'EL Runner-Up'

	DRIVER_PATH = Service('/Users/Nicholas/Desktop/chromedriver')
	driver = webdriver.Chrome(options=options, service=DRIVER_PATH)
	driver.get(el_url)
	sleep(5)

	while year_oldest_season < current_year:
		value_str = "//a[@title='" + str(year_oldest_season) + "–" + str(int(year_oldest_season_str[-2:]) + add_1) + " UEFA Europa League']"
		seasons.append(driver.find_element(by=By.XPATH, value=value_str).text)
		year_oldest_season += 1
		year_oldest_season_str = str(year_oldest_season)

	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Atlético Madrid']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='FC Porto']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Atlético Madrid']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Chelsea F.C.']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Sevilla FC']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Sevilla FC']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Sevilla FC']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Manchester United F.C.']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Atlético Madrid']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Chelsea F.C.']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Sevilla FC']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Villarreal CF']").text)
	winners.append(driver.find_element(by=By.XPATH, value="//a[@title='Eintracht Frankfurt']").text)

	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='Fulham F.C.']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='S.C. Braga']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='Athletic Bilbao']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='S.L. Benfica']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='S.L. Benfica']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='FC Dnipro']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='Liverpool F.C.']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='AFC Ajax']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='Olympique de Marseille']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='Arsenal F.C.']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='Inter Milan']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='Manchester United F.C.']").text)
	runner_ups.append(driver.find_element(by=By.XPATH, value="//a[@title='Rangers F.C.']").text)

	dictionary[season_header] = seasons
	dictionary[club_header] = winners
	dictionary[runner_up_header] = runner_ups

	driver.quit()

# Main
extract_el_data(el)

df = pd.DataFrame(dictionary)
df.to_csv('table.csv')