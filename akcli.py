#!/usr/bin/env python3


import requests
import argparse
from jira import JIRA
from config.settings import *
from collections import namedtuple


class JiraCli:
  def __init__(self, args):
    self.args = args
  
  def create(self):
    '''
      Create new issue by providing dictionary of data

      Here I faced a problem, by using REST API service
      creating a new issue continuously returning 400 error from the server says
      transition and assigner missing, by that I decided to use jira library for the whole project
      but in the upcoming versions I'll resolve the problem.
    '''
    issue_dict = {
      'project': {'key': self.args.projectId},
      'summary': self.args.issueSummary or '',
      'description': self.args.issueDescription,
      'issuetype': {'name': self.args.issueType},
    }
    new_issue = self.auth().create_issue(fields=issue_dict)
    return new_issue

  def dump(self):
    '''
      Dump data of the given parameter
      issues or projects
    '''
    if self.args.dump == 'projects':
      projects = self.auth().projects()
      print(projects)
    else:
      issues = self.auth().issue(self.args.issueKey)
      print(issues)

  def transition(self):
    '''
      Implement transition on issue
      To Do = 11
      In Progress = 21
      In Review = 31
      Done = 41
    '''
    if self.args.transitionId:
      issue = self.auth().issue(self.args.issueKey)
      transitions = self.auth().transitions(issue)
      self.auth().transition_issue(self.args.issueKey, self.args.transitionId)

  def delete(self):
    '''
      Delete an issue by the given issueKey
    '''
    if self.args.issueKey:
      issue = self.auth().issue(self.args.issueKey)
      issue.delete()

  def close(self):
    '''
      Close an issue by sitting it status to Done
    '''
    if self.args.issueKey:
      issue = self.auth().issue(self.args.issueKey)
      transitions = self.auth().transitions(issue)
      self.auth().transition_issue(self.args.issueKey, '41')

  def comment(self):
    '''
      Comment on issue
    '''
    if self.args.issueKey:
      self.auth().add_comment(self.args.issueKey, self.args.commentBody)

  def auth(self):
    '''
      Basic authorization for JIRA
    '''
    auth_jira = JIRA('https://jira-tt-123.atlassian.net', basic_auth=(AUTH_USER, AUTH_TOKEN))
    return auth_jira

  def getter(self, args):
    '''
      Future function to convert dictionary keys into properties
    '''
    return namedtuple('Dict', ' '.join(list(args.keys())))(**args)

def main_func(args):
  """
  Initialize main class
  """
  akcli = JiraCli(args)

  if args.create:
    akcli.create()

  if args.dump:
    akcli.dump()

  if args.delete:
    akcli.delete()

  if args.close:
    akcli.close()

  if args.comment:
    akcli.comment()

  if args.transition:
    akcli.transition()


if __name__ == '__main__':
  # create the top-level parser
  parser = argparse.ArgumentParser(prog='JIRA Command Line Interface')
  parser.add_argument('--issueKey', dest="issueKey", help='issue key or id')
  parser.add_argument('--projectKey', dest="projectKey", help='issue key or id')


  # Create issue
  parser.add_argument('--create', action='store_true', help='create an issue')
  create_sub_parse = parser.add_subparsers(help='sub commands for creating issue')
  sub_create = create_sub_parse.add_parser('issue', help='create issue is sub-command with sub-commands')
  sub_create.add_argument('--issueType', required=True, type=str, help='issue type')
  sub_create.add_argument('--issueDescription', required=True, type=str, help='issue description')
  sub_create.add_argument('--issueSummary', required=True, type=str, help='issue summary')
  sub_create.add_argument('--projectId', required=True, type=str, help='project key')

  # Dump issue
  parser.add_argument('--dump',
    default=None,
    nargs='?',
    choices=['issues', 'projects'],
    help='dump projects, issues, (default: %(default)s)'
  )

  # Delete issue
  parser.add_argument('--delete', action='store_true', help='delete an issue')

  # Close an issue
  parser.add_argument('--close', action='store_true', help='delete an issue')

  # Do transition
  parser.add_argument('--transition', action='store_true', help='transit an issue')
  parser.add_argument(
  	'--transitionId',
  	type=int,
  	dest="transitionId",
    choices=[11, 21, 31, 41],
    help='transit an issue'
  )

  # Comment on issue
  parser.add_argument('--comment', action='store_true', help='comment on issue')
  parser.add_argument('--commentBody', dest="commentBody", help='comment body')

  args = parser.parse_args()

  main_func(args)
