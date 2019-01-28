# knowledge memo

## \__pycache\__
- Python3.2以降で出てきた、インポート時の読み込みを早くするためのバイナリファイルを配置したフォルダ。
- 消しても問題ない。たいてい.gitignore

## Error: [WinError 10013] アクセス許可で禁じられた方法でソケットにアクセスしようとしました。
portを変更する
>python manage.py runserver <変更したいport>

## TypeError: __init__() missing 1 required positional argument: 'on_delete'
- モデル同士を紐づけるときに、ForeignKeyやOneToOneFieldを使うが、引数としてon_deleteを指定することがDjango2.0から必須となった。

## git push heroku masterでエラー 
```bash
$ git push heroku master
Enumerating objects: 94, done.
Counting objects: 100% (94/94), done.
Delta compression using up to 8 threads
Compressing objects: 100% (85/85), done.
Writing objects: 100% (94/94), 11.71 KiB | 705.00 KiB/s, done.
Total 94 (delta 34), reused 3 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote:  !     Python has released a security update! Please consider upgrading to python-3.7.1
remote:        Learn More: https://devcenter.heroku.com/articles/python-runtimes
remote: -----> Installing python-3.7.2
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        /app/tmp/buildpacks/<instance id>/bin/steps/pip-install: line 42: /app/.heroku/python/bin/pip: No such file or directory
remote:  !     Push rejected, failed to compile Python app.
remote:
remote:  !     Push failed
remote: Verifying deploy...
remote:
remote: !       Push rejected to <service name>.
remote:
To https://git.heroku.com/<service name>.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/<service name>.git'
```
runtime.txtを3.7.1に変更して解決。エラーからは読み取りにくいが、ドキュメントにあるPythonのsupportしているバージョンが3.7.1を使うことで回避。エラーは、3.7.2の際に出た
