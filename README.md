# kakuyu_dorm https://nascola.github.io/kakuyu_dorm/

http://www.maizuru-ct.ac.jp/06life/other.html#dormitory

のためにだけある寮食メニュー切り取り&日付ラベリングスクリプト。

python3系です。

# 多分必要なやつ
 wget python3 poppler-utils

# 使い方

例:ターミナルで2017年4月の寮食メニューを取得したい

$ python3 crop.py 2017 04

imgディレクトリ内に '%Y-%m-%d.jpg'のフォーマットで画像が入る
