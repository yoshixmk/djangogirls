# knowledge memo

## \__pycache\__
- Python3.2以降で出てきた、インポート時の読み込みを早くするためのバイナリファイルを配置したフォルダ。
- 消しても問題ない。たいてい.gitignore

## Error: [WinError 10013] アクセス許可で禁じられた方法でソケットにアクセスしようとしました。
portを変更する
>python manage.py runserver <変更したいport>
