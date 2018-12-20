#!/usr/local/bin/python3

import pygit2
from urllib.request import urlopen, Request
import sys
import json
import os
import configparser


CONFIG_PATH="~/.circleci/build_status"

config_params = None
# SOURCE_CONTROL="bitbucket"
# USERNAME="accezz-io"
# ACCESS_TOKEN = "9dde9f18b8458965a91800745af8ffcb95ed44db"

def load_config():
	cfg_path = os.path.expanduser(CONFIG_PATH)
	if not os.path.isfile(cfg_path):
		raise FileNotFoundError("You must create {0} configuration file".format(CONFIG_PATH))
	config = configparser.ConfigParser()
	config.read(cfg_path)
	return config['build_status']
	

def base_circle_params():
	global config_params
	return {"source_control": config_params['source_control'], "username": config_params['project_username']}

def format_circle_token_url(url):
	global config_params
	return url + "?circle-token="+config_params['user_token']

def get_json_from_circle(url):
	final_url = format_circle_token_url(url)

	r = Request(final_url)
	r.add_header('Content-Type', 'application/json')
	r.add_header('Accept', 'application/json')
	response = urlopen(r)
	data = response.read()
	encoding = response.info().get_content_charset('utf-8')

	return json.loads(data.decode(encoding))

def get_builds(project, branch):
	
	params = base_circle_params()
	params["project"] = project
	params["branch"] = branch

	url = "https://circleci.com/api/v1.1/project/{source_control}/{username}/{project}/tree/{branch}".format(**params)

	result = get_json_from_circle(url)
	targetObj = result[0]
	print("Build Name: {0}".format(targetObj["subject"]))
	print ("Build URL: {0}".format(targetObj["build_url"]))
	print ("Build Status: {0}".format(targetObj["status"]))
	print ("Workflow: {0}".format(targetObj["workflows"]["job_name"]))

def main():
	global config_params
	try:
		progname, path = sys.argv
	except:
		path = os.getcwd()

	config_params = load_config()

	proj_name = os.path.basename(path)
	r = pygit2.Repository('.')
	branch = r.head.shorthand

	get_builds(proj_name, branch)
	return 0

if __name__ == "__main__":
	sys.exit(main())