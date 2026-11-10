# Linux Operations Runbook

## Check Current User
Command:
whoami

Purpose:
Confirms which Linux account is currently active.

## Check User Groups
Command:
groups

Purpose:
Confirms that the user belongs to the devops-team group.

## Check Project Permissions
Command:
ls -ld /opt/devops-project

Purpose:
Verifies the project directory ownership and permissions.

## Check Running Processes
Command:
ps aux | grep python

Purpose:
Checks for Python-related processes.

## Check Docker Service
Command:
systemctl is-active docker

Purpose:
Confirms that the Docker service is running.
