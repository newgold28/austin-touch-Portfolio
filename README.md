# Austin's Touch — Portfolio

3D portfolio site for **Austin**, graphic designer and Founder & CEO of Touch Creative Agency.

## The pages

| File | What it is |
|---|---|
| `index.html` | Home: 3D avatar hero (eyes follow the cursor or a finger), About + swinging badge, card tunnel, 3D work dome, brands, services, contact strip, ink-reveal footer |
| `work.html` | All work, Netflix-style: featured banner, category chips, rows, Top 10, TikTok row, design viewer. Open one category with `work.html?c=logo`, or one brand with `work.html#brand-d-gadgets` |
| `contact.html` | Contact page with a brief builder that opens WhatsApp with the message already written, plus the 3D "A" |
| `cv.html` / `cv.pdf` | Plain CV page and its PDF download |
| `img/` | His designs (w01–w16) |
| `vendor/three.module.js` | The 3D engine (three.js), stored locally so the site doesn't depend on a CDN |

The site is plain HTML and needs no build step to run. Upload the top-level files to any static host:
- **Vercel:** import this repo with the framework preset set to "Other".
- **GitHub Pages:** Settings → Pages → deploy from the `main` branch, root folder.

## Editing

The editable files are in `source/`. The pages at the top level are built from them.

1. `cd source && npm i @fontsource/bebas-neue @fontsource/montserrat` (fonts get packed into the pages)
2. Edit `src.html` (home), `work_src.html`, `contact_src.html`, `cv_src.html`, or `menu_snip.html` (phone menu)
3. `python3 build.py`, which writes the built pages into `source/dist/`
4. Copy `source/dist/*.html` over the top-level files

Quick changes inside `build.py`:
- `NAME = 'Austin'`: the name used everywhere
- `WORKS = [...]`: design titles, brands and categories (`flyer`, `party`, `logo`, `social`)
- `VIDEOS = []`: add TikTok clips, e.g. `[["vid/v01.mp4", "Making a rave flyer"]]`, and put the MP4s in `vid/`
- `%%AGENCY_URL%%`: set to the Touch Creative Agency website

Still to fill in: the CV years, tools and education (marked in blue `[brackets]` in `cv_src.html`), and the agency link.
