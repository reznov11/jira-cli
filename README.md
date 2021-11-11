# jira-cli
JIRA Command Line Interface

### Install requirements
`python3 -m pip install -r requirements.txt`

### Show script help
`python akcli.py -h`

### Dump projects
`akcli --dump projects`

### Dump issues of a project
`akcli --dump issues --projectKey=PUT PROJECT KEY`

### Dump specific issue
`akcli --dump issues --issueKey=PUT ISSUE KEY`

### Create an issue
`akcli --create issue --issueSummary=YOUR SUMMARY --issueDescription=YOUR DESCRIPTION --issueType=TYPE OF ISSUE --projectId=PUT PROJECT KEY`

### Transit an issue

**transitionId** is the code of the transition, for example:
- To Do = 11
- In Progress = 21
- Done = 31

`akcli --transition --transitionId=PUT STATUS CODE --issueKey=`

### Comment on issue
`akcli --comment --commentBody=YOUR COMMENT --issueKey=PUT ISSUE KEY`

### Close an issue
`akcli --close --issueKey=PUT ISSUE KEY`

### Delete an issue
`akcli --delete --issueKey=PUT ISSUE KEY`

### Filter

**Get only my issues**
`akcli --filter --myIssues --projectKey=PUT PROJECT KEY`


If you want to get from multi projects, you can type other projects keys like the following:

`akcli --filter --myIssues --projectKey="FIRST KEY, SECOND KEY"`

**Get issues by type**

`akcli --filter --issuetype="Task, New Feature"`



**Get issues by text**

`akcli --filter --text='TYPE ISSUE TITLE, DESCRIPTION OR ANYTHING'`


**Get issues by status**

`akcli --filter --status='To Do, In progress'`
