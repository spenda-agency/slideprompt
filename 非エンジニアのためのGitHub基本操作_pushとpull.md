---



marp: true

theme: spenda-style

size: 16:9

paginate: true

---

<!-- _class: lead -->

# 非エンジニアのためのGitHub基本操作

## 「push」と「pull」をマスターして同期の仕組みを理解する

Copyright © SPENDA Corp. All Rights Reserved.

---

<div class="title-bar">本日のゴール</div>
<div class="confidential">Confidential</div>
<div class="content">
<div class="message-large">GitHubにおける「情報の同期」の仕組みを理解する</div>
<div class="message-small">「push」と「pull」の役割を明確にし、チーム開発で事故を防ぐための「デイリーワークフロー」を学ぶ</div>
</div>
<div class="catchcopy">pushとpullをマスターして、チーム開発を安全に</div>

---

<div class="title-bar">前提知識：2つの「置き場所」</div>
<div class="confidential">Confidential</div>
<div class="content">
<div class="message-large">GitHubでは、情報は常に2つのリポジトリ（貯蔵庫）を行き来します</div>
<div class="message-small">リモートリポジトリ（共有場所）：GitHubのサーバー上にある「マスターデータ」で、チーム全員が見る場所。ローカルリポジトリ（自分の作業場）：自分のPC内にある「自分専用の領域」で、納得いくまで自由に編集できる場所。</div>
</div>
<div class="catchcopy">2つのリポジトリで情報を管理する仕組み</div>

---

<div class="title-bar">「push（プッシュ）」：成果を共有する</div>
<div class="confidential">Confidential</div>
<div class="content">
<div class="message-large">自分の手元で行った作業を、GitHub上の共有場所に「押し出す」操作です</div>
<div class="message-small">pushの前に、何を変えたかのメモ（履歴）を残すコミット（Commit）が前提。自分の成果がチーム全員に見えるようになり、複数の修正を「ひとまとめ」にして安全に反映できるメリットがあります。</div>
</div>
<div class="catchcopy">成果をチームに共有する「押し出す」操作</div>

---

<div class="title-bar">「pull（プル）」：最新を取り込む</div>
<div class="confidential">Confidential</div>
<div class="content">
<div class="message-large">GitHub上にある最新の変更を、自分の手元に「引っ張ってくる」操作です</div>
<div class="message-small">他人が更新した内容を自分のPCに反映させる情報の同期。古いデータで作業を始めると、後で矛盾が起きやすくなるため、「まずpullから始める」のが鉄則です。</div>
</div>
<div class="catchcopy">最新状態を取り込む「引っ張ってくる」操作</div>

---

<div class="title-bar">コンフリクト（競合）とは何か？</div>
<div class="confidential">Confidential</div>
<div class="content">
<div class="message-large">同じファイルの同じ行を、2人が同時に編集した際に起こる「確認作業」です</div>
<div class="message-small">エラーではなく「安全装置」。GitHubが勝手に判断せず、「人間が選んでください」と警告してくれます。こまめにpush/pullを行い、差分を小さく保つことや、「今からここを直します」というチーム内コミュニケーションで回避できます。</div>
</div>
<div class="catchcopy">安全に編集するための「確認作業」</div>

---

<div class="title-bar">実践！理想のデイリーワークフロー</div>
<div class="confidential">Confidential</div>
<div class="content">
<div class="message-large">「先祖返り」や「上書きミス」を防ぐための4ステップ</div>
<div class="message-small">【朝】まずpull：チームの最新状態を手元に入れる。【日中】作業＆コミット：自分のPCでこまめに履歴を残す。【完了前】念のためpull：自分が作業中に誰かが更新していないか確認。【夕方】最後にpush：自分の成果をチームに共有する。</div>
</div>
<div class="catchcopy">pullで始まり、pushで終わる安全なリズム</div>

---

<div class="title-bar">まとめと次のステップ</div>
<div class="confidential">Confidential</div>
<div class="content">
<div class="message-large">pushは「共有場所へのアップロード」、pullは「最新状態のダウンロード」</div>
<div class="message-small">pullで始まり、pushで終わるリズムを身につけることが重要です。Next Action：テスト用のリポジトリで、1行だけのテキストファイルを「push」して、ブラウザで編集後に「pull」するキャッチボールを試してみましょう！</div>
</div>
<div class="catchcopy">pullで始まり、pushで終わるリズムを身につける</div>

---

<!-- _class: last-slide -->

# お問い合わせ

運用作業やサポートを依頼したい方は下記よりご依頼頂けます。

- **Web**: https://spendacorp.com/contact.html

- **Email**: contact@spenda-c.com

無料相談（30分）、アカウント診断申込など、お気軽にご相談ください。

