"""PPT詳細テンプレの Marp テーマをビルドする。

templates/spenda-detail.src.css の __BAND__ / __COVER__ / __LOGO__ を
templates/assets/ の画像の data URI に置き換え、themes/spenda-detail.css を出力する。
（画像を埋め込むことで、mdファイルの場所に関係なく背景画像が表示される）

使い方: python3 templates/build_theme.py
"""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "templates" / "assets"
TOKENS = {
    "__BAND__": ("band.jpg", "image/jpeg"),
    "__COVER__": ("cover-bg.jpg", "image/jpeg"),
    "__LOGO__": ("logo.png", "image/png"),
}

css = (ROOT / "templates" / "spenda-detail.src.css").read_text(encoding="utf-8")
for token, (name, mime) in TOKENS.items():
    data = base64.b64encode((ASSETS / name).read_bytes()).decode()
    css = css.replace(token, f"data:{mime};base64,{data}")
out = ROOT / "themes" / "spenda-detail.css"
out.write_text(css, encoding="utf-8")
print(f"wrote {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)")
