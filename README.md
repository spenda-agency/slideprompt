# PPT詳細テンプレ

SPENDAのスライド資料を Markdown（Marp）で作り、**PPT詳細テンプレ**のデザインで PDF・PPTX に変換するリポジトリです。

## 使い方

1. `slide.md` か `templates/PPT詳細テンプレ_サンプル.md` をコピーして、リポジトリ直下に `資料名.md` を作る
2. `templates/PPT詳細テンプレ_作成ルール.md` の部品を使って中身を書く
3. push すると GitHub Actions が `output/資料名.pdf` と `output/資料名.pptx` を自動で作る

## フォルダ構成

| パス | 内容 |
|---|---|
| `templates/PPT詳細テンプレ_SPENDA_components.pptx` | デザインの原本（16種類の部品スライド） |
| `templates/PPT詳細テンプレ_作成ルール.md` | 書き方・部品・文字数のルール |
| `templates/PPT詳細テンプレ_サンプル.md` | 全16部品の見本（Marp） |
| `templates/spenda-detail.src.css` / `build_theme.py` / `assets/` | テーマのソースとビルドスクリプト |
| `themes/spenda-detail.css` | 生成済みテーマ（直接編集しない） |
| `style.css` | 旧テーマ `spenda-style`（既存資料用） |
| `output/` | 変換済みの PDF・PPTX |
| `images/` | 資料ごとの図版 |

## 手元で変換する

```bash
npx @marp-team/marp-cli@4.0.3 資料名.md --theme-set style.css themes/spenda-detail.css --allow-local-files --pptx -o output/資料名.pptx
```

PDF は `--pdf`、画像は `--images png` に置き換えます。
