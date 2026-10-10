# PPT詳細テンプレ（リポジトリ: ppt-detail-template）

SPENDAのスライド資料を Marp の Markdown で作り、PDF・PPTX に変換するリポジトリ。

## スライドを作るときは必ずこのテンプレを使う

- 新しい資料は `theme: spenda-detail`（PPT詳細テンプレ）で作る。旧テーマ `spenda-style`（`style.css`）は既存資料の互換用で、新規には使わない。
- 書き方・部品・文字数の上限は `templates/PPT詳細テンプレ_作成ルール.md` に従う。
- 部品のHTMLは `templates/PPT詳細テンプレ_サンプル.md` からコピーする（テンプレ原本の16スライドと1対1で対応）。
- 新しい資料はリポジトリ直下に `資料名.md` で置く。図版は `images/<資料名>/` に置き、`<div class="figure">` で挿入する。

## 仕上げの確認

- 手元で PNG に書き出して全ページを目視し、文字のはみ出し・重なりがないことを確認する：
  `CHROME_PATH=$(ls -d /opt/pw-browsers/chromium*/chrome-linux/chrome | head -1) npx @marp-team/marp-cli@4.0.3 資料名.md --theme-set style.css themes/spenda-detail.css --allow-local-files --images png -o <作業用ディレクトリ>/s.png`
- PPTX が必要なら同じコマンドで `--pptx -o output/資料名.pptx`。
- push すると `.github/workflows/convert.yml` が全資料を `output/` に変換する。

## テーマの修正

`templates/spenda-detail.src.css` を編集 → `python3 templates/build_theme.py` で `themes/spenda-detail.css` を再生成する。`themes/` のCSSは画像埋め込み済みの生成物なので直接編集しない。
