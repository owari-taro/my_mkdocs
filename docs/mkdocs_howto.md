# MkDocsHowTo


## docstring example
moduleを指定すれば自動でdocstringとソースコードが表示できる

::: src.dummy



## darkmodeの切り替え
下の設定でできる

    theme:
    palette:
        - scheme: default
          toggle:
              icon: material/toggle-switch-off-outline
              name: ダークモードに切り替えます。
        - scheme: slate
          primary: red
          accent: red
          toggle:
              icon: material/toggle-switch
              name: ライトモードに切り替えます


## 注の書き方
```
test[^1] 


[^1]:注は一番したに表示されるよ
```