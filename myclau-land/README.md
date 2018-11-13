Current app
===========
default:
https://myclau-land.appspot.com/
where to go:
https://myclau-land.appspot.com/where2go

Checkout code
============================
open google cloud terminal

	WORKDIR=~/src/mywork/mycloudapi
	git clone https://github.com/myclau/GoogleCloud-appengine.git $WORKDIR
	cd $WORKDIR


How to build and Deploy
=======================

cd into project:
	
	#if you in google cloud terminal
	cd ~/src/mywork/mycloudapi
	#else just goto your checkout location

if you not using google cloud terminal please install gcloud from https://cloud.google.com/sdk/install

Do initial setup for local gcloud sdk (in google cloud terminal you can skip this)

	gcloud auth login
	gcloud config set project <your-project-name>

Deploy:

	gcloud app deploy app.yaml
	
Check logs

	gcloud app logs tail -s default
	
Open app in brower

	gcloud app browse

For local Debug
===============

Install the appenginelancher
----------------------------

https://cloud.google.com/appengine/docs/standard/python/download#appengine_sdk


Use dev_appserver.py to test app in local
--------------------

It will runtime update the appserver, if there are any changes


	dev_appserver.py app.yaml

Debug url (in google cloud):

https://ssh.cloud.google.com/devshell/proxy?authuser=0&port=8080

Debug url in local:

http://localhost:8080/

Extra: Download the sourcecode
-----------------------
if you already deployto  google cloud, you want use that to debug

	appcfg.py -A [YOUR_PROJECT_ID] -V [YOUR_VERSION_ID] download_app [OUTPUT_DIR]


	
