---
marp: true
theme: default
style: |
  section {
    background-color: #FFFFFF;
    color: #222222;
    font-family: 'Yu Gothic', '游ゴシック', sans-serif;
  }
  h1 {
    font-size: 30pt;
    font-weight: bold;
    color: #222222;
  }
  h2 {
    font-size: 22pt;
    font-weight: normal;
    color: #222222;
  }
  p, li {
    font-size: 18pt;
    font-weight: normal;
    color: #222222;
    line-height: 1.35;
  }
  .small {
    font-size: 12pt;
    color: #555555;
  }
  .section-label {
    font-size: 12pt;
    color: #555555;
    font-weight: normal;
    position: absolute;
    top: 20px;
    left: 40px;
  }
  hr {
    border: none;
    border-top: 1pt solid #E6E6E6;
  }
  strong {
    color: #0B57D0;
  }
  ul {
    list-style: none;
    padding-left: 0;
  }
  li::before {
    content: "・";
    margin-right: 0.5em;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# 非エンジニアが知るべきGitHubの活用方法と事例

---

<!-- _class: lead -->
<!-- _paginate: false -->

# 非エンジニアが知るべきGitHubの活用方法と事例

発表者：[発表者名]

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Introduction</span>

# GitHubの一般的な認識

・GitHubはエンジニア向けのコード管理ツールとして広く認知されている

・実際には、コードを書かずに活用できる機能が多数存在する

・テキスト（文章）の進化過程を記録するタイムマシンのような性質を持つ

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Introduction</span>

# 非エンジニアが直面する課題

・文書管理における履歴追跡の困難さ

・共同作業における校正プロセスの非効率性

・知識の蓄積と検索の課題

・タスク管理ツールの分散

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Introduction</span>

# 本研究の目的

非エンジニアがコードを書かずにGitHubを活用する方法を3つ厳選して提示する

プロンプト管理以外の実践的な活用事例を紹介する

ブラウザ操作のみで実現可能な機能に焦点を当てる

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Methods</span>

# 対象

・エンジニアではない一般社会人

・コードを書かない、または書けない方

・文書作成、タスク管理、知識管理に関心がある方

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Methods</span>

# 評価方法

・ブラウザ操作のみで実現可能か

・コード知識が不要か

・実務での実用性

・学習コストの低さ

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Methods</span>

# 評価項目

主要評価項目：活用方法の実現可能性

副次評価項目：操作の容易性、実用性、汎用性

評価基準：マウス操作とタイピングのみで完結すること

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Results</span>

# 活用方法1：執筆・ドキュメント作成の最強のバックアップ

報告書、マニュアル、ブログ記事、書籍などの長文作成において、GitHubは最高のパートナーとなる

「あの時の表現に戻したい」が瞬時に可能

Markdown（マークダウン）での清書が自動で見栄えの良いドキュメントとして表示される

共同校正において、プルリクエストによるスマートなやり取りが可能

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Results</span>

# 活用方法2：GitHub Projects を使った視覚的なタスク管理

TrelloやNotionのカンバンボードに似た高機能なタスク管理ツールが備わっている

ドラッグ＆ドロップで「未着手」「進行中」「完了」などの列を作り、タスクを移動させて管理できる

ライフログや家事のルーチン化など、定期タスクをリスト化してチェックボックスで管理できる

全ての情報を一箇所に集約し、関連するプロンプトや参考URL、メモを紐付けておける

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Results</span>

# 活用方法3：自分だけの秘伝のタレ（ナレッジベース）の構築

Wiki機能やREADMEファイルを使って、自分専用の百科事典を作ることができる

「半年に一度しかやらない経費精算の手順」や「AIへの効果的な指示の出し方コツ集」などを蓄積できる

GitHubはテキスト検索が非常に強力で、過去の膨大なメモから必要な情報をすぐに見つけ出せる

公開・非公開の切り替えがフォルダごとに簡単に選べる

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Discussion</span>

# 主要な発見

非エンジニアでもコードを書かずにGitHubを活用できる方法が3つ特定された

いずれの方法もブラウザ操作のみで実現可能であることが示された

実務での実用性が高く、学習コストが低いことが示唆される

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Discussion</span>

# 発見1の裏付け：履歴管理の優位性

Wordの「元に戻す」機能よりもはるかに強力な履歴管理が可能である

過去の任意の時点の状態に戻せるため、文書作成における自由度が高い

この機能は既存の文書管理ツールと比較して優位性を示す

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Discussion</span>

# 発見2の裏付け：タスク管理の統合性

既存のタスク管理ツール（Trello、Notion）と同等以上の機能を提供する

さらに、コード管理機能と統合されているため、技術文書とタスクを一元管理できる

この統合性は他のツールでは実現が困難である

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Discussion</span>

# 発見3の裏付け：知識管理の検索性

テキスト検索機能が非常に強力であり、過去の膨大な情報から必要な情報を迅速に発見できる

公開・非公開の切り替えが容易であるため、個人利用から組織利用まで柔軟に対応できる

この柔軟性は既存の知識管理ツールと比較して優位性を示す

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Discussion</span>

# 限界点

GitHubの操作に慣れるまでに一定の学習時間が必要である

初回設定において、アカウント作成やリポジトリ作成などの手順を理解する必要がある

高度な機能を使用する場合、コマンドライン操作が必要になる可能性がある

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">Conclusion</span>

# 結論

非エンジニアがコードを書かずにGitHubを活用する方法として、執筆・ドキュメント作成のバックアップ、GitHub Projects を使ったタスク管理、ナレッジベースの構築の3つが有効であることが示された

いずれの方法もブラウザ操作のみで実現可能であり、実務での実用性が高い

まずはIssue、Markdown、Projectの3つの機能から始めることを推奨する

---

<!-- _class: section -->
<!-- _paginate: true -->

<span class="section-label">References</span>

# 参考文献

GitHub公式ドキュメント

https://docs.github.com/

Markdown記法ガイド

https://www.markdownguide.org/

