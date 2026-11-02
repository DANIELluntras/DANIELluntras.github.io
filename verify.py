from pathlib import Path
from html.parser import HTMLParser

root = Path(__file__).parent
pages = sorted((root / "proiecte").glob("*.html"))
assert len(pages) == 20, f"Expected 20 pages, found {len(pages)}"

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.urls += [value for key, value in attrs if key == "href"]

for page in [root / "index.html", root / "404.html", *pages]:
    parser = Links()
    parser.feed(page.read_text(encoding="utf-8"))
    for url in parser.urls:
        if url.startswith("/"):
            target = root / url.lstrip("/")
            if url == "/": target = root / "index.html"
            assert target.is_file(), f"Broken link in {page.name}: {url}"

home_links = Links()
home_links.feed((root / "index.html").read_text(encoding="utf-8"))
for page in pages:
    assert f"/proiecte/{page.name}" in home_links.urls, f"Missing home link: {page.name}"
assert (root / "style.css").is_file()
assert (root / "app.js").is_file()
print(f"Verified {len(pages)} project pages and all internal links.")
