from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# URL dos Exoplanetas da NASA
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)
headers = ["name", "light_years_from_earth", 'planet_mass', 'stellar_magnitude', 'discovery_date', 
        'hyperlink', 'planet_type', 'planet_radius', 'orbital_radius', 'orbital_period', 'eccentricity']

planet_data = []
new_planet_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    
    ## ADICIONE O CÓDIGO AQUI ##
    try: 
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, 'html.parser')
        temp_list = []

        for tr_tag in soup.find_all('tr', attrs={'class': 'fact_row'}):
            td_tags = tr_tag.find_all('td')
            for td_tag in td_tags:
                try: 
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")

        new_planet_data.append(temp_list)

    except: 
        time.sleep(1)
        scrape_more_data(hyperlink)

scrape()
for index, data in enumerate (planet_data):
    scrape_more_data(data[5])
    print(f'{index+1} page done 2')

final_planet_data = []
for index, data in enumerate (planet_data):
    new_planet_data_element = new_planet_data[index]
    new_planet_data_element = [elem.replace("/n", "") for elem in new_planet_data_element]
    new_planet_data_element = new_planet_data_element[:7]
    new_planet_data.append(data + new_planet_data_element)

with open("final.csv", "w") as f:
    cvswriter = csv.writer(f)
    cvswriter = writerow(headers)
    cvswriter.writerows(final_planet_data)


planet_df_1 = pd.read_csv("updated_scraped_data.csv")

# Chame o método
for index, row in planet_df_1.iterrows():

    ## ADICIONE O CÓDIGO AQUI ##

     # Call scrape_more_data(<hyperlink>)

    print(f"Coleta de dados do hyperlink {index+1} concluída")

print(new_planets_data)

# Remova o caractere '\n' dos dados coletados
scraped_data = []

for row in new_planets_data:
    replaced = []
    ## ADICIONE O CÓDIGO AQUI ##


    
    scraped_data.append(replaced)

print(scraped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scrapped_data,columns = headers)

# Converta para CSV
new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
