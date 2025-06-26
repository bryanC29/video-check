# 1-Month Project Timeline

> Duration: 4 Weeks  
> Goal: Build a video recognition system MVP with working microservices, gRPC communication, and frontend.

---

## Week 1 – Setup & Foundations

- [ ] Set up monorepo/repo structure
- [ ] Docker setup for all services
- [ ] Define gRPC `.proto` files
- [ ] Scaffold API Gateway (NestJS)
- [ ] Scaffold Video Processor (Python gRPC)
- [ ] Set up MongoDB (local or cloud)
- [ ] Frontend project (Next.js) basic layout
- [ ] Plan UI (upload, result views)

---

## Week 2 – Upload to Processing Integration

- [ ] Implement video upload flow (Frontend → Gateway)
- [ ] Forward video to Video Processor via gRPC
- [ ] Extract keyframes from video
- [ ] Generate hashes for each frame
- [ ] Send hashes to Metadata Service
- [ ] Store hashes + dummy metadata in MongoDB
- [ ] Add test dataset + DB seeding script

---

## Week 3 – Video Matching & AI Detection

- [ ] Implement search flow (upload → match → metadata)
- [ ] Match video hashes in DB and return metadata
- [ ] Frontend: Show matched video and author info
- [ ] Integrate AI model (tampering detection)
- [ ] Return confidence score with match results

---

## Week 4 – Final Integration & Polish

- [ ] Add error handling, edge cases, logs
- [ ] End-to-end testing: Upload → Process → Match
- [ ] Optimize metadata queries (tolerance, indexing)
- [ ] UI polish (loading states, fallback messages)
- [ ] Finalize deployment setup (Docker Compose / Cloud)
- [ ] Complete all documentation
- [ ] Prepare demo, report, and final checklist

---

## Final Deliverables

- [ ] Working MVP (upload → match → metadata)
- [ ] Clean UI (Next.js)
- [ ] Microservices with gRPC communication
- [ ] MongoDB with metadata + hash index
- [ ] Documentation
- [ ] Presentation
