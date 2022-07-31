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
season_21_22 = 'https://www.google.com/search?q=la+liga+standings&rlz=1C5CHFA_enUS739US739&oq=la+iga+&aqs=chrome.1.69i57j0i10i433j46i10i433j0i10j46i10i433j69i60l3.2907j0j7&sourceid=chrome&ie=UTF-8#sie=lg;/g/11mqlmppsd;2;/m/09gqx;st;fp;1;;'
season_20_21 = 'https://www.google.com/search?q=la+liga+standings+2021&rlz=1C5CHFA_enUS739US739&oq=la+liga+standings+2021&aqs=chrome..69i57j0i512l4j0i22i30l5.3200j0j9&sourceid=chrome&ie=UTF-8#sie=lg;/g/11j0y2m458;2;/m/09gqx;st;fp;1;;'
season_19_20 = 'https://www.google.com/search?q=la+liga+standings+2020&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsaWptRnw5CpG7w7Kdei2XTYyta4bg%3A1657317276089&ei=nKfIYsH4BNTLkPIPh7-TkAs&ved=0ahUKEwjBtpX8o-r4AhXUJUQIHYffBLIQ4dUDCA4&uact=5&oq=la+liga+standings+2020&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBY6BwgAEEcQsANKBAhBGABKBAhGGABQ7wZYmAdgtgtoAXABeAGAAcACiAHNBJIBBTItMS4xmAEAoAEByAEHwAEB&sclient=gws-wiz#sie=lg;/g/11ff1xzn64;2;/m/09gqx;st;fp;1;;'
season_18_19 = 'https://www.google.com/search?q=la+liga+standings+2019&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsaCYQvkE1qCRyZE24SK1BebXXhjnA%3A1658187883810&ei=a_DVYpyBMfOkqtsPhvC30As&ved=0ahUKEwjc4qOez4P5AhVzkmoFHQb4DboQ4dUDCA4&uact=5&oq=la+liga+standings+2019&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEM6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAFKBAhBGABKBAhGGAFQmQNY7AVgxgZoAXABeACAAYwBiAGMAZIBAzAuMZgBAKABAcgBEcABAdoBBggBEAEYCQ&sclient=gws-wiz#sie=lg;/g/11f57gslw8;2;/m/09gqx;st;fp;1;;'
season_17_18 = 'https://www.google.com/search?q=la+liga+standings+2018&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsb1tnU1ej3vf8s0UZLYAjabVuZpdQ%3A1658187869695&ei=XfDVYoyIKqWkqtsPiNaW6Ag&ved=0ahUKEwjMqsaXz4P5AhUlkmoFHQirBY0Q4dUDCA4&uact=5&oq=la+liga+standings+2018&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBSgQIQRgASgQIRhgBUI8DWKAHYIQIaAFwAXgAgAGSAYgBkgGSAQMwLjGYAQCgAQHIARHAAQHaAQYIARABGAk&sclient=gws-wiz#sie=lg;/g/11c6w1q_2s;2;/m/09gqx;st;fp;1;;'
season_16_17 = 'https://www.google.com/search?q=la+liga+standings+2017&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsbI0rs7VIghrFGH-F0SP49qz0WNPw%3A1658187855653&ei=T_DVYu28J4K1qtsPm92MyAg&ved=0ahUKEwitoO2Qz4P5AhWCmmoFHZsuA4kQ4dUDCA4&uact=5&oq=la+liga+standings+2017&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEM6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAFKBAhBGABKBAhGGAFQ3QNYiwVgoAZoAXABeACAAZMBiAGTAZIBAzAuMZgBAKABAcgBEcABAdoBBggBEAEYCQ&sclient=gws-wiz#sie=lg;/g/11c3ypm39d;2;/m/09gqx;st;fp;1;;'
season_15_16 = 'https://www.google.com/search?q=la+liga+standings+2016&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZbMcLxhrklPp0yNQnqTUWAkwqXoQ%3A1658187841686&ei=QfDVYuq0KfKfqtsPl6uUiAk&ved=0ahUKEwiq2ZiKz4P5AhXyj2oFHZcVBZEQ4dUDCA4&uact=5&oq=la+liga+standings+2016&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEM6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAFKBAhBGABKBAhGGAFQmARYlwZguAdoAXABeACAAYoBiAGKAZIBAzAuMZgBAKABAcgBEcABAdoBBggBEAEYCQ&sclient=gws-wiz#sie=lg;/g/11byqjrmxh;2;/m/09gqx;st;fp;1;;'
season_14_15 = 'https://www.google.com/search?q=la+liga+standings+2015&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZ796roBFxC8KogLylibH-m22QFmw%3A1658187825097&ei=MfDVYoCxBbasqtsPxOiQuAE&ved=0ahUKEwjAjaSCz4P5AhU2lmoFHUQ0BBcQ4dUDCA4&uact=5&oq=la+liga+standings+2015&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBSgQIQRgASgQIRhgBULYDWKMFYKIGaAFwAXgAgAGRAYgBkQGSAQMwLjGYAQCgAQHIARHAAQHaAQYIARABGAk&sclient=gws-wiz#sie=lg;/m/0118q_gx;2;/m/09gqx;st;fp;1;;'
season_13_14 = 'https://www.google.com/search?q=la+liga+standings+2014&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsbhlwXc_7I56ZL8qE7dHHgdE9iFgQ%3A1658187808577&ei=IPDVYubTItWyqtsPmdiHqA0&ved=0ahUKEwjm47P6zoP5AhVVmWoFHRnsAdUQ4dUDCA4&uact=5&oq=la+liga+standings+2014&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToECAAQQ0oECEEYAEoECEYYAVDxA1jzBGCMB2gBcAF4AIABlwGIAakCkgEDMC4ymAEAoAEByAERwAEB2gEGCAEQARgJ&sclient=gws-wiz#sie=lg;/m/0r4zfgy;2;/m/09gqx;st;fp;1;;'
season_12_13 = 'https://www.google.com/search?q=la+liga+standings+2013&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZWJmO8bRa2QAwudkIfFThqHG1jBQ%3A1658187794301&ei=EvDVYrTyEd-jqtsPybahsAQ&ved=0ahUKEwi0w8zzzoP5AhXfkWoFHUlbCEYQ4dUDCA4&uact=5&oq=la+liga+standings+2013&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIFCAAQhgMyBQgAEIYDMgUIABCGAzoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToECAAQQ0oECEEYAEoECEYYAVDqA1ikBGDVCGgBcAF4AIABoQGIAbACkgEDMC4ymAEAoAEByAERwAEB2gEGCAEQARgJ&sclient=gws-wiz#sie=lg;/m/0j9pp1r;2;/m/09gqx;st;fp;1;;'
season_11_12 = 'https://www.google.com/search?q=la+liga+standings+2012&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsZIvWjL7MVGU9enmY2q0pMXFpjiTg%3A1658187715205&ei=w-_VYsmNDLegqtsP7Nyn4Ao&ved=0ahUKEwiJ-_DNzoP5AhU3kGoFHWzuCawQ4dUDCA4&uact=5&oq=la+liga+standings+2012&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToECCMQJ0oECEEYAEoECEYYAVDDA1iqBGDjBmgBcAF4AIABpAGIAa0CkgEDMC4ymAEAoAEByAERwAEB2gEGCAEQARgJ&sclient=gws-wiz#sie=lg;/m/0gkyx89;2;/m/09gqx;st;fp;1;;'
season_10_11 = 'https://www.google.com/search?q=la+liga+standings+2011&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsb-HvbW3qvE-Ke9DJy26fsnbFBpQg%3A1658187732065&ei=1O_VYuO8A7OqqtsPjMatiAY&ved=0ahUKEwjj9vXVzoP5AhUzlWoFHQxjC2EQ4dUDCA4&uact=5&oq=la+liga+standings+2011&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIFCAAQhgMyBQgAEIYDMgUIABCGAzoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYAToECAAQQ0oECEEYAEoECEYYAVCyDVjYDWCZEWgBcAF4AIAB8AGIAccDkgEDMi0ymAEAoAEByAERwAEB2gEGCAEQARgJ&sclient=gws-wiz#sie=lg;/m/0bs5lcl;2;/m/09gqx;st;fp;1;;'
season_09_10 = 'https://www.google.com/search?q=la+liga+standings+2010&rlz=1C5CHFA_enUS739US739&sxsrf=ALiCzsbzSEMoKfjZ8ATxmerHIItACf-rbA%3A1658187133689&ei=fe3VYtTMKce2qtsP5oaDqAQ&ved=0ahUKEwiU_8u4zIP5AhVHm2oFHWbDAEUQ4dUDCA4&uact=5&oq=la+liga+standings+2010&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBQgAEIYDMgUIABCGAzIFCAAQhgMyBQgAEIYDOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOgQIIxAnOgQIABBDSgQIQRgASgQIRhgBUJrVAljc2gJggt0CaAJwAXgAgAF7iAGqA5IBAzEuM5gBAKABAcgBEcABAdoBBggBEAEYCQ&sclient=gws-wiz#sie=lg;/m/05_5ptc;2;/m/09gqx;st;fp;1;;'
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

	# Fill season and rank columns
	for i in range(num_teams):
		tmp_str = str(curr_season + 1)
		if dictionary[season_header] == None:
			dictionary[season_header] = [str(curr_season) + '-' + tmp_str[-2:]]
			dictionary[rank_header] = [i + add_1]
		else:
			dictionary[season_header].append(str(curr_season) + '-' + tmp_str[-2:])
			dictionary[rank_header].append(i + add_1)

	# Open website
	DRIVER_PATH = Service('/Users/Nicholas/Desktop/chromedriver')
	driver = webdriver.Chrome(options=options, service=DRIVER_PATH)
	driver.get(league_url)
	sleep(5)

	# Fill club name column
	teams_elements = driver.find_elements(by=By.XPATH, value="//span[@class='ellipsisize hsKSJe']")
	for i in teams_elements:
		if dictionary[club_header] == None:
			dictionary[club_header] = [i.text]
		elif i.text != '':
			dictionary[club_header].append(i.text)

	# Add first team in league (only because Google soccer standings HTML is weird)
	first_elements = driver.find_elements(by=By.XPATH, value="//td[@class='e9fBA xkW0Cc snctkc xL0E7c']")
	if dictionary[pts_header] == None:
		dictionary[pts_header] = [first_elements[skip_3].text]
	else:
		dictionary[pts_header].append(first_elements[skip_3].text)

	# Add all middle elements to club points column
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

	# Add last club points to column (also b/c Google soccer standings HTML is weird)
	last_elements = driver.find_elements(by=By.XPATH, value="//td[@class='e9fBA xkW0Cc snctkc bWoKCf']")
	dictionary[pts_header].append(last_elements[skip_3].text)

	# Close chromedriver (website)
	driver.quit()

# Main

# Call function and add to global season variable so that seasons column changes appropriately
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

# Create csv file, output and name
df = pd.DataFrame(dictionary)
df.to_csv('la_liga_table.csv', index=False)
