Vanity import paths:

https://sagikazarmark.hu/blog/vanity-import-paths-in-go/

- Get a lib - done
- Get a static site - done
- Host in GitHub pages

## Vangen Notes

repositories[].prefix is the name of the packages
repositories[].subs[] is the name of subpackages

It doesn't seem to generate a root index.html...

GitHub Pages only wants to publish from / or /docs/ so let's use:

```
vangen -out=docs/
```

I think I need to wait until 5PM Sunday for HTTPS to work.

GitHub might also not be happy with me using a subdomain for this? I need bbkane.com to point to netlify
