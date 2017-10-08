Linux Bash CLI/CUI 辞書引きコマンド
==================
【参考】
[CUI超お手軽英語辞書 - capriccioso String Creating(Object something){ return My.Expression(something); }](http://d.hatena.ne.jp/its\_out\_of\_tune/20120610/1339311044)

にあるようなweblioから説明文を抽出するスクリプトに
L
に

* メモ化
* 言及英単語を再帰的呼び出し
* 発音
* オプションからクリップボード監視翻訳

の機能を追加したようなもの(ただしコードはシェルスクリプトのみで書かれています)。
コマンド名は上と同様に "je"

複数の語を分かち書きしたものからなる節を調べるときは語と語の間を(空白ではなく)プラス記号で区切る
例: Haskell Curry を調べるときは `je haskell+curry`
