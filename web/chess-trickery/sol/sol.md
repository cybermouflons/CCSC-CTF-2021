# Solution

<details>
 <summary>Reveal Spoiler</summary>
Target @ http://172.16.3.11

The application is vulnerable to Web Cache Deception; a type of attack that forces caching servers to store and reveal sensitive information. The attack hinges on "path confusion" – manipulating URL paths to confound the cache server into classifying sensitive HTTP responses as public, cacheable documents.

The application is behind a reverse proxy (Nginx) which caches static files (e.g. css,jpg) to improve performance.

Consider a dynamic, non-cacheable page that contains sensitive user account information, say /account.php.

To get the proxy server to store a cached copy of the page, a malicious user might add a suffix to the path to make it look like a static, public asset – `/account.php/nonexistent.jpg`.

If a victim who is logged in the application visits the aforementioned URL, it would cause their account data to be cached on the proxy server.

After that, all the attacker has to do is send a GET request for the forged URL to the edge server and receive a copy of the cached data.

```bash
curl -ski -X POST -d "name=test&email=test&subject=test&link=http%3A%2F%2F172.16.3.11%2Faccount.php%2Fdoesnotexist.css&message=test" http://172.16.3.11/submit-message.php

curl -ski http://172.16.3.11/account.php/doesnotexist.css -H "Accept-Encoding: gzip, deflate" --compressed
```

</details>
