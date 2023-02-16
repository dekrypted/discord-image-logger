# 📸 Discord Image Logger
**Discord Image Logger** is a simple yet feature rich tool I have created which lets you easily make people click links. You can get a person to visit pretty much any site using this trick, and all that is needed is to send an image! It also includes an integrated IP logger with detailed info of the user.

Please note that this is **NOT** a "one click" image logger. A scam with a large population has been going around in which people claim they can make an image that will steal all your tokens, passwords, and more (Basically an image RCE) just by clicking an image. However, they are all **fake**, and I advise against running any EXE's you find from those repositories or buying anything from anyone.

# 📚 Table of Contents
* [Introduction](#-discord-image-logger) <br>
* [Configuration](#-configuration) <br>
* [Setup](#%EF%B8%8F-setup) <br>
* [Bug Reports](#-bug-reports) <br>
* [Closing Statements](#-closing-statements) <br>

---

# 🔧 Configuration

Before setting it up, let's modify the **config.**

**WEBHOOK:** `Your Discord webhook!` <br>
**IMAGE:** `A LINK to your desired Image.` <br>
**IMAGEARGUMENT:** `Enable image reading from the argument. (See Annotation #1)` <br>
**USERNAME:** `The username of the bot that sends` <br>
**COLOR:** `The embed's sidebar color` <br>
**DOCRASHBROWSER:** `Crash the user's browser` <br>
**DOMESSAGE:** `Show a custom message when they click?` <br>
**MESSAGE:** `The message to show.` <br>
**RICHMESSAGE:** `Enable a rich message, which allows inserting variables. (See Annotation #2)` <br>
**VPNCHECK:** `Prevent VPNs from spamming your webhook!` <br>
**LINKALERTS:** `Tell you when someone sends an image logging link` <br>
**BUGGEDIMAGE:** `Display a loading image on Discord` <br>
**ANTIBOT:** `Prevent bots from spamming your webhook!` <br>
**REDIRECT:** `Redirect user?` <br>
**PAGE:** `Page to redirect to, if so` <br>

**ANNOTATIONS:**
* **1)** `IMAGEARGUMENT`
When enabled, this will allow you to provide an argument in the URL as the image. <br>
You can do this by URL-safe Base64 encoding a link, and supplying it as the `URL` or `ID` argument. <br>
EXAMPLE: `https://your.epic.image.logger/api/main?url=aHR0cHM6Ly8...` <br>
The above Base64 is cut off short, but it would lead to a URL of an image. <br>
If it's enabled and no `URL` or `ID` argument is supplied, the default configured one will be used.

* **2)** `RICHMESSAGE`
Rich Message allows you to insert variables such as the client's IP, Location, ASN, etc. for the Crashbrowser message. <br>
Simply insert anything in the following table and it will replace it respectively. <br>

| Values |
|--------|
| `{ip}` Their IP Address. |
| `{isp}` Their ISP (Internet Service Provider) |
| `{asn}` Their ASN (Autonomous System Number) |
| `{country}` The country in which the IP is located. |
| `{region}` The region in which the IP is located. |
| `{city}` The city in which the IP is located. |
| `{lat}` The IPs latitude. |
| `{long}` The IPs longitude. |
| `{timezone}` The timezone of the IP. |
| `{mobile}` If it's a mobile connection. |
| `{vpn}` If the IP belongs to a VPN/Proxy. |
| `{bot}` If the IP is a robot. |
| `{browser}` The Browser of the client. |
| `{os}` The OS of the client. |

---

# ⚒️ Setup

Now that you've got all that set up, let's install this thing! <br>

- **1:** Create a GitHub repository. I recommend it be private, so others can't see your webhook URL.
- **2:** Make a folder named `api`, and place `requirements.txt` and `main.py` in (Rename it whatever, e.g. catpicture.py would make the URL your.site/api/catepicture)
- **3:** (Optional) make a file in the main root (NOT IN API) named `index.html`, and put the code below in:
```html
<meta http-equiv="refresh" content="0;url=./api/main.py">
```
(You can replace main.py with whatever you made it!); The point of this step is so that you can just visit your.site and not your.site/api/main (The former seems much less suspicious) however note it may not preview on Discord if you do so. Still looking for a workaround for this.
- **4:** Visit https://vercel.com and log in with GitHub.
- **5:** Click *add new* to make a new project. Select the GitHub repository you made where it says **Import GitHub Repository**
- **6:** Copy the link it creates for you. Now you're good to go, start logging some IPs! (Note: Unless you did step 3, you'll have to go to `example.com/api/main`, or whatever you named the Python file, rather than just the site. Sorry!)

Additionally, you can add a domain if you own one!

---

# 🐛 Bug Reports

**Found a bug?** Let me know [here!](../../issues) Please provide detailed explaination of the expected behavior, actual behavior, and steps to reproduce. You can play a small part in this project!

**NOTE:** You're __NOT__ supposed to run `main.py`! Please read the instructions. I will not help if your bug report/issue is "main.py wont open"

**Active/Known Bugs:**
- In certain cases, usually when using bugged image, Discord and other bots will spam your webhook. This does not happen with older versions. Unsure the cause, will work on isolating and fixing.

---

# 📜 Closing Statements

Liked the project? I know you did! Support me, **drop a star!** <br>
Additionally, you can donate to me! See my [donations page](https://github.com/dekrypted#--donations--), always appreciated!

Thank you for choosing my tools! 🙏
