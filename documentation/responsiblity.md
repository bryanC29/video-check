# Project Responsibility Chart

### Abhishek – Frontend (Next.js)

- [ ] Video Upload UI
- [ ] Result Page UI (Video match + metadata)
- [ ] Video Preview Component
- [ ] API Integration (Upload + Search)
- [ ] Progress/Error States + Notifications

---

### Aslaan – AI Model (main), Utilities & Scripts

#### AI Model Service

- [ ] Pretrained Model Setup (tampering/deepfake detection)
- [ ] Video Preprocessing Logic
- [ ] Confidence Score Logic

#### Utility & Automation Scripts

- [ ] Database Seeder Script
- [ ] Local Setup Scripts
- [ ] Testing Scripts (unit/e2e)
- [ ] Shared gRPC & REST Types
- [ ] Constants & Helper Utilities

---

### Mazhar – Video Processing & Metadata Service

#### Video Processing Service (Python)

- [ ] gRPC Server Setup
- [ ] Frame Extraction (OpenCV)
- [ ] Perceptual Hashing (pHash, dHash, etc.)
- [ ] Return hash vector to API Gateway

#### Metadata Service (NestJS + MongoDB)

- [ ] MongoDB Schema & Indexing
- [ ] Insert Handler (store hashes + metadata)
- [ ] Search Handler (match hashes)
- [ ] Optimize Hash Matching Logic

---

### Bryan – API Gateway, AI Model (partial), DevOps & Infra

#### API Gateway (NestJS)

- [ ] REST API Setup
- [ ] gRPC Client Integration (to Processing, Metadata, AI)
- [ ] Upload Handler (receive and forward)
- [ ] Search Handler (match and return metadata)

#### DevOps & Infrastructure

- [ ] Dockerization of All Services
- [ ] Docker Compose Setup
- [ ] Kubernetes Orchestration
- [ ] Cloud Deployment (Render / AWS / DO / GCP)

#### AI Model (Support)

- [ ] gRPC Interface for AI Model Service
- [ ] Help integrate into processing pipeline

---

### Documentation

- [ ] `README.md`
- [ ] REST API Documentation
- [ ] gRPC Service Documentation
- [ ] System Architecture Diagram
- [ ] Final Demo & Presentation
