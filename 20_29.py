# %%
import re
import pandas as pd
from ast import pattern

import requests

url = 'https://nlp100.github.io/data/jawiki-country.json.gz'
filename = 'jawiki-country.json.gz'
urldata = requests.get(url).content
with open(filename, mode='wb') as f:
    f.write(urldata)
"""まず、jsonのファイルの読み込みから難しい"""
# %%
"""
20. JSONデータの読み込み

    Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

"""
"""jsonをpandasでこれほど無理くりいじくれるのかっていう感じ"""

df = pd.read_json(filename, lines=True)
text = df[df["title"] == "イギリス"]["text"].values
# %%
"""
21. カテゴリ名を含む行を抽出

    記事中でカテゴリ名を宣言している行を抽出せよ．

"""

[x for x in text[0].split() if re.match(r'.*Category', x)]

# %%
"""
22. カテゴリ名の抽出

    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""
[x.lstrip("Category:") for x in text[0].split() if re.match(r'.*Category', x)]

# %%
pattern = r'^.*\[\[Category:(.*)(?:\|.*)?\]\].*$' #(.*?)(?:\|.*)?わからない (?:...) は マッチ後に取り込まれない
result = '\n'.join(re.findall(pattern, text[0], re.MULTILINE))
print(result)

# %%
"""
23. セクション構造

    記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

"""
pattern = r'^(\={2,})\s*(.+?)\s*(\={2,}).*$' #\s*(.+?)\s* is 何
result = '\n'.join(i[1] + ':' + str(len(i[0]) - 1) for i in re.findall(pattern, text[0], re.MULTILINE))
print(result)
# %%
"""
24. ファイル参照の抽出

    記事から参照されているメディアファイルをすべて抜き出せ．

"""
pattern = r'\[\[ファイル:(.+?)\|'
result = '\n'.join(re.findall(pattern, text[0]))
print(result)

# %%
