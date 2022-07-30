from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# Macros
num_teams = 20
skip_3 = 3
num_middle_elements = 18
first_line_edge_case = 3
middle_element_3rd_index = 3
add_1 = 1
jump_to_4th = 4
# These are different so that dictionary keys (which later turn into Excel headers) are different, otherwise keys will overwrite
curr_season = 2009
ZERO = 0
season_21_22 = 'https://www.google.com/search?q=premier+league+standings+2021-22&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsY1YbE2jG5ivkJ2WTGrZlZRPtvBJQ%3A1658352805722&ei=pXTYYsTIK4W5qtsP3KyEiAU&ved=0ahUKEwiEr5bPtYj5AhWFnGoFHVwWAVEQ4dUDCA4&uact=5&oq=premier+league+standings+2021-22&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWOgcIIxCwAxAnOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOgwILhDIAxCwAxBDGAI6DwguENQCEMgDELADEEMYAjoECCMQJ0oECEEYAEoECEYYAVCjCFjOM2DWOGgBcAF4AIAB3wGIAYgIkgEFMi41LjGYAQCgAQHIARPAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz#sie=lg;/g/11p44qhs93;2;/m/02_tc;st;fp;1;;'
season_20_21 = 'https://www.google.com/search?q=premier+league+standings+2021&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsYA8cECyVoGpPnGejO4UWJboKx8Fw%3A1658351641089&ei=GXDYYqn0BJnDkPIP5-ikaA&ved=0ahUKEwjp5OqjsYj5AhWZIUQIHWc0CQ0Q4dUDCA4&uact=5&oq=premier+league+standings+2021&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEIAEMgUIABCABDIECAAQQzIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToMCC4QyAMQsAMQQxgCSgQIQRgASgQIRhgBUJEDWOwDYOEFaAFwAXgAgAGoAYgBvQKSAQMwLjKYAQCgAQHIARPAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz#sie=lg;/g/11j4y8fvpd;2;/m/02_tc;st;fp;1;;'
season_19_20 = 'https://www.google.com/search?q=premier+league+standings+2020&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsbmvY57R7zFyorkL8Ir5WYEph23PQ%3A1658351609274&ei=-W_YYrafEIvAkPIPx5iWmA0&ved=0ahUKEwj2_9SUsYj5AhULIEQIHUeMBdMQ4dUDCA4&uact=5&oq=premier+league+standings+2020&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBY6CggAEEcQsAMQiwM6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAE6DAguEMgDELADEEMYAjoICAAQgAQQsQM6BAgAEENKBAhBGABKBAhGGAFQ1QJY4AZguAloAXABeACAAbEBiAHpBJIBAzAuNJgBAKABAcgBE7gBAsABAdoBBggBEAEYCdoBBggCEAEYCA&sclient=gws-wiz#sie=lg;/g/11fj6snmjm;2;/m/02_tc;st;fp;1;;'
season_18_19 = 'https://www.google.com/search?q=premier+league+standings+2019&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZVnpO9OKnXLblLJcXo5upFta-vLQ%3A1658351593495&ei=6W_YYuX6HfXRkPIPveufiAc&ved=0ahUKEwilk5KNsYj5AhX1KEQIHb31B3EQ4dUDCA4&uact=5&oq=premier+league+standings+2019&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAEIAEMgUIABCABDoKCAAQRxCwAxCLAzoHCAAQRxCwAzoKCAAQsAMQQxCLAzoKCC4QsAMQQxCLAzoNCAAQ5AIQsAMQiwMYAUoECEEYAEoECEYYAVCUAliTBmDrBmgBcAF4AIABzAGIAcwBkgEDMi0xmAEAoAEByAERuAECwAEB2gEGCAEQARgJ&sclient=gws-wiz#sie=lg;/g/11f60x_ln9;2;/m/02_tc;st;fp;1;;'
season_17_18 = 'https://www.google.com/search?q=premier+league+standings+2018&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsamfkHP-6OfF6voJ6WEJ7khEeUavg%3A1658351575128&ei=12_YYsWsB7rGkPIPwpSXuA4&ved=0ahUKEwiF9LCEsYj5AhU6I0QIHULKBecQ4dUDCA4&uact=5&oq=premier+league+standings+2018&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgUIABCABDIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOgQIIxAnSgQIQRgASgQIRhgBUJEEWL8GYJsIaAFwAXgAgAGlAYgBtwKSAQMwLjKYAQCgAQHIARHAAQHaAQYIARABGAk&sclient=gws-wiz#sie=lg;/g/11c74zg7g7;2;/m/02_tc;st;fp;1;;'
season_16_17 = 'https://www.google.com/search?q=premier+league+standings+2017&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZmcRz-TYrKFyqJ4LSlyj06D5AphA%3A1658351558275&ei=xm_YYr6uEMTPkPIP7qSigAU&ved=0ahUKEwi-qaz8sIj5AhXEJ0QIHW6SCFAQ4dUDCA4&uact=5&oq=premier+league+standings+2017&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAEIAEOgoIABBHELADEIsDOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBSgQIQRgASgQIRhgBUJsHWO8KYPcLaAFwAXgAgAGVAYgBlQGSAQMwLjGYAQCgAQHIARG4AQLAAQHaAQYIARABGAk&sclient=gws-wiz#sie=lg;/g/11c3yptrz5;2;/m/02_tc;st;fp;1;;'
season_15_16 = 'https://www.google.com/search?q=premier+league+standings+2016&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZH6nhIBOyNHl_ihpk7bt7ZEDfW1w%3A1658351541518&ei=tW_YYtyGH_6ckPIP3sqVyAc&ved=0ahUKEwicta30sIj5AhV-DkQIHV5lBXkQ4dUDCA4&uact=5&oq=premier+league+standings+2016&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgUIABCABDIGCAAQHhAWMggIABAeEA8QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBY6CggAEEcQsAMQiwM6BwgAEEcQsAM6CggAELADEEMQiwM6DQgAEOQCELADEIsDGAE6BAgjECdKBAhBGABKBAhGGAFQjQVY2gVgqApoAXABeACAAZsBiAGrApIBAzAuMpgBAKABAcgBEbgBAsABAdoBBggBEAEYCQ&sclient=gws-wiz#sie=lg;/m/012vp1qy;2;/m/02_tc;st;fp;1;;'
season_14_15 = 'https://www.google.com/search?q=premier+league+standings+2015&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsbc_kakwBtA2QT27pC1D6x8Ivb41Q%3A1658351496728&ei=iG_YYoz0K_vLkPIPm-imcA&ved=0ahUKEwiM2P_esIj5AhX7JUQIHRu0CQ4Q4dUDCA4&uact=5&oq=premier+league+standings+2015&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgUIABCABDIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOgQIIxAnSgQIQRgASgQIRhgBUKYEWLoFYIEHaAFwAXgAgAGgAYgBtwKSAQMwLjKYAQCgAQHIARHAAQHaAQYIARABGAk&sclient=gws-wiz#sie=lg;/m/0_v76q8;2;/m/02_tc;st;fp;1;;'
season_13_14 = 'https://www.google.com/search?q=premier+league+standings+2014&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsY6gI5TShPxQ85QAxnCaINCnfweMQ%3A1658351459526&ei=Y2_YYsvfH6bVkPIPx-SXqAU&ved=0ahUKEwiLnaHNsIj5AhWmKkQIHUfyBVUQ4dUDCA4&uact=5&oq=premier+league+standings+2014&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgUIABCABDIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIICAAQHhAPEBY6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAE6BAgjECdKBAhBGABKBAhGGAFQnwRY8ARg3ApoAXABeACAAZcBiAGhApIBAzAuMpgBAKABAcgBEcABAdoBBggBEAEYCQ&sclient=gws-wiz#sie=lg;/m/0r4t7p1;2;/m/02_tc;st;fp;1;;'
season_12_13 = 'https://www.google.com/search?q=premier+league+standings+2013&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZk-DfZ2kI9jTTsnupu_9_xOmaQHQ%3A1658351412842&ei=NG_YYsjqMubXkPIPkeY-&ved=0ahUKEwjI1P-2sIj5AhXmK0QIHRGzDwAQ4dUDCA4&uact=5&oq=premier+league+standings+2013&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToECCMQJ0oECEEYAEoECEYYAVDXA1izBGClBmgBcAF4AIABnwGIAa8CkgEDMC4ymAEAoAEByAERwAEB2gEGCAEQARgJ&sclient=gws-wiz#sie=lg;/m/0h564kc;2;/m/02_tc;st;fp;1;;'
season_11_12 = 'https://www.google.com/search?q=premier+league+standings+2012&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsaX59Qrg6cuOqKJxyzmbKAcGOyMng%3A1658351361742&ei=AW_YYuLWLLOZkPIP0LO2wA0&ved=0ahUKEwii29CesIj5AhWzDEQIHdCZDdgQ4dUDCA4&uact=5&oq=premier+league+standings+2012&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToECCMQJ0oECEEYAEoECEYYAVD_A1i4BGCXBmgBcAF4AIABowGIAbcCkgEDMC4ymAEAoAEByAERwAEB2gEGCAEQARgJ&sclient=gws-wiz#sie=lg;/m/0gkzcwr;2;/m/02_tc;st;fp;1;;'
season_10_11 = 'https://www.google.com/search?q=premier+league+standings+2011&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZjnHWRFfLYArk2_56_s2MX1i_5rA%3A1658351107548&ei=A27YYoz7IOCfkPIPlveWyAY&ved=0ahUKEwjMiLalr4j5AhXgD0QIHZa7BWkQ4dUDCA4&uact=5&oq=premier+league+standings+2011&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToECCMQJ0oECEEYAEoECEYYAVC0A1j_A2DRCGgBcAF4AIABnQGIAbcCkgEDMC4ymAEAoAEByAERwAEB2gEGCAEQARgJ&sclient=gws-wiz#sie=lg;/m/0bh9196;2;/m/02_tc;st;fp;1;;'
season_09_10 = 'https://www.google.com/search?q=premier+league+standings+2010&rlz=1C5CHFA_enUS739US739&oq=premier+league+standings+2010&aqs=chrome..69i57j0i512l9.10814j0j7&sourceid=chrome&ie=UTF-8#sie=lg;/m/05c25w5;2;/m/02_tc;st;fp;1;;'
club_header = 'Club'
pts_header = 'Pts'
rank_header = 'Rank'
season_header = 'Season'

