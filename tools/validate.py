"""Validate the generated static site without third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.assets, self.headings = [], [], [], []
        self.canonical = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.headings.append(int(tag[1]))
        if tag == 'a':
            self.links.append(a.get('href', ''))
        if tag in ['img', 'script'] and a.get('src'):
            self.assets.append(a['src'])
        if tag == 'img':
            assert 'alt' in a, 'Image missing alt attribute'
        if tag == 'link':
            if a.get('rel') == 'canonical':
                self.canonical.append(a['href'])
            elif a.get('rel') in ['stylesheet', 'icon', 'apple-touch-icon']:
                self.assets.append(a['href'])

def validate():
    source = json.loads((ROOT / 'tools/content.en.json').read_text(encoding='utf-8'))
    parsed = {name: Page((ROOT / name).read_text(encoding='utf-8')) for name in source}
    for name, page in parsed.items():
        assert page.headings.count(1) == 1, (name, 'Expected one H1')
        assert len(page.ids) == len(set(page.ids)), (name, 'Duplicate ID')
        assert len(page.canonical) == 1 and page.canonical[0].startswith('https://probotz.eu/'), name
        previous = 0
        for level in page.headings:
            assert level <= previous + 1, (name, 'Skipped heading level')
            previous = level
        for ref in page.links + page.assets:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            target = url.path.lstrip('/') if url.path else name
            target = target or 'index.html'
            assert (ROOT / target).is_file(), (name, 'Missing target', ref)
            if url.fragment:
                assert url.fragment in parsed[target].ids, (name, 'Missing anchor', ref)
    sitemap = ET.parse(ROOT / 'sitemap.xml')
    locations = [e.text for e in sitemap.findall('.//{*}loc')]
    expected = [page.canonical[0] for name, page in parsed.items() if not source[name].get('noindex')]
    assert locations == expected, 'Sitemap differs from indexable pages'
    config = json.loads((ROOT / 'staticwebapp.config.json').read_text())
    assert config['responseOverrides']['404'] == {'rewrite': '/404.html', 'statusCode': 404}
    assert any(r.get('redirect') == '/dentalcharz.html#proposal' and r.get('statusCode') == 301 for r in config['routes'])
    print(f'PASS: {len(parsed)} pages, headings, assets, internal links/anchors, canonicals, sitemap and routing configuration')

if __name__ == '__main__':
    validate()
