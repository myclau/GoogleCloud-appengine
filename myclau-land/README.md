Current app
===========
https://myclau-land.appspot.com/

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
=========
Install the appenginelancher from https://cloud.google.com/appengine/docs/standard/python/download#appengine_sdk

Download the sourcecode
if you already deployto  google cloud, you want use that to debug
	appcfg.py -A [YOUR_PROJECT_ID] -V [YOUR_VERSION_ID] download_app [OUTPUT_DIR]

From Git
	git clone https://github.com/myclau/GoogleCloud-appengine.git $WORKDIR


Create a new project and link to the checkout source location.
Then click run.
Default url for the app is localhost:8080


	