dictionary = {}
dictionary[season_header] = None
dictionary[rank_header] = None
dictionary[club_header] = None
dictionary[pts_header] = None

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# Extract both La Liga and Premier League standings data
def extract_league_data(league_url):
	teams = []
	pts = []
	rank = []
	season = []

	for i in range(num_teams):
		tmp_str = str(curr_season + 1)
		if dictionary[season_header] == None:
			dictionary[season_header] = [str(curr_season) + '-' + tmp_str[-2:]]
			dictionary[rank_header] = [i + add_1]
		else:
			dictionary[season_header].append(str(curr_season) + '-' + tmp_str[-2:])
			dictionary[rank_header].append(i + add_1)

	DRIVER_PATH = Service('/Users/Nicholas/Desktop/chromedriver')
	driver = webdriver.Chrome(options=options, service=DRIVER_PATH)
	driver.get(league_url)
	sleep(5)

	teams_elements = driver.find_elements(by=By.XPATH, value="//span[@class='ellipsisize hsKSJe']")
	for i in teams_elements:
		if dictionary[club_header] == None:
			dictionary[club_header] = [i.text]
		elif i.text != '':
			dictionary[club_header].append(i.text)

	first_elements = driver.find_elements(by=By.XPATH, value="//td[@class='e9fBA xkW0Cc snctkc xL0E7c']")
	if dictionary[pts_header] == None:
		dictionary[pts_header] = [first_elements[skip_3].text]
	else:
		dictionary[pts_header].append(first_elements[skip_3].text)

	middle_elements = driver.find_elements(by=By.XPATH, value="//td[@class='e9fBA xkW0Cc snctkc']")

	for i, value in enumerate(middle_elements):
		if len(pts) <= num_middle_elements:
			if i <= first_line_edge_case:
				if i == middle_element_3rd_index:
					single_element = value.text
					dictionary[pts_header].append(single_element)
				continue
			if (((i + add_1) % jump_to_4th) == 0 and value.text != ''):
				single_element = value.text
				dictionary[pts_header].append(single_element)

	last_elements = driver.find_elements(by=By.XPATH, value="//td[@class='e9fBA xkW0Cc snctkc bWoKCf']")
	dictionary[pts_header].append(last_elements[skip_3].text)

	driver.quit()

# Main
extract_league_data(season_09_10)
curr_season += 1
extract_league_data(season_10_11)
curr_season += 1
extract_league_data(season_11_12)
curr_season += 1
extract_league_data(season_12_13)
curr_season += 1
extract_league_data(season_13_14)
curr_season += 1
extract_league_data(season_14_15)
curr_season += 1
extract_league_data(season_15_16)
curr_season += 1
extract_league_data(season_16_17)
curr_season += 1
extract_league_data(season_17_18)
curr_season += 1
extract_league_data(season_18_19)
curr_season += 1
extract_league_data(season_19_20)
curr_season += 1
extract_league_data(season_20_21)
curr_season += 1
extract_league_data(season_21_22)

df = pd.DataFrame(dictionary)

df.to_csv('premier_league_table.csv', index=False)