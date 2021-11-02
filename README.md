# jira-cli
JIRA Command Line Interface

### Install requirements
`python3 -m pip install -r requirements.txt`

### Run the script
`

	positional arguments:
	  {issue}               sub commands for creating issue
	    issue               create issue is sub-command with sub-commands

	optional arguments:
	  -h, --help            show this help message and exit
	  --issueKey ISSUEKEY   issue key or id
	  --projectKey PROJECTKEY
	                        issue key or id
	  --create              create an issue
	  --dump [{issues,projects}]
	                        dump projects, issues, (default: None)
	  --delete              delete an issue
	  --close               delete an issue
	  --transition          transit an issue
	  --transitionId {11,21,31,41}
	                        transit an issue
	  --comment             comment on issue
	  --commentBody COMMENTBODY
	                        comment body
`
