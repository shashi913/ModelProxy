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
- [ ] Build FastAPI service with LLM integration
- [ ] Containerize with Docker
- [ ] Push image to AWS ECR
- [ ] Automate build/test/push with GitHub Actions
- [ ] Deploy to ECS Fargate
- [ ] Add CloudWatch logging + health checks

## Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License
See [LICENSE](./LICENSE).