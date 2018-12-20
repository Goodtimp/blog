# -*- coding: utf-8 -*-
from backsite.settings import MEDIA_URL 

def AddMEDIA_URLToUrl(url):
  if url.find(MEDIA_URL.split("/")[1])>0:
    return "/".join([MEDIA_URL+url])
  return url