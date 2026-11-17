# CSAI-Sorting-robot
CS&AIセットのシングルモーターを使った仕分けロボットです。
カメラの映像から「リンゴ」と「バナナ」を認識して、モーターを制御します。
リンゴの場合、シングルモーターを+45度に回転します。
バナナの場合、シングルモーターを-45度に回転します。

## Files
・project.tm : 「Teachable Machine」のプロジェクトファイル。

・keras_model.h5 : 「Teachable Machine」からエクスポートしたモデル。

・labels.txt : 「Teachable Machine」からエクスポートしたファイル。

・sorting_robot.py : プログラム。
VideoCapture関数の引数でカメラを選択できます。

## ライセンス
・当プログラムの著作権は株式会社アフレルと松原拓也に帰属します。

・当プログラムの商用利用は禁止します。

・当プログラムの動作保証とサポートはいたしかねます。

AFREL TECH BLOG Webサイト

https://afrel.co.jp/techblog/
