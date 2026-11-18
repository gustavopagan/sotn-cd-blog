# sotn-cd-blog

Development log of the Symphony of the Night port to the Sega Mega CD.

- `posts/`: posts in Markdown (one file per post).
- `src/`: page template and `build.py`, which turns a post into `public/index.html`.
- `public/`: the site Netlify serves (no build step on Netlify).

Build: `python3 src/build.py posts/000-why.md`
