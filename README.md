# circlecistatus
Get current build status of a repo on circleci from CLI

# Installation
* Python3 is required
* Clone the repo `git clone git@github.com:kostyay/circlecistatus.git`
* `pip3 install -r requirements.txt`
* Create an alias in your `.bashrc`: `alias bs=/path/to/build_status.py`
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