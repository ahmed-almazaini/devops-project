# Deployment Checklist

## Prerequisites
- Docker is installed and running.
- The required Docker artifact is available.
- Port 5000 is available.
- The target release version is confirmed.

## Approval
- Deployment change is reviewed and approved.
- Source commit and release version are recorded.

## Deployment
- Stop and remove the current container if needed.
- Load or use the approved Docker image.
- Start the container on port 5000.

## Verification
- Run the `/health` endpoint.
- Confirm the expected application version.
- Check `docker ps`.
- Review application logs.

## Rollback
- Stop and remove the failed or unwanted release.
- Start the previous known working Docker image.
- Verify `/health` and the previous version.
