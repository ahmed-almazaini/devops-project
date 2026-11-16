# Evidence Index

This file lists the main evidence used to verify the DevOps project implementation.

## Repository
https://github.com/ahmed-almazaini/devops-project

## Pull Requests
- PR #1 - Deployment checklist - Ahmad
- PR #2 - Service verification script - Amjad
- PR #3 - Linux operations runbook - Anas
- PR #4 - Support information test - Anas
- PR #5 - Incident recovery record - Ahmad
- PR #6 - CI non-root Docker check - Amjad
- PR #7 - Final project README - Anas

## CI and Testing
- Automated unit tests executed with Python unittest.
- Ruff static analysis passed.
- Controlled CI failure was demonstrated and corrected.
- Final CI runs completed successfully.

## Versioned Releases
- v1.0.0
- v1.1.0

## CI Artifact
- Source commit: d2cfe05f872d25752bcb9213aebeca871d2241d2
- CI run: 41164195569
- Artifact: devops-service-d2cfe05f872d25752bcb9213aebeca871d2241d2
- Deployed container: ci-artifact-v110
- Host port: 5002

## Deployment Verification
- /health returned healthy.
- /contact returned expected service information.
- docker ps confirmed the container was running.

## Security Evidence
- Named Linux accounts for team members.
- Shared devops-team group.
- Application runs as non-root appuser.
- UFW default incoming policy is deny.
- Required service port was explicitly allowed.

## Recovery and Rollback
- Controlled service failure and recovery were demonstrated.
- Rollback from v1.1.0 to v1.0.0 was verified.

## Change Records
- CR-001 - Initial v1.0.0 deployment - Approved by Anas Marshud Alsuhaymi.
- CR-002 - Exact CI artifact v1.1.0 deployment - Approved by Amjad Yasser Bahakeem.

## Individual Contribution Evidence

### Anas
- Linux administration evidence.
- Linux operations runbook.
- Support information automated test.
- Final project README.
- Peer reviews and CR-001 approval.

### Ahmad
- Base environment and application setup.
- Docker, CI, releases, deployment, recovery, and rollback.
- Deployment checklist.
- Incident recovery record.
- Peer reviews.

### Amjad
- Linux administration evidence.
- Service verification script.
- CI non-root Docker security check.
- Evidence index.
- Peer reviews and CR-002 approval.
