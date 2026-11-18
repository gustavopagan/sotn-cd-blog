# sotn-cd-blog

Development log of the Symphony of the Night port to the Sega Mega CD.

- `posts/`: posts in Markdown (one file per post).
- `src/`: page template and `build.py`, which turns a post into `public/index.html`.
- `public/`: the site Netlify serves (no build step on Netlify).

Build: `python3 src/build.py` (adds `--drafts` for a local preview; never push a draft build).
Images from Wikimedia Commons: `python3 src/commons.py busca "..."`, then `baixa "File:..." public/img/NN-name.jpg` (prints the credit line).
