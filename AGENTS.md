# スライド作成ルール

## 標準テンプレート

- ユーザーが別のテンプレートを明示しない限り、標準は **PPT詳細テンプレ**（SPENDA 2026版デザインの詳細版）。
- 正本は次の2つ。どちらも同じスライドマスタ（TITLE_AND_BODY / BIG_NUMBER / BLANK）・背景・ロゴ・配色を持つ同一デザイン。
  - `templates/PPT詳細テンプレ_SPENDA_components.pptx` … 表紙・章扉・アジェンダ・カード・ステップ・表・ロードマップ・数値・チェックリスト・会社概要・クロージングなど **16部品**。資料を組み立てるときの基準。
  - `templates/spenda-2026/SPENDA_PPTテンプレート.pptx` … 表紙と本文の **基本2枚**。
- Marp用テーマは `theme: spenda-detail`（`themes/spenda-detail.css`）。書き方・部品・文字数の上限は `templates/PPT詳細テンプレ_作成ルール.md`、全部品の見本は `templates/PPT詳細テンプレ_サンプル.md`。
- `style.css` の `theme: spenda-style` は2026版の基本形（表紙＋本文）を再現するMarpテーマ。既存資料の互換用で、新規資料は `spenda-detail` で作る。

## 作成前の確認

1. このファイルと `README.md`、`templates/PPT詳細テンプレ_作成ルール.md` を読む。
2. 指定ブランチ（指定がなければ最新の `main`）で正本PPTXの存在を確認する。過去のZIPやキャッシュだけを根拠にテンプレートを選ばない。
3. PowerPointの作成を依頼された場合は、正本PPTXを取得して開き、表紙・本文レイアウト・スライドサイズ（4:3）・スライドマスタ・背景・ロゴ・フォントを確認してから制作する。
4. 使用するテンプレート名とパスを制作開始時に伝える。

## PowerPointの作成

- 正本PPTXを基礎に、既存のスライドマスタ・レイアウト・背景・ロゴ・配色・余白・スライドサイズを引き継ぐ。部品は `SPENDA_components.pptx` のスライドを複製して使う。
- 「雰囲気が似た」独自デザイン、過去の出力PPTX、旧テーマで置き換えない。
- 本文・表・図形は、制作環境で可能な限り編集可能にする。
- 完成後は正本と出力を比較し、はみ出し・欠落・文字の重なりを確認する。

## Marpの作成・変換

- 新しい資料はリポジトリ直下に `資料名.md` を置き、`theme: spenda-detail` で作る。図版は `images/<資料名>/` に置き `<div class="figure">` で挿入する。
- Marp出力は正本PPTXのデザインを再現するもの（各スライドが画像のPPTX）であり、正本のスライドマスタを直接利用したPowerPointとは区別して伝える。
- `themes/legacy/spenda-style-legacy.css` は、ユーザーが旧版を明示した場合のみ使用する。
- 手元で PNG に書き出して全ページを目視し、文字のはみ出し・重なりがないことを確認する：
  `npx @marp-team/marp-cli@4.0.3 資料名.md --theme-set style.css themes/spenda-detail.css themes/legacy/spenda-style-legacy.css --allow-local-files --images png -o <作業用ディレクトリ>/s.png`
- push すると `.github/workflows/convert.yml` が `marp: true` を含むルート直下の md をすべて `output/` に PDF・PPTX で出力する。

## テーマの修正

- `spenda-detail`：`templates/spenda-detail.src.css` を編集 → `python3 templates/build_theme.py` で `themes/spenda-detail.css` を再生成（`themes/` 側は画像埋め込み済みの生成物なので直接編集しない）。
- `spenda-style`：`style.css` 冒頭の変数と px 値を編集（画像は `templates/spenda-2026/assets/`）。

## 取得できない場合

- 正本PPTXを取得・確認できない場合、別テンプレートへ無断で切り替えない。
- 内容の整理は進めてよいが、「テンプレ適用済み」の完成版として提出しない。
- 取得できない理由を伝え、正本の提供を依頼する。仮版を別デザインで作るのはユーザーが明示的に了承した場合のみ。

## サンプル資料

`サンプル出力_md/` と過去の `output/` は内容・構成の参考。そこにある別のデザイン指定で標準テンプレートを上書きしない。ユーザーの今回の明示的な指定を優先する。
