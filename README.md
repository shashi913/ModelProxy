# LLM API Wrapper with CI/CD on AWS

A containerized LLM-powered API, deployed to AWS ECS Fargate via an automated
GitHub Actions CI/CD pipeline. Built as a learning project covering Docker,
CI/CD, and cloud deployment fundamentals.

## Status
🚧 In development — see [Roadmap](#roadmap) below.

## Tech stack
- **App:** Python (FastAPI)
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud:** AWS (ECR, ECS Fargate, CloudWatch)

## Local development

```bash
git clone https://github.com/shashi913/llm-api-devops.git
cd llm-api-devops
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Roadmap
- [x] Build FastAPI service with LLM integration
- [x] Containerize with Docker
- [x] Push image to AWS ECR
- [x] Automate build/test/push with GitHub Actions
- [x] Deploy to ECS Fargate
- [x] Add CloudWatch logging + health checks

## Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License
See [LICENSE](./LICENSE).

## Author
Maintained by [@shashi913](https://github.com/shashi913)

## Deployment

This app is deployed to AWS ECS Fargate, pulling its image from a private ECR repository.

### Architecture
- **ECR** — stores the built Docker image
- **ECS Fargate** — runs the container, no server management required
- **Secrets Manager** — stores the Groq API key, injected into the container at runtime
- **CloudWatch Logs** — captures container output for monitoring

### Deploying
1. Build and push the image: see `Dockerfile`
2. Task definition: `deploy/task-definition.json`
3. Scale the service up/down:
```bash
   aws ecs update-service --cluster modelproxy-cluster --service modelproxy-service --desired-count 1 --region us-east-1
```

**Note:** the service is scaled to 0 by default to avoid ongoing costs. Scale up before demoing.