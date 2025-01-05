from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import pandas as pd


def corona_information():
    try:
        # COUNTRIES - Request
        response_c = requests.get('https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/')
        soup_c = BeautifulSoup(response_c.text, 'html.parser')

        # HEADER
        head_c = soup_c.find('thead').find_all('th')
        head_c_list = []
        for th in head_c:
            head_c_list.append(th.text)

        # BODY
        body_c = soup_c.find('tbody').find_all('tr')

        body_c_list = []  # create list of lists
        for tr in body_c:
            body_c_item = []
            for tr_info in tr.find_all('td'):
                body_c_item.append(tr_info.text)
            body_c_list.append(body_c_item)

        # The NAME is in the body_c_list with index=1
        name_list = []
        for c in body_c_list:
            name_list.append(c[1])

        # CORONA - Request
        head_corona_list = list()
        body_corona_list = list()
        merged_lists = list()

        run_once = True

        for country_name in name_list[0:20]:
            response = requests.get(f'https://www.worldometers.info/coronavirus/country/{country_name}/')
            soup_country = BeautifulSoup(response.text, 'html.parser')
            assets = soup_country.find_all('div', attrs={'id': 'maincounter-wrap'})

            for i in range(0, 3):
                if run_once:
                    h1 = assets[i].find('h1')
                    head_corona_list.append(h1) if h1 == None else head_corona_list.append(h1.text.strip()[:-1])
            run_once = False
            body_corona = list()
            for div in assets[:-1]:  # there are 4 divs with id=maincounter-wrap for each country
                div_value = div.find('span')
                # <span style="color:#aaa">7,627,186</span> *** needed for all countrys***
                if div_value:
                    body_corona.append(div_value.text.strip())
            body_corona_list.append(body_corona)

            merged_lists = [row1 + row2 for row1, row2 in zip(body_c_list, body_corona_list)]

        head = head_c_list + head_corona_list
        return head, merged_lists

    except HTTPError as error:
        print(error.response.status_code)


head_final, merged_lists_final = corona_information()
print(f'head_final: {head_final}\n', f'merged_final: {merged_lists_final}')
final = pd.DataFrame(merged_lists_final, columns=head_final).drop('#', axis=1)
final.index = range(1, len(final) + 1)
final.to_csv('Countries-final.csv')
