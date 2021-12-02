# languageshadower

マルコフ連鎖を用いて、文章の自動生成をおこなってくれる無駄アプリです。
中国語、英語の2言語と、医療、ビジネス、科学の3つのジャンルを選ぶことができます。

## 仕組み
1. VOAの著作権フリーの記事を読み込む（ファイル内に存在）
2. 中国語の文章は、形態素解析エンジンJiebaを用いて分かち書きを行う
3. 中国語、英語の文章の下処理を行う
4. マルコフ連鎖のライブラリmarkkovifyを用いて文章生成を行い、表示
5. 生成した文章をgoogletransで日本語に訳して表示

## 使用技術
フレームワーク: Django
バックエンド: Python
フロントエンド: Html, Css
使用したライブラリ: markovify(マルコフ連鎖), Jieba(中国語形態素解析), googletrans(非公式のgoogle翻訳API)

## 注意事項
同時アクセスがあると、新しい方に生成されたファイルが書き換えられます。（データベース作成で解消されるかも）
googletransが非公式APIなので、googleバージョンによっては作動しないことがあります。
記事を更新していないので、2021年上半期ごろのニュース記事をもとに生成されます。

## その他追記
デプロイとデータベース、記事の著作権の再チェックが終わりしだいデプロイして公開します。
ただ、当人がherokuへのデプロイを苦手としているため期待しないでください。
