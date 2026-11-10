# Incident and Recovery Record

## Incident
The DevOps service container was intentionally stopped to simulate a controlled service failure.

## Symptoms
- The /health endpoint became unavailable.
- The service could not be reached on port 5000.

## Recovery Action
The container was started again using Docker.

## Verification
After recovery:
- The /health endpoint returned a healthy response.
- The application version was confirmed.
- The container status was checked.

## Result
The service was successfully restored after the controlled failure.
