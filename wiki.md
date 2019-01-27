# knowledge memo

## \__pycache\__
- Python3.2以降で出てきた、インポート時の読み込みを早くするためのバイナリファイルを配置したフォルダ。
- 消しても問題ない。たいてい.gitignore

## Error: [WinError 10013] アクセス許可で禁じられた方法でソケットにアクセスしようとしました。
portを変更する
>python manage.py runserver <変更したいport>

## TypeError: __init__() missing 1 required positional argument: 'on_delete'
- モデル同士を紐づけるときに、ForeignKeyやOneToOneFieldを使うが、引数としてon_deleteを指定することがDjango2.0から必須となった。
