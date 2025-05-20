# MCP Server

Model Context Protocol (MCP) server for AI model management and inference.

## Features

- FastAPI backend
- Multiple AI model support (GPT-4, Deepseek)
- Docker containerization
- Environment configuration
- LoRA fine-tuning capabilities

## Setup

### Local Development

1. Clone the repository
2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create `.env` file from `.env.example` and configure API keys
5. Run the server:
```bash
uvicorn app.main:app --reload
```

### Docker Deployment

1. Build and run:
```bash
docker-compose up --build
```
2. Access the API at `http://localhost:8000`

### Cloud Deployment

#### AWS ECS
1. Configure AWS CLI
2. Build and push Docker image to ECR
3. Create ECS task definition
4. Deploy service

#### Google Cloud Run
1. Install gcloud CLI
2. Build and push container:
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/mcp-server
```
3. Deploy:
```bash
gcloud run deploy --image gcr.io/PROJECT-ID/mcp-server
```

## API Documentation

Access Swagger UI at `http://localhost:8000/docs`

## Environment Variables

See `.env.example` for configuration options

## License

MIT