# Probotz project website

Static HTML/CSS/JavaScript, using the existing Probotz palette and components. Probotz Consultancy Oy is a deliberately small home for personal software projects, experiments and infrastructure. DentalCharz is an ongoing side project; Falcon is a goodwill website project for a local club.

## Edit and preview

- Edit English page content and metadata in `tools/content.en.json`.
- Edit the shared shell and public email in `tools/build.py`.
- Run `python tools/build.py`, then commit the generated root HTML and sitemap with the source changes.
- Preview with `python -m http.server 4173 --bind 127.0.0.1` at `http://127.0.0.1:4173`.
- Run `python tools/validate.py` and `node --check script.js`.

Python uses only the standard library. There is no TypeScript project or Node build. The existing Azure workflow deploys committed static files with `skip_app_build: true`. English content is separated from the shared shell; no Finnish translation is implemented.

## Current structure

- `/`: short introduction, DentalCharz and Falcon project cards, brief About and email contact.
- `/dentalcharz.html`: detailed current workflows, illustrative preview, integrations and a development note. DS Core remains explicitly in development.
- `/work.html#falcon`: concise Falcon portfolio entry, screenshot and external link; retained at the existing URL for compatibility.
- `/about.html`: short personal description of the company's role alongside the owner's day job.
- `/contact.html`: casual contact via `jooa@probotz.eu`. Old `#lab` and `#project` fragments remain as compatibility anchors.
- `/pricing.html` and `/pricing`: Azure 301 to `/dentalcharz.html#project-status`. The HTML fallback also points there. The old product `#proposal` anchor remains beside the development note for existing/cached links, but no proposal offering is presented.
- `/privacy.html`, `/terms.html`: limited factual/publication-status notices, noindexed; not approved legal documents.
- `/404.html`: custom Azure error response with HTTP 404 retained.

Navigation is Projects, DentalCharz, About and Contact. DentalCharz login remains on its page and in the footer. Agency/service lists, customer-acquisition copy, qualification prompts and sales CTAs have been removed. Metadata, structured data and the social preview use the same small-project positioning.

## Assets

- `assets/falcon-home.png`: retained real 1440 × 1080 screenshot captured from the supplied development site, `https://zealous-ground-0b3ac8a03.7.azurestaticapps.net/`, during the earlier revision. The standalone project page identifies it as a development capture. Public links now use `https://jousiammuntaseurafalcon.fi/`, as requested by the owner.
- DentalCharz: retained HTML workflow illustration, explicitly labelled as an illustration rather than an application screenshot. No genuine application screenshots were present in the repository.
- Icons retain the existing P mark. `assets/social-card.png` now reads “A small home for software projects.”

## Outstanding facts and publication details

- Public contact email is supplied and implemented. Business ID and registered address remain unverified and are not invented.
- Approved privacy/terms text is still needed if those documents are to be published. The website has no analytics, tracking cookies, browser storage or form backend. Hosting/access logs, email handling and the separate DentalCharz application need consideration in approved privacy information.
- Genuine, anonymised DentalCharz screenshots can replace the illustration when available. Capabilities reflect the owner's supplied brief; this marketing repository does not verify the application implementation. Finvoice/Peppol-specific claims remain omitted.
- On 2026-09-07, this environment could not resolve Falcon's domain. The owner-requested public link is included, but live availability remains unverified here.
- On 2026-09-07, `https://probotz.eu/` failed certificate verification. A public HTML fetch with certificate checking bypassed returned Azure's “404 Web Site not found” page. This is an observation from this environment, not a diagnosis of the production configuration. No DNS, hosting or certificate settings were changed.

## Validation and deployment

Static generation, HTML/link/asset/heading/canonical/sitemap checks and JavaScript syntax checks are available through the commands above. Local browser checks use Edge with temporary Playwright/axe tools at mobile, tablet and desktop widths, including navigation with and without JavaScript. The simple Python server does not emulate Azure redirects, headers or error overrides; those require a deployment smoke check.

This revision is local only; no deployment was performed.
