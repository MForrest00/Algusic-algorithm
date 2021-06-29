import os
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By


interval_mapping = {
    'h': 1,
    'W': 2,
    '(W+h)': 3,
    '(W+W)': 4,
}


def main():
    driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver'))
    driver.get('https://www.scales-chords.com/shscalesbykey.php?skey=C')
    scale_table = driver.find_element(By.CSS_SELECTOR, 'table.scaleinfotable')
    scale_rows = scale_table.find_elements(By.TAG_NAME, 'tr')[1:]
    scale_links_list = list()
    for scale_row in scale_rows:
        scale_links = scale_row.find_elements(By.TAG_NAME, 'a')
        for scale_link in scale_links:
            scale_name = scale_link.text.strip().replace('C ', '').title()
            scale_link = scale_link.get_attribute('href')
            scale_links_list.append({'scale_name': scale_name, 'scale_link': scale_link})
    pprint(scale_links_list)
    existing_intervals = dict()
    scale_data = list()
    for scale_link in scale_links_list:
        driver.get(scale_link['scale_link'])
        data_tables = driver.find_elements(By.CSS_SELECTOR, 'table.scaleinfotable')
        intervals_data = data_tables[1].find_elements(By.TAG_NAME, 'td')[1].find_element(By.TAG_NAME, 'b')
        intervals_text = intervals_data.text.split()
        intervals = list()
        current_interval = 0
        for interval_text in intervals_text[:-1]:
            current_interval += interval_mapping[interval_text]
            intervals.append(current_interval)
        if tuple(intervals) in existing_intervals:
            scale_data[existing_intervals[tuple(intervals)]]['alternative_names'] = \
                scale_data[existing_intervals[tuple(intervals)]].get('alternative_names', []) + \
                [scale_link['scale_name']]
            continue
        chords = list()
        chords_data = data_tables[3].find_elements(By.TAG_NAME, 'span')
        for chord_data in chords_data:
            chords.append(chord_data.text)
        scale_data.append({'scale_name': scale_link['scale_name'], 'intervals': intervals, 'chords': chords})
        existing_intervals[tuple(intervals)] = len(scale_data) - 1
    pprint(scale_data)
    driver.close()
    with open('scales_chords_scale_scrape_output.txt', 'w') as f:
        for scale in scale_data:
            f.write('|'.join([scale['scale_name'], ', '.join(map(str, scale['intervals'])),
                              ', '.join(map(str, scale['chords'])),
                              ', '.join(map(str, scale.get('alternative_names', [])))]) + '\n')


if __name__ == '__main__':
    main()
