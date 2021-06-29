import os
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver'))
    i = 1
    chord_data = list()
    while True:
        driver.get('https://www.scales-chords.com/showchbykey.php?key=C&page={}'.format(i))
        chord_table = driver.find_element(By.CSS_SELECTOR, 'table.scaleinfotable')
        chord_rows = chord_table.find_elements(By.TAG_NAME, 'tr')
        if len(chord_rows) == 1:
            break
        chord_links_list = list()
        for chord_row in chord_rows[1:]:
            chord_link = chord_row.find_element(By.TAG_NAME, 'a').get_attribute('href')
            chord_links_list.append(chord_link)
        pprint(chord_links_list)
        page_chord_data = list()
        for chord_link in chord_links_list:
            driver.get(chord_link)
            info_table = driver.find_element(By.CSS_SELECTOR, 'table.chordinfotable')
            info_table_rows = info_table.find_elements(By.TAG_NAME, 'tr')
            chord_name_data = info_table_rows[0].find_elements(By.TAG_NAME, 'td')[1].text.strip().split(' (C ')
            chord_symbol = chord_name_data[0].strip()
            if len(chord_name_data) == 2:
                chord_name = chord_name_data[1].strip(')').title()
            else:
                chord_name = ''
            intervals_data = \
                info_table_rows[2].find_elements(By.TAG_NAME, 'td')[1].text.strip().split(' (')[1].split(')')[0].split()
            j = 3
            while j < len(info_table_rows):
                if info_table_rows[j].find_elements(By.TAG_NAME, 'td')[0].text.strip().lower() == 'other notations':
                    other_notations = info_table_rows[j].find_elements(By.TAG_NAME, 'td')[1].text.split()
                    break
                j += 1
            else:
                other_notations = list()
            page_chord_data.append({
                'chord_symbol': chord_symbol,
                'chord_name': chord_name,
                'intervals_data': intervals_data,
                'other_notations': other_notations,
            })
        chord_data.extend(page_chord_data)
        i += 1
    pprint(chord_data)
    driver.close()
    with open('scales_chords_chord_scrape_output.txt', 'w') as f:
        for chord in chord_data:
            f.write('|'.join([chord['chord_symbol'], chord['chord_name'], ', '.join(chord['intervals_data']),
                              ', '.join(chord['other_notations'])]) + '\n')


if __name__ == '__main__':
    main()
