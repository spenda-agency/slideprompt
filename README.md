# PPT詳細テンプレ

SPENDAのスライド資料を Markdown（Marp）で作り、**PPT詳細テンプレ**（SPENDA 2026版デザインの詳細版）で PDF・PPTX に変換するリポジトリです。
`main` 以外も含め、push すると GitHub Actions（`.github/workflows/convert.yml`）が `output/` に PDF・PPTX を生成します。

## AIによる資料作成の標準ルール

資料作成を依頼する際は、最初に [AGENTS.md](AGENTS.md) を読ませてください（Claude Code向けの入口は [CLAUDE.md](CLAUDE.md)）。

- 標準テンプレートは **PPT詳細テンプレ**。正本は [SPENDA_components.pptx（16部品）](templates/PPT詳細テンプレ_SPENDA_components.pptx) と [spenda-2026（基本2枚）](templates/spenda-2026/SPENDA_PPTテンプレート.pptx) で、同じスライドマスタ・背景・ロゴの同一デザインです。
- PowerPointの作成は、最新の正本PPTXを取得・確認し、既存マスタ・レイアウト・背景・ロゴを引き継いで行います。
- 正本を取得できない場合は、古いZIP・旧テーマ・独自デザインへ無断で切り替えません。
- Marp変換はデザインの再現であり、正本PPTXのスライドマスタを直接使う処理ではありません。
- `サンプル出力_md/` にある個別のデザイン指定は参考例であり、標準テンプレートの指定ではありません。

依頼文の例：

> このリポジトリのAGENTS.mdを読み、PPT詳細テンプレ（templates/PPT詳細テンプレ_SPENDA_components.pptx）の部品を使って資料を作成してください。取得できなければ別テンプレートに切り替えず、その旨を知らせてください。

## 使い方（Marp）

1. `slide.md` か `templates/PPT詳細テンプレ_サンプル.md` をコピーして、リポジトリ直下に `資料名.md` を作る（`theme: spenda-detail`）
2. [作成ルール](templates/PPT詳細テンプレ_作成ルール.md) の部品（表紙・アジェンダ・カード・ステップ・表・数値など16種）を使って中身を書く
3. push すると `output/資料名.pdf` と `output/資料名.pptx` が自動で作られる

## テーマ一覧

| テーマ名 | ファイル | 用途 |
|---|---|---|
| `spenda-detail` | `themes/spenda-detail.css` | **標準**。PPT詳細テンプレの16部品を再現（4:3） |
| `spenda-style` | `style.css` | 2026版の基本形（表紙＋本文）。既存資料の互換用 |
| `spenda-style-legacy` | `themes/legacy/spenda-style-legacy.css` | 旧デザイン。明示された場合のみ |

## フォルダ構成

| パス | 内容 |
|---|---|
| `templates/PPT詳細テンプレ_SPENDA_components.pptx` | 正本（16部品） |
| `templates/spenda-2026/` | 正本（基本2枚）と `spenda-style` 用の画像 |
| `templates/PPT詳細テンプレ_作成ルール.md` | 書き方・部品・文字数のルール |
| `templates/PPT詳細テンプレ_サンプル.md` / `.pptx` | 全16部品の見本 |
| `templates/spenda-detail.src.css` / `build_theme.py` / `assets/` | `spenda-detail` のソースとビルドスクリプト |
| `output/` | 変換済みの PDF・PPTX |
| `images/` | 資料ごとの図版 |

## 手元で変換する

```bash
npx @marp-team/marp-cli@4.0.3 資料名.md --theme-set style.css themes/spenda-detail.css themes/legacy/spenda-style-legacy.css --allow-local-files --pptx -o output/資料名.pptx
```

PDF は `--pdf`、画像は `--images png` に置き換えます。

## テンプレートを更新するとき

- **spenda-detail**：`templates/spenda-detail.src.css` を編集し、`python3 templates/build_theme.py` で `themes/spenda-detail.css` を再生成（`themes/` 側は直接編集しない）。画像は `templates/assets/`。
- **spenda-style**：`style.css` 冒頭の変数（`--spenda-navy`, `--spenda-copyright` など）と px 値を編集。画像は `templates/spenda-2026/assets/`。
