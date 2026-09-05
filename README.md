# Probotz company website

Static HTML/CSS/JavaScript, deployed by the existing Azure Static Web Apps workflow. Probotz Consultancy Oy is the company; DentalCharz is its flagship product; Falcon is customer work.

## Edit and preview

- Edit English page content and metadata in `tools/content.en.json`.
- Edit the shared HTML shell and verified contact configuration in `tools/build.py`.
- Run `python tools/build.py` (Python standard library only). Commit the generated root HTML files and `sitemap.xml` with the source changes.
- Run `python -m http.server 4173 --bind 127.0.0.1` and open `http://127.0.0.1:4173`. Root-relative links require HTTP rather than opening files directly.
- Styles remain in `styles.css`; progressive navigation enhancement is in `script.js`.

The English content is separated from the shared shell to support another language later. No Finnish translation or language switcher is implemented. Azure still deploys committed static files with `skip_app_build: true`; there is no Node build or TypeScript project.

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Company homepage; retains the former `#product`, `#workflow` and `#what-we-build` entry points where relevant |
| `/dentalcharz.html` | Flagship product, six workflow themes, integrations and `#proposal` |
| `/work.html#falcon` | Falcon customer case study |
| `/about.html` | Company philosophy and scope |
| `/contact.html#lab`, `/contact.html#project` | Two enquiry paths |
| `/privacy.html`, `/terms.html` | Limited publication-status/technical notices, not approved legal documents; noindexed |
| `/pricing.html` | Azure 301 to `/dentalcharz.html#proposal`; static fallback for simple preview servers |
| `/404.html` | Custom error page; Azure response override retains HTTP 404 |

Canonical URLs, per-page descriptions/titles, Open Graph metadata, social card, favicon, touch icon, robots and sitemap are included. Organisation structured data identifies Probotz; the product page identifies DentalCharz as a SoftwareApplication created by Probotz. No prices, reviews, ratings or certifications are supplied. Azure routing and response overrides follow [Microsoft's configuration documentation](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration). The plain Python preview server does not emulate Azure redirects, response overrides or headers; check those on the deployment preview.

## Owner input required before production

1. **Public enquiry email:** no email address was present in repository content or configuration. Set `EMAIL` in `tools/build.py`, then regenerate. Both enquiry paths will receive working mail links with distinct subjects. Until supplied, the page explicitly says direct email enquiries are unavailable. No form backend or guessed address was added.
2. **Company details:** verify the business ID and registered/public address, plus a phone number only if it should be shown. Currently only the supplied legal company name and Finland are displayed. Add verified details to contact content and structured data as appropriate.
3. **Approved privacy notice:** supply controller identity/contact, actual hosting and access-log processing, enquiry handling, purposes/legal bases, processors/recipients, transfers, retention, rights and supervisory authority information. Supply or link approved DentalCharz privacy/DPA information separately where applicable. The current technical notice is deliberately incomplete and noindexed.
4. **Approved terms:** supply the DentalCharz subscription/service terms and any company website or project terms that should be public, with correct contracting company details. No binding clauses have been invented. Replace the publication-status notice and remove `noindex` after approval.
5. **Hosting privacy review:** repository code contains no analytics, tracking pixels, cookies, local/session storage, forms, embedded third-party media or external fonts. No analytics or cookie banner was added. Hosting/access logs and the separate DentalCharz application cannot be assessed from this marketing repository. Review those when approving the privacy notice and reassess consent if tracking is introduced.
6. **Falcon launch:** `jousiammuntaseurafalcon.fi` did not resolve from this environment during implementation. Verify DNS, valid HTTPS and that it serves the new site, then replace the launch-status sentence with a visit link in the case study. The Azure development URL is not linked in public site pages.
7. **DentalCharz proof:** no genuine application screenshots or application source were found. Supply approved, anonymised screenshots to replace the labelled illustrative preview. Product descriptions use the owner's supplied current workflow brief; this repository cannot independently verify application capabilities. Finvoice/Peppol specifics were omitted pending confirmation. DS Core is explicitly in development.

## Visual assets and provenance

- `assets/falcon-home.png`: real 1440 × 1080 browser capture of the supplied Falcon development site, reviewed against its rendered homepage and published bundle. The bundle also confirmed the Finnish navigation and historical document archive. Source: `https://zealous-ground-0b3ac8a03.7.azurestaticapps.net/`. No fake browser frame, customer quote, result metric or commercial detail was added.
- DentalCharz preview: reuses the existing case/card/step styling with explicitly illustrative, non-personal content. It is labelled as an illustration, not a screenshot.
- `assets/favicon.svg`, `favicon.png`, `apple-touch-icon.png`, `social-card.png`: rendered from the existing Probotz P mark, palette and typography. No generated photography or external integration logos.

## Verification

Run `python tools/build.py`, `python tools/validate.py` and `node --check script.js` for dependency-free checks. Browser verification was performed with installed Edge through temporary Playwright and axe tooling at 375, 768 and 1440 px: all nine pages, images, internal links/anchors, single H1, horizontal overflow, WCAG A/AA checks, mobile navigation, Escape handling and navigation without JavaScript. Automated accessibility checks supplement visual and keyboard checks; they are not a certification.

No deployment was performed. Live Azure redirects, custom error response and production domain behaviour still need a deployment smoke check.
