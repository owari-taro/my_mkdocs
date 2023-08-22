# 技術日記・メモ

## 2023/8/18
### mkdocs
* とりあえず初めて使ってみた。
* toctreeみたいなのがないのはsphinxに比べて不便。あとはおおむ満足.

## 2023/8/19

* ダークモードの切り替えもつけれた
* 拡張機能もかなりあるみたいなのでsphinxと比べても仕事でも十分つかえるだろう

``` yaml

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

```


## 2023/8/20
### mkdocs and read the docs

* blog[^1]を参考にmkdocsをread the docsで公開できるようにした
* sphinxも同じ感じにできるようだ。github pagesのほうが繁栄が早い気もするがlocalでbuildしてpushしてるからだろうか
* github pagesだとdocsにhtmlを展開しなきゃいけないけど,mkdocsはmdファイルをdocsに入れなきゃいけなさそうなので
#### github-pages
* mkdocs gh-deployでも簡単にデプロイできた。こっちのほうがdeployがはやい？[^2]

```
mkdocs gh-deploy\
```
!!! todo
   
      codecommit→s3の組み合わせでもできそうなのでやる
      [clasmethod例](https://dev.classmethod.jp/articles/sphinx_auto_deployment_to_aws_s3/)


[^1]:[MkDocsドキュメントをGitHubに登録してRead the Docsで自動公開する](https://blog.goediy.com/?p=535#google_vignette)を参考にした
[^2]:[参考](https://enu23456.hatenablog.com/entry/2022/11/11/192039)



https://github.com/pangeo-data/cog-best-practices/issues/4