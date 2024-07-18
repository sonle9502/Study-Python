from bs4 import BeautifulSoup
import pandas as pd
import os

output_dir = 'C:\\Users\\s-le\\Desktop\\study-private\\Python\\Study-Python\\Project\\Project_file\\data'  # Windowsの場合
output_file = os.path.join(output_dir, 'output.csv')
# HTMLファイルを読み込む
with open('C:\\Users\\s-le\\Desktop\\study-private\\Python\\Study-Python\\Project\\Project_file\\data\\output.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html_content, 'lxml')

cards = soup.find_all(class_ = 'resultContent css-1qwrrf0 eu4oa1w0')
tile_list = []
company_list = []
location_list = []
for card in cards:
    tile_list.append(card.find('h2').span.text.strip())
    company_list.append(card.find(class_ = 'css-63koeb eu4oa1w0').text.strip())
    location_list.append(card.find( class_='css-10r3o6i eu4oa1w0'))
data = { 'Title': tile_list, 'Company': company_list, 'location' : location_list}
df = pd.DataFrame(data)

# ディレクトリが存在しない場合は作成
os.makedirs(output_dir, exist_ok=True)

# データフレームを指定した場所にCSVファイルとして保存
df.to_csv(output_file, index=False, encoding='utf-8-sig')






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