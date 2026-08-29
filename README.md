# Self-Healing Deployment

A simple DevOps project that automatically builds, deploys, monitors, and recovers a Dockerized FastAPI application on AWS EC2.

## Architecture

```text
Developer
    |
    | git push
    v
GitHub
    |
    v
GitHub Actions
    |
    +---- Run tests
    |
    +---- Build Docker image
    |
    +---- Push image to GHCR
    |
    v
AWS EC2
    |
    +---- Docker container
    |       |
    |       v
    |    FastAPI :8000
    |       |
    |       v
    |    /health
    |
    +---- Health Monitor
            |
            v
       Health check
            |
       +----+----+
       |         |
    Healthy   Unhealthy
       |         |
    Continue     v
             recover.sh
                 |
                 v
            Start container
                 |
                 v
              /health
                 |
                 v
             Healthy
```

## What the project does

The project demonstrates an automated CI/CD and self-healing workflow:

1. Code is pushed to the `main` branch.
2. GitHub Actions runs the application tests.
3. A Docker image is built.
4. The image is pushed to GitHub Container Registry (GHCR).
5. GitHub Actions connects to the AWS EC2 server.
6. The latest container is deployed automatically.
7. A health monitor checks `/health` periodically.
8. If the application becomes unavailable, the monitor runs the recovery script.
9. The container is started again and the health endpoint is checked.

## Technologies

* Python
* FastAPI
* Docker
* GitHub Actions
* GitHub Container Registry (GHCR)
* AWS EC2
* Linux
* Bash
* Python health monitoring

## Project Structure

```text
self-healing-deployment/
|
├── .github/
│   └── workflows/
│       └── ci.yml
|
├── app/
|
├── monitor/
│   ├── health_monitor.py
│   └── recover.sh
|
├── tests/
|
├── Dockerfile
├── requirements.txt
└── README.md
```

## CI/CD Flow

```text
git push
    |
    v
Run tests
    |
    v
Build Docker image
    |
    v
Push image to GHCR
    |
    v
Deploy to EC2
```

Deployment is blocked if the CI job fails.

## Self-Healing Flow

```text
Application running
       |
       v
GET /health
       |
       +---- 200 ------> HEALTHY
       |
       +---- Failure --> UNHEALTHY
                           |
                           v
                     recover.sh
                           |
                           v
                    Start container
                           |
                           v
                     GET /health
                           |
                           v
                        HEALTHY
```

## Failure Scenario Tested

The application was deliberately stopped to simulate a failure.

The monitor detected the failure:

```text
UNHEALTHY
```

The recovery script automatically started the application:

```text
RECOVERY SUCCESSFUL
```

The application then returned:

```json
{
  "status": "healthy",
  "version": "2.0.0"
}
```

## Key DevOps Concepts Demonstrated

* Continuous Integration
* Continuous Deployment
* Docker containerization
* Container registry usage
* AWS EC2 deployment
* SSH-based deployment automation
* Application health checks
* Failure detection
* Automated remediation
* Basic self-healing

## Future Improvements

Possible next improvements include:

* Versioned Docker image tags instead of relying only on `latest`
* Automatic rollback to the previous healthy version
* Monitoring and alerting with CloudWatch
* Running the health monitor as a managed service
* Infrastructure as Code using Terraform
* Better secret and credential management
* Deployment strategies such as blue-green or canary deployment
* Centralized logging
