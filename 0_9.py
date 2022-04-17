# %%
"""
00. 文字列の逆順

    文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""
import random
import re

str_0 = "stressed"
str_0_ans = str_0[::-1]
print(str_0_ans)
# %%
"""
01. 「パタトクカシーー」

    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""
str_1 = "パタトクカシーー"
str_1_ans = [str for i, str in enumerate(str_1) if i % 2 == 0]
str_1_ans = "".join(str_1_ans)
print(str_1_ans)
"""
模範解答
確かに
"""
str = 'パタトクカシーー'
ans = str[::2]  # 「先頭」から「末尾」まで「移動幅2」で

print(ans)
# %%
"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

"""
str_2_pa = "パトカー"
str_2_ta = "タクシー"
str_2_ans = [str_pa + str_ta for str_pa, str_ta in zip(str_2_pa, str_2_ta)]
str_2_ans = "".join(str_2_ans)
print(str_2_ans)
# %%
"""
03. 円周率

    “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    答えみた
"""

str_4 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str_4 = re.sub("[,\.]", "", str_4)
list_4 = str_4.split()
print([len(val) for val in list_4])
# %%
"""
04. 元素記号
“Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. 
Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の
単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した
文字列から単語の位置（先頭から何番目の単語か）への連想配列
（辞書型もしくはマップ型）を作成せよ．
答えみた
else使うのとenumerate出てこなかった
"""
str_5 = ("Hi He Lied Because Boron Could"
         " Not Oxidize Fluorine. New Nations "
         "Might Also Sign Peace"
         " Security Clause. Arthur King Can.")
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
str_5 = re.sub("[.\,]", "", str_5)
str_list_5 = str_5.split()
ans_5 = {}
for i, word in enumerate(str_list_5):
    if i + 1 in num_list:
        ans_5[i + 1] = word[:1]
    else:
        ans_5[i + 1] = word[:2]
print(ans_5)
# %%
"""
05. n-gram
与えられたシーケンス（文字列やリストなど）
からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から
単語bi-gram，文字bi-gramを得よ．
問題の意味がよく分からなかった。
"""


def ngram(n, lst):
    # ex.
    # [str[i:] for i in range(2)] -> ['I am an NLPer', ' am an NLPer']
    # zip(*[str[i:] for i in range(2)]) -> zip('I am an NLPer', ' am an NLPer')
    return list(zip(*[lst[i:] for i in range(n)]))
    """
    list(zip(*list))が少しみない書き方なので、
    一応
    list(zip(*["ab", "cd", "ef"]))
    """


str_6 = 'I am an NLPer'
words_bi_gram = ngram(2, str_6.split())
chars_bi_gram = ngram(2, str_6)

print('単語bi-gram:', words_bi_gram)
print('文字bi-gram:', chars_bi_gram)
# %%
"""
06. 集合

    “paraparaparadise”と”paragraph”に含まれる文字bi-gramの
    集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を
    求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

    和集合とかの求めからわからない
"""


def n_gram(n, str):
    return list(zip(*[str[i:] for i in range(n)]))


str_7_a = "paraparaparadise"
str_7_b = "paragraph"

X = set(n_gram(2, str_7_a))  # setで重複削除
Y = set(n_gram(2, str_7_b))

union = X | Y
intersection = X & Y
difference = X - Y

print('X:', X)
print('Y:', Y)
print('和集合:', union)
print('積集合:', intersection)
print('差集合:', difference)
print('Xにseが含まれるか:', {('s', 'e')} <= X)
print('Yにseが含まれるか:', {('s', 'e')} <= Y)

# %%


def return_tamplate(x, y, z):
    return f"{x}時の{y}は{z}"


print(return_tamplate(12, "気温", 22.4))

# %%
"""
08. 暗号文

    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．

    文字コード苦手で無理だった
"""


def cipher(str):
    rep = [chr(219 - ord(x)) if x.islower() else x for x in str]

    return ''.join(rep)


message = 'the quick brown fox jumps over the lazy dog'
message = cipher(message)
print('暗号化:', message)
message = cipher(message)
print('復号化:', message)

"""おもしろい"""


def chr_ord_al(alpha):
    alpha_ord = ord(alpha)
    diff_alpha_ord = 219 - alpha_ord
    diff_alpha_chr = chr(diff_alpha_ord)
    re_alpha_ord = 219 - diff_alpha_ord
    re_alpha_chr = chr(re_alpha_ord)
    print(alpha, alpha_ord, diff_alpha_ord,
          diff_alpha_chr, re_alpha_ord, re_alpha_chr)


chr_ord_al("b")
chr_ord_al("d")
# %%
"""
09. Typoglycemia

    スペースで区切られた単語列に対して，
    各単語の先頭と末尾の文字は残し，
    それ以外の文字の順序をランダムに並び替える
    プログラムを作成せよ．
    ただし，長さが４以下の単語は並び替えないこととする．
    適当な英語の文
    （例えば”I couldn’t believe that I could actually understand 
    what I was reading : the phenomenal power of the human mind .”）
    を与え，その実行結果を確認せよ．

    shuffleわからん
    random.sampleについて
    https://note.nkmk.me/python-random-choice-sample-choices/
"""

str_10 = ("I couldn’t believe that "
          "I could actually understand"
          "what I was reading : the phenomenal"
          " power of the human mind .")
str_10_list = str_10.split()
ans_10 = []
for val_10 in str_10_list:
    if len(val_10) > 4:
        val_10 = val_10[:1] + \
            "".join(random.sample(val_10[1:-1], len(val_10) - 2)) + val_10[-1:]
    ans_10.append(val_10)
print(" ".join(ans_10))
# %%
