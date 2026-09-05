"""Generate the static English site: python tools/build.py.

The shared shell and page content are separated so another language can reuse
the layout. Generated HTML is committed; Azure needs no build dependencies.
"""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parent.parent
CONTENT = json.loads((ROOT / 'tools/content.en.json').read_text(encoding='utf-8'))
ORIGIN = 'https://probotz.eu'
# TODO(owner): supply verified public contact email, business ID and address.
EMAIL = None

def link(href, label, kind='secondary'):
    return f'<a class="button button-{kind}" href="{href}">{label}</a>'

def build():
    nav = [('index.html', 'Home'), ('dentalcharz.html', 'DentalCharz'), ('work.html', 'Work'), ('about.html', 'About'), ('contact.html', 'Contact')]
    organisation = {'@context': 'https://schema.org', '@type': 'Organization', '@id': ORIGIN + '/#organisation', 'name': 'Probotz Consultancy Oy', 'url': ORIGIN + '/', 'logo': ORIGIN + '/assets/apple-touch-icon.png', 'location': {'@type': 'Country', 'name': 'Finland'}}
    for filename, page in CONTENT.items():
        canonical = ORIGIN + ('/' if filename == 'index.html' else '/' + filename)
        navigation = ''.join(f'<a href="/{path}"' + (' aria-current="page"' if filename == path else '') + f'>{label}</a>' for path, label in nav)
        metadata = organisation
        if filename == 'dentalcharz.html':
            metadata = {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': 'DentalCharz', 'applicationCategory': 'BusinessApplication', 'operatingSystem': 'Web browser', 'url': canonical, 'description': page['description'], 'creator': {'@id': ORIGIN + '/#organisation', '@type': 'Organization', 'name': 'Probotz Consultancy Oy'}}
        robots = '<meta name="robots" content="noindex, follow">' if page.get('noindex') else ''
        body = page['body']
        for topic, subject in [('lab', 'DentalCharz enquiry'), ('project', 'Software project enquiry')]:
            if EMAIL:
                from urllib.parse import quote
                contact = link('mailto:' + html.escape(EMAIL) + '?subject=' + quote(subject), 'Email Probotz', 'primary')
            else:
                contact = '<p class="contact-status">Direct email enquiries are not available on this website yet.</p><!-- TODO(owner): add verified public enquiry email in tools/build.py. -->'
            body = body.replace('{{contact_' + topic + '}}', contact)
        output = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page['title'])}</title>
  <meta name="description" content="{html.escape(page['description'], quote=True)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Probotz Consultancy Oy">
  <meta property="og:locale" content="en_GB">
  <meta property="og:title" content="{html.escape(page['title'], quote=True)}">
  <meta property="og:description" content="{html.escape(page['description'], quote=True)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{ORIGIN}/assets/social-card.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Probotz Consultancy Oy — focused software, built around real work">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#315f58">
{robots}
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/assets/favicon.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="stylesheet" href="/styles.css">
  <script type="application/ld+json">{json.dumps(metadata, ensure_ascii=False)}</script>
  <script src="/script.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <a class="logo" href="/" aria-label="Probotz home"><span class="logo-mark" aria-hidden="true">P</span><span>Probotz</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span class="sr-only">Open navigation</span><span></span><span></span><span></span></button>
    <nav class="site-nav" id="site-nav" aria-label="Main navigation">{navigation}<a class="button button-ghost login-link" href="https://dental.probotz.eu/login">DentalCharz login</a></nav>
  </header>
  <main id="main" tabindex="-1">{body}</main>
  <footer class="site-footer">
    <div><a class="logo footer-logo" href="/"><span class="logo-mark" aria-hidden="true">P</span><span>Probotz</span></a><p>Probotz Consultancy Oy · Finland<br>Focused software, built around real work.</p></div>
    <nav aria-label="Footer navigation"><a href="/dentalcharz.html">DentalCharz</a><a href="/work.html">Customer work</a><a href="/about.html">About</a><a href="/contact.html">Contact</a><a href="/privacy.html">Privacy</a><a href="/terms.html">Terms</a></nav>
  </footer>
</body>
</html>
'''
        (ROOT / filename).write_text(output, encoding='utf-8')
    urls = [ORIGIN + ('/' if path == 'index.html' else '/' + path) for path, page in CONTENT.items() if not page.get('noindex')]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{url}</loc></url>\n' for url in urls) + '</urlset>\n', encoding='utf-8')
    print(f'Generated {len(CONTENT)} pages and sitemap.xml')

if __name__ == '__main__':
    build()
