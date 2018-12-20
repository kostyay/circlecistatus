# circlecistatus
Get current build status of a repo on circleci from CLI

# Installation
* You need to install 
* Python3 is required
* pip3 is required: `sudo apt install python3-pip`
* Clone the repo `git clone https://github.com/kostyay/circlecistatus.git`
* `apt-get install libgit2-dev`
* `pip3 install -r requirements.txt`
* Create an alias in your `.bashrc`: `alias bs=/path/to/build_status.py`.
  * bash: ```echo alias bs=`pwd`/build_status.py >> ~/.bashrc```
  * zsh: ```echo alias bs=`pwd`/build_status.py >> ~/.zshrc```
* Run `bs` from project directory to get the current build status

# Usage
Create a configuration file at the following path: `~/.circleci/build_status`
It should contain the following contents:
```
[build_status]
user_token = <<REPLACE>>
project_username = <<REPLACE>>
source_control = <<REPLACE>>
```
* user_token - Go to CircleCI and generate a personal API token token (https://circleci.com/account/api). 
* project_username - The repository you are working it. Normally when viewing builds from circle ci you can decude it from the URL. For example `https://circleci.com/bb/<<project_username>>/<<project>/<<build_id>>`
* source_control - Either `bitbucket` or `github`