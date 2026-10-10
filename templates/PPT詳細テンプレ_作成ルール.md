# PPT詳細テンプレ 作成ルール

SPENDAのスライドは、このルールに沿って Marp の Markdown で作成する。
デザインの原本は `templates/PPT詳細テンプレ_SPENDA_components.pptx`、全部品の見本は `templates/PPT詳細テンプレ_サンプル.md`。

## 基本設定

```markdown
---
marp: true
theme: spenda-detail
paginate: true
---
```

- サイズは **4:3（960×720px＝10×7.5インチ）**。テンプレ原本と同じ。
- スライドの区切りは `---`。
- 1スライド1メッセージ。タイトル（`#`）は体言止め、句点なしで20字程度まで。

## 共通パーツ（本文スライド）

| パーツ | 書き方 | 文字数の目安 |
|---|---|---|
| 帯ラベル（上部の青帯の白文字） | `<!-- _header: 課題の整理 -->` | 12字以内 |
| スライドタイトル（24pt） | `# タイトル` | 20字以内 |
| リード文（ネイビー太字） | `<p class="msg">…</p>` | 50字以内 |
| 強調 | `**強調**`（ネイビー太字） | — |
| 注記 | `<p class="note">※ …</p>` | 60字以内 |
| 図版 | `<div class="figure">` の中に空行を挟んで `![h:300](images/...)` | — |

- 帯ラベルは必ず `_header`（先頭のアンダースコア付き）で指定する。付けないと次のスライドにも引き継がれる。
- フッター（コピーライト・ページ番号）は自動で入る。

## 部品カタログ（テンプレ原本の16スライドに対応）

| No. | 部品 | 指定 | 中身の上限 |
|---|---|---|---|
| 01 | 表紙 | `<!-- _class: cover -->` | 宛名・タイトル2行（1行11字以内）・英語サブタイトル・日付 |
| 02 | 章扉 | `<!-- _class: chapter -->` | 番号・章タイトル（12字以内）・英語サブタイトル |
| 03 | アジェンダ | `<div class="agenda">` | 6項目・タイトル15字・補足30字 |
| 04 | キーメッセージ | `<div class="key">` ＋直後の段落 | 主張2行（1行18字）・補足120字 |
| 05 | 箇条書き | `<div class="bullets">` ＋ Markdownリスト | 7項目・各60字 |
| 06 | 横並びカード | `<div class="cards">` ＋ `.card` ×2〜4 | 見出し12字・本文80字 |
| 07 | 2×2グリッド | `<div class="grid2">` ＋ div ×4 | 見出し15字・本文70字 |
| 08 | Before / After | `<div class="ba">` | 各6項目 |
| 09 | ステップ | `<div class="steps">` ＋ `.step` ×2〜5 | フェーズ名8字・期間・本文60字 |
| 10 | 表 | Markdownの表 | 5列×8行。1列目は行ラベル |
| 11 | ロードマップ | `<div class="roadmap">` | 6期間×5タスク |
| 12 | 数値で示す | `<div class="kpis">` ＋ `.kpi` ×2〜4 | 指標名15字・補足40字。前提を注記に必ず書く |
| 13 | チェックリスト | `<ul class="checklist">` | 8項目・各40字 |
| 14 | 会社概要 | `<div class="company">` ＋ `.row` | 7行・内容60字 |
| 15 | クロージング | `<!-- _class: closing -->` | タイトル＋連絡先 |
| 16 | 自由スライド | 共通パーツのみ（図版などを自由に配置） | — |

各部品の正確なHTMLは `templates/PPT詳細テンプレ_サンプル.md` からコピーして使う。代表例：

```markdown
<!-- _header: 課題の整理 -->

# 横並びカード

<p class="msg">リード文（50字以内）</p>

<div class="cards">
<div class="card"><span class="label">POINT 01</span><h3>見出し1</h3><p>本文。80字以内。</p></div>
<div class="card"><span class="label">POINT 02</span><h3>見出し2</h3><p>本文。80字以内。</p></div>
</div>
```

```markdown
<div class="roadmap">
<div></div><div class="m">1月</div><div class="m">2月</div><div class="m">3月</div><div class="m">4月</div><div class="m">5月</div><div class="m">6月</div>
<div class="task">タスク1</div><div class="bar s1 e2">内容</div>
<div class="task">タスク2</div><div class="bar dark s2 e4">内容</div>
</div>
```

ロードマップのバーは `s1`〜`s6`（開始月）と `e1`〜`e6`（終了月）で位置を決める。`dark` を付けるとネイビーになる。

## 構成の型（提案・会社紹介の場合）

1. 表紙（cover）
2. アジェンダ（agenda）
3. キーメッセージ（key）
4. 章扉（chapter）→ 本文スライド（カード／グリッド／表／数値など）を章ごとに繰り返す
5. 進め方（steps）・スケジュール（roadmap）
6. 確認事項（checklist）・会社概要（company）
7. クロージング（closing）

同じ部品を3枚以上続けない。数値は根拠・前提を注記に書き、試算・目標値であることを明示する。

## 配色・書体（テンプレ原本の値）

| 用途 | 色 |
|---|---|
| ネイビー（見出し・番号・帯） | `#262C7B` |
| ブルー（アクセント・数値） | `#2B5FD9` |
| ライトブルー（ラベル） | `#6F9FD6` |
| 淡ブルー（ボックス背景） | `#E8F3FD` |
| 罫線 | `#C9D6EA` |
| 本文 / 補足 | `#1F1F1F` / `#595959` |

書体は Noto Sans JP（英数字は Arial）。

## 出力

- push すると GitHub Actions が `marp: true` を含むルート直下の md をすべて `output/` に PDF・PPTX で出力する。
- 手元で出力する場合：

```bash
npx @marp-team/marp-cli@4.0.3 資料名.md --theme-set style.css themes/spenda-detail.css themes/legacy/spenda-style-legacy.css --allow-local-files --pptx -o output/資料名.pptx
```

## テーマを直すとき

`templates/spenda-detail.src.css` を編集し、`python3 templates/build_theme.py` で `themes/spenda-detail.css` を再生成する（画像を埋め込むため、`themes/` 側は直接編集しない）。
