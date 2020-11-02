
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

import csv
# 検索ソース

source = ['ねずこ','たんじろう','きょうじゅろう','ぎゆう','げんや','かなお','ぜんいつ']

### 検索ツール
        
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    print(word in source)

    if word in source:
        print('います')
    else:
        source.append(word)
        print('いません。追加します。')

    print("{}が見つかりした".format(word))

if __name__ == "__main__":
    search()


with open('source.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(source)

with open('source.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
    

