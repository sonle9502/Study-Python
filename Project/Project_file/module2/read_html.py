from bs4 import BeautifulSoup
import pandas as pd
import os
from utils import dataPath

output_dir = 'C:\\Users\\s-le\\Desktop\\study-private\\Python\\Study-Python\\Project\\Project_file\\datatest'  # Windowsの場合
output_file = os.path.join(output_dir, 'output.csv')
save_dir = 'C:\\Users\\s-le\\Desktop\\study-private\\Python\\Study-Python\\Project\\Project_file\\datatest'

def create_list_element(cards, element ):
    m_list = []
    element = element
    cards = cards
    if element == 'title':
        for card in cards:
            job_title_tag = card.find('div', class_='css-dekpa e37uo190')
            if job_title_tag:
                a_tag = job_title_tag.find('a')
                if a_tag:
                    span_tag = a_tag.find('span')
                    if span_tag:
                        job_title = span_tag.get_text(strip=True)
                        if job_title:
                            m_list.append(job_title)
            else:
                m_list.append(" ")
        return m_list
    elif  element == 'company':
        for card in cards:
            job_title_tag = card.find('div', class_='company_location css-17fky0v e37uo190')
            if job_title_tag:
                span_tag = job_title_tag.find('span',class_ ='css-63koeb eu4oa1w0')
                if span_tag:
                    job_title = span_tag.get_text(strip=True)
                    if job_title:
                        m_list.append(job_title)
            else:
                m_list.append(" ")
        return m_list
    elif  element == 'location':
        for card in cards:
            job_title_tag = card.find('div', class_='company_location css-17fky0v e37uo190')
            if job_title_tag:
                span_tag = job_title_tag.find('div',{'data-testid': 'timing-attribute'})
                if span_tag:
                    text = span_tag.find('div', 'css-10r3o6i eu4oa1w0')
                    if text:
                        text1 = text.get_text(strip=True)
                    else:
                        tmp = job_title_tag.find('div',class_ = 'css-1p0sjhy eu4oa1w0')
                        text1 = tmp.get_text(strip=True)
                    if text1:
                        m_list.append(text1)
            else:
                m_list.append(" ")
        return m_list
    elif  element == 'salary':
        for card in cards:
            job_title_tag = card.find('div', class_='heading6 tapItem-gutter metadataContainer css-z5ecg7 eu4oa1w0')
            if job_title_tag:
                a_tag = job_title_tag.find('div', class_='metadata salary-snippet-container css-5zy3wz eu4oa1w0')
                if a_tag:
                    job_title = a_tag.find('div', class_='css-1cvvo1b eu4oa1w0').get_text(strip=True)
                else:
                    job_title = job_title_tag.find('div', class_='css-1cvvo1b eu4oa1w0').get_text(strip=True)
                if job_title:
                    m_list.append(job_title)
            else:
                m_list.append(" ")
        return m_list
    elif  element == 'contact_type':
        for card in cards:
            job_title_tag = card.find('h2', class_='css-1cvvo1b eu4oa1w0')
            if job_title_tag:
                a_tag = job_title_tag.find('a')
                if a_tag:
                    span_tag = a_tag.find('span')
                    if span_tag:
                        job_title = span_tag.get_text(strip=True)
                        if job_title:
                            m_list.append(job_title)
            else:
                m_list.append(" ")
        return m_list

    
def create_DF(position):
    tile_list = []
    company_list = []
    location_list = []
    salary_list = []
    size = dataPath.count_files_in_folder(position)
    for i in range(1,size):
        file_path = dataPath.create_filepath(position,name = f'output_{i}.html')

        # HTMLファイルを読み込む
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # BeautifulSoupオブジェクトを作成
        soup = BeautifulSoup(html_content, 'lxml')

        cards = soup.find_all('td', class_='resultContent css-1qwrrf0 eu4oa1w0')
        tile_list.extend(create_list_element(cards,'title'))
        company_list.extend(create_list_element(cards, 'company'))
        location_list.extend(create_list_element(cards, 'location'))
        salary_list.extend(create_list_element(cards, 'salary'))
    df = { 'Title': tile_list, 'Company': company_list, 'Location': location_list, 'Salary': salary_list}
    df = pd.DataFrame(df)

    output_csv_folderpath = dataPath.create_folderpath(position)
    output_csv_filepath = os.path.join(output_csv_folderpath,"output.csv")
    # データフレームを指定した場所にCSVファイルとして保存
    df.to_csv(output_csv_filepath, index=False, encoding='utf-8-sig')




# ディレクトリが存在しない場合は作成
# os.makedirs(output_dir, exist_ok=True)
# for card in cards:
#     job_title_tag = card.find('h2', class_='jobTitle css-198pbd eu4oa1w0')
#     if job_title_tag:
#         a_tag = job_title_tag.find('a')
#         if a_tag:
#             span_tag = a_tag.find('span')
#             if span_tag:
#                 job_title = span_tag.get_text(strip=True)
#                 if job_title:
#                     tile_list.append(job_title)
                
# else:
#     tile_list.append(" ")
    #tile_list.append(card.find('h2', class_='jobTitle css-198pbd eu4oa1w0').find('a').find('span').get_text(strip=True))

# company_list.append(card.find('h2', class_='jobTitle css-198pbd eu4oa1w0').find('a').find('span').get_text(strip=True))
# location_list.append(card.find('h2', class_='jobTitle css-198pbd eu4oa1w0').find('a').find('span').get_text(strip=True))

# m_company = card.find(class_ = 'css-63koeb eu4oa1w0').text.stsrip()
# m_location = card.find('span', attrs={'data-testid': 'myJobsStateDate'})

# salary_list.append(card.find( class_='metadata salary-snippet-container css-5zy3wz eu4oa1w0'))
#, 'Company': company_list, 'location' : location_list, 'salary' : salary_list
# # 例として、すべての<h2>タグを選択して、そのテキストを出力する
# for h2_tag in soup.find_all('h2'):
#     print(h2_tag.text)

# # 特定のクラスを持つ<div>タグを選択する例
# for div_tag in soup.find_all('div', class_='specific-class'):
#     print(div_tag.text)

# # id属性が'specific-id'の要素を選択する例
# specific_element = soup.find(id='specific-id')
# if specific_element:
#     print(specific_element.text)

# # タグの属性値を取得する例
# for link in soup.find_all('a'):
#     href = link.get('href')
#     print(href)