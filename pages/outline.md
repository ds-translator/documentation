# Functional Requirements

**Users:** Input speech in one language and receive translated speech in another.
Access the service via a web interface.

**Developers:** Easy integration with CI/CD pipelines.
Clear API documentation for backend services.

**Customer:** Real-time notifications for downtime or failures.
Scalable infrastructure to handle user growth.

# Non-Functional Requirements

- Performance: Response time < 2 seconds under normal load.

- Scalability: Support up to 10,000 concurrent users.

- Security: TLS encryption, private subnets, and role-based access control.

- Availability: 99.9% uptime for the production environment.

- Compliance: GDPR-compliant data handling.

# System Architecture

![Diagram](/images/diagram.png)

## Components

**Frontend:** JS-based web interface for user interaction (Docker container)

**Backend:** FastAPI-Server with Python as logical controller (Docker container)

**Speech-To-Text:** Whisper (Docker container)

**Translation** Libretranslate (Docker container)

**Text-To-Speech** Tortoise-TTS (Docker container)

**CI/CD Pipeline:** GitHub Actions for automated testing and deployment.

**Monitoring:** AWS CloudWatch and Grafana for metrics, logs, and alerts.




Interactions

    Users interact with the frontend, which sends requests to the backend.

    The backend processes speech, interacts with the translation engine, and stores data in the database.

    CI/CD pipelines automate testing and deployment to staging and production environments.

    Monitoring tools track performance and alert the team to issues.