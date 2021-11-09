# jira-cli
JIRA Command Line Interface

### Install requirements
`python3 -m pip install -r requirements.txt`

### Dump projects
`akcli --dump projects`

### Dump issues of a project
`akcli --dump issues --projectKey=PUT PROJECT KEY`

### Dump specific issue
`akcli --dump issues --issueKey=PUT ISSUE KEY`

### Create an issue
`akcli --create issue --issueSummary='' --issueDescription='' --issueType=Task --projectId=PUT PROJECT KEY`

### Transit an issue

**transitionId** is the code of the transition, for example:
- To Do = 11
- In Progress = 21
- Done = 31
`akcli --transition --transitionId=PUT STATUS CODE --issueKey=`


### Get help
`python akcli.py -h`

`

	usage: JIRA Command Line Interface [-h] [--issueKey ISSUEKEY] [--projectKey PROJECTKEY] [--create]
	                                   [--dump [{issues,projects}]] [--delete] [--close] [--transition]
	                                   [--transitionId {11,21,31,41}] [--comment]
	                                   [--commentBody COMMENTBODY]
	                                   {issue} ...

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
