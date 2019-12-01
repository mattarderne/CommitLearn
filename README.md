# CommitLearn
Curated Podcast Learning Paths

[XML Example](https://s3.amazonaws.com/aws-website-matt-fe1iw/ai-podcasts-img.xml) (open with Podcast App on your iPhone)

## Infrastructure
* XML files hosted on S3 as file feeds
* Development on Github, 1 branch per topic, prefix `prod_` indicates a branch for Hosting on Production

## How to contribute
* Fork a branch and modify XML to suit your learning path, host on S3 to test XML
* PR into a `prod_` branch to request review into Production

## Roadmap
1. Build a POC example **3/5**
1. Setup Git -> AWS integration (AWS to host XML of master branches) **0/5**
1. Build [Landing Page](https://s3.amazonaws.com/aws-website-matt-fe1iw/index.html) website **0.1/5**
1. Build Onboarding [test](https://www.typeform.com/help/create-a-quiz/) for customized learning path **0/5**
1. Setup monetization / patreon account **0/5**
1. ...
1. ...? Learning? Amazing!

## Future Features
1. Pay contributors per commit for any advertising revenue
1. Customized learning paths to give customized learning experience
   * quiz to onboard and measure baseline & expected outcomes
1. Audio-to-Text to more accurately identify scope of content
1. App to quiz listeners and measure learning (competency based education)
1. Custom recorded bridging audio to summarize contents and segue from one concept to another

## Issues / Stucks
1. Content
1. Ease of use of opening XML URLs


[Google Doc for now](https://docs.google.com/spreadsheets/d/1KaFdfvQieXUIvZQYRpBuDB2mJC7Ol5nqYB-CgscENa4/edit#gid=0)


# Principles 
## Why
* Encourage & Enable Learning
* Open access, open contribution
* Broad access to knowledge is essential to humanity
* Another medium of learning

## How
* Long format audio (podcasts)
* Specific Learning Outcomes
* Focus on AI, Philosophy, Ethics
* Community curated through Github & rewarded by number of commits
* Generate revenue through Patreon / other?

## What
1. **Listeners** Advertising > Website > Appropriate Stream > App or XML
1. **Contributors** Create Learning Design > Identify Podcasts > *\*Record content* > Submit for Review 

# Python app

```
python3 -m venv ~/.virtualenvs/commitlearn
source ~/.virtualenvs/commitlearn/bin/activate
pip install -r requirements.txt 
```