# slideprompt

Marp でスライド（PDF / PPTX）を作成するためのテンプレート一式です。
`main` 以外も含め、push すると GitHub Actions（`.github/workflows/convert.yml`）が `output/` に PDF・PPTX を生成します。

## デフォルトテンプレート（SPENDA 2026版）

| ファイル | 役割 |
|---|---|
| `style.css` | デフォルトテーマ（`theme: spenda-style`） |
| `templates/spenda-2026/SPENDA_PPTテンプレート.pptx` | デザインの元になった PowerPoint テンプレート |
| `templates/spenda-2026/assets/` | テーマが使う画像（表紙背景・ヘッダー帯・ロゴ・L字フレーム） |
| `themes/legacy/spenda-style-legacy.css` | 旧デザイン（`theme: spenda-style-legacy`） |

### スライドの書き方

```markdown
---
marp: true
theme: spenda-style
size: 4:3
paginate: true
---

<!-- _class: lead -->

# 表紙タイトル<br>2行目

## English subtitle

---

<!-- header: 章の名前（上部の帯に表示） -->

# 本文スライドのタイトル

## キーメッセージ（20pt 太字）

- 本文テキスト、箇条書きなど（行頭文字 ● ○ ■）
```

- **1枚目は必ず表紙**：`<!-- _class: lead -->` … `#` がタイトル、`##` が英字サブタイトル
- **2枚目以降は本文**（PPT テンプレート2枚目のスライドマスタ「TITLE_AND_BODY」を再現）
  - 上部グラデーション帯：`<!-- header: ... -->` の文字（以降のスライドにも引き継がれます。1枚だけなら `_header`）
  - `#`：タイトルプレースホルダー（24pt）
  - 本文：18pt、`##` はキーメッセージ（20pt 太字）
  - 下部グラデーション帯：左にコピーライト、右にページ番号（自動）
- 旧テンプレートの `title-bar` / `content` / `message-large` / `message-small` / `catchcopy` クラスもそのまま使えます

## テンプレートを更新するとき

1. 新しい PPTX を `templates/spenda-2026/SPENDA_PPTテンプレート.pptx` に上書き
2. 画像が変わった場合は `templates/spenda-2026/assets/` の同名ファイルを差し替え
3. 色・コピーライト表記・フォントは `style.css` 冒頭の変数（`--spenda-navy`, `--spenda-copyright` など）を編集
4. 位置やサイズが変わった場合は `style.css` の `section.lead` / `section h1` などの px 値を調整（960×720px 基準）

画像は Markdown ファイルからの相対パスで読み込むため、`.md` はリポジトリ直下に置き、変換時は `--allow-local-files` を付けてください。

```bash
marp slide.md --theme style.css --allow-local-files --pdf
```
