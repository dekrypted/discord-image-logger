# Discord Image Logger
**DISCLAIMER:** This is not a "one-click" token logger. This uses Discord's "Open Original" feature to create a website which Discord previews as an Image, but when clicked, actually logs your IPs! Any "one-click" image loggers (especially ones that aren't open source) are 100% a scam. Do not use them.

---

# How to use it?
Replace "WEBHOOK" with a Discord Webhook. <br>
Also, replace 'link to image here' with the link to your Image!
```py
webhook = 'WEBHOOK'
bindata = requests.get('link to image here').content
```

**Example:** <br>
```py
webhook = 'https://discord.com/api/webhooks/6969/420420420'
bindata = requests.get('https://images.google.com/rickroll').content
```

Once finished, use a **Web Host** which supports **Backend Python Runtimes**, I personally use [<ins>Vercel.</ins>](https://vercel.com) <br>
Every Web Host functions different, so you'll have to **look up their documentation**. <br>
For example, if you were to use **000webhost** you'd look up `"000webhost python backend api"` <br>
Then, just follow the setup instructions! <br>

---

# Support/Help
If you need support, please [make an issue!](https://github.com/dekrypted/discord-image-logger/issues) <br>
However, please attempt to set it up yourself before making an issue. Chances are you will figure it out on your own.

---

# Closing Statements/Support Me!
**Discord Image Logger** was created by DeKrypt. (Me!) <br>
**Support me and my projects!** Please 🌟 this repository and follow my GitHub!

**Donations are always appreciated!** More information about donations on my main profile page! <br>
Thank you very much, have a wonderful day! :D
