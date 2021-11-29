# jira-cli
JIRA Command Line Interface

### Install requirements
`python3 -m pip install -r requirements.txt`

### Show script help
`akcli -h`

### Dump projects
`akcli --dump projects`

### Dump issues of a project
`akcli --dump issues --projectKey=PUT PROJECT KEY`

### Dump specific issue
`akcli --dump issues --issueKey=PUT ISSUE KEY`

### Create an issue
`akcli --projectKey=PUT PROJECT KEY` --create issue --summary YOUR SUMMARY --description YOUR DESCRIPTION --type TYPE OF ISSUE

If you want to use environment, use `--environment YOUR ENVIRONMENT` parameter.

### Transit an issue

**transitionId** is the code of the transition, for example:
- To Do = 11
- In Progress = 21
- Done = 31

`akcli --transition --transitionId=PUT STATUS CODE --issueKey=`

### Comment on issue
`akcli --comment --commentBody=YOUR COMMENT --issueKey=PUT ISSUE KEY`

### Get issue watchers/users

`akcli --watchers --issueKey=PUT ISSUE KEY --projectKey=PUT PROJECT KEY`

### Assign issue to user
`akcli --assign --accountId=USER ACCOUNT ID --issueKey=PUT ISSUE KEY`

### Close an issue
`akcli --close --issueKey=PUT ISSUE KEY`

### Delete an issue
`akcli --delete --issueKey=PUT ISSUE KEY`

### Limit issues

If you want to limit issues, you can use the limit parameter also
you can use offset from where to start the limit.

`akcli --dump issues --projectKey=DO --limit=26`

`akcli --dump issues --projectKey=DO --limit=26 --offset=2`

# Filter

**Get only my issues**

`akcli --filter --myIssues --projectKey=PUT PROJECT KEY`

**Get unassigned issues**

`akcli --filter --unassigned --projectKey=PUT PROJECT KEY`

If you want to get from multi projects, you can type other projects keys like the following:

`akcli --filter --myIssues --projectKey="FIRST KEY, SECOND KEY"`

**Get issues by type**

`akcli --filter --issuetype="Task, New Feature" --projectKey=PUT PROJECT KEY`


**Get issues by text**

`akcli --filter --text='TYPE ISSUE TITLE, DESCRIPTION OR ANYTHING' --projectKey=PUT PROJECT KEY`


**Get issues by status**

`akcli --filter --status='To Do, In progress' --projectKey=PUT PROJECT KEY`
