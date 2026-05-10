# slideprompt

スライド制作のための **2 系統のツールキット**を 1 リポジトリに集約したものです。

| 系統 | 用途 | 入口 |
|---|---|---|
| **A. Marp + プロンプト** | Markdown を書いて GitHub Actions で PDF/PPTX を自動生成 / Claude に貼り付ける雛形 | [`marp/`](marp/) ・ [`prompts/`](prompts/) |
| **B. SlideKit（Claude Code スキル）** | `/slidekit-create` で HTML スライドを新規作成、`/slidekit-templ` で PDF→HTML テンプレ化 | [`skills/`](skills/) ・ [`slide-templates/`](slide-templates/) |

両者は競合しません。Markdown で素早く作るなら A、デザイン性の高い HTML スライドを作るなら B、という使い分けです。

---

## ディレクトリ構成

```
slideprompt/
├── marp/              # Marp 用 Markdown / CSS テーマ / 出力
│   ├── slide.md
│   ├── style.css
│   ├── 非エンジニアのためのGitHub基本操作_pushとpull.md
│   └── output/        # CI が PDF/PPTX を自動コミット
├── prompts/           # Claude に貼るスライド作成プロンプト雛形
├── skills/            # Claude Code スキル本体
│   ├── slidekit-create/    # /slidekit-create
│   ├── slidekit-templ/     # /slidekit-templ
│   └── SLIDEKIT.md         # SlideKit 詳細ドキュメント
├── slide-templates/   # 11 種類の HTML スライドテンプレート集
├── examples/          # SlideKit の出力サンプル
└── .github/workflows/convert.yml   # marp/ を push 時に自動変換
```

---

## A. Marp 系統の使い方

### ローカルで PDF/PPTX を作る

```bash
npm install -g @marp-team/marp-cli
marp marp/slide.md --theme marp/style.css --pdf --output marp/output/slide.pdf
marp marp/slide.md --theme marp/style.css --pptx --output marp/output/slide.pptx
```

### GitHub Actions で自動変換

`marp/` 配下を編集して push すると、[`.github/workflows/convert.yml`](.github/workflows/convert.yml) が
PDF/PPTX を生成し `marp/output/` に自動コミットします。

### プロンプト雛形を使う

[`prompts/`](prompts/) に Claude へ渡すためのスライド作成プロンプトが置いてあります。
テーマや構成を埋めて Claude にコピペすれば、Marp 形式の `slide.md` を生成できます。

| ファイル | 用途 |
|---|---|
| [01スライド作成プロンプト.md](prompts/01スライド作成プロンプト.md) | フル機能のプロンプト |
| [02簡易版_スライド作成プロンプト.md](prompts/02簡易版_スライド作成プロンプト.md) | 短縮版 |
| [11プレゼンテーション資料作成事例,構成から図解まで一気通貫 .md](prompts/11プレゼンテーション資料作成事例,構成から図解まで一気通貫%20.md) | 構成→図解までの一気通貫例 |
| [非エンジニアが知るべきGitHubの活用方法と事例.md](prompts/非エンジニアが知るべきGitHubの活用方法と事例.md) | サンプルテーマ用プロンプト |

---

## B. SlideKit（Claude Code スキル）の使い方

詳細は [`skills/SLIDEKIT.md`](skills/SLIDEKIT.md) を参照してください。要点だけ抜粋します。

### インストール

```bash
claude install-skill https://github.com/spenda-agency/slideprompt
```

または `skills/slidekit-create/`、`skills/slidekit-templ/` の中身を `~/.claude/skills/` 配下にコピーします。

### Claude Code 内で実行

```
/slidekit-create     # 新規 HTML スライドプレゼンテーションを作成
/slidekit-templ      # 既存 PDF を HTML スライドテンプレートに変換
```

### 付属テンプレート（11 種）

[`slide-templates/`](slide-templates/) に 11 種類の HTML テンプレートが収録されています。
詳細・配置手順は [`slide-templates/README.md`](slide-templates/README.md)。

| ニックネーム | 用途 |
|---|---|
| abc-navy | ビジネスプレゼン基本（Navy + Gold） |
| venture-split | ベンチャー向けピッチ（Orange + Green） |
| biz-plan-blue | 事業計画書（Blue + Amber） |
| greenfield | 新規事業提案（Forest Green） |
| novatech | スタートアップ紹介（Navy + Orange） |
| skyline | 次世代ビジネス戦略（Cyan + Red） |
| ai-proposal | AI 導入プロジェクト提案書 |
| customer-experience | 顧客体験 / CX 提案 |
| ai-tech | AI 技術プレゼン |
| marketing-research | 市場調査レポート |
| digital-report | デジタルビジネス戦略レポート |

---

## 動作環境

- Marp 系統: Node.js + Marp CLI
- SlideKit 系統: Claude Code、`/slidekit-templ` 利用時は Poppler（`pdftoppm`）、PPTX 化時は別途 [`pptx` スキル](https://github.com/anthropics/claude-code-agent-skills/tree/main/skills/pptx)

## ライセンス

MIT
