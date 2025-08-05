# 📅 6-Day Build Plan for CreatorGenie – AI Content Co-Creator

Welcome to the CreatorGenie project! This is a 6-day rapid build sprint to bring our AI-powered content co-creator to life. This document outlines **day-by-day goals, tasks, and outcomes** for each development day.

---

## 🧠 Project Summary

CreatorGenie is an AI assistant for digital content creators that:
- Accepts **natural language** prompts (Prompting)
- Uses **RAG** to retrieve trends, brand voice, previous posts
- Returns **structured content calendars, captions, thumbnails**
- Uses **Function Calling** to interact with tools like trend fetchers, schedulers, etc.

---

## 🗓️ Day-wise Development Plan

### 🟢 **Day 1 – Setup & Prompt Design**
**Goal**: Lay the foundation and define the agent’s persona

**Tasks:**
- ✅ Set up repo and environment
- ✅ Install dependencies: `FastAPI`, `LangChain`, `OpenAI`, `FAISS`, etc.
- ✅ Create `.env` and store OpenAI/Pinecone keys
- ✅ Design initial system prompt for CreatorGenie
- ✅ Implement basic chat endpoint with FastAPI
- ✅ Build CLI or Postman interface to test LLM responses

**Output:**
- `prompts.py` with a system prompt
- `api.py` basic chat route

---

### 🟡 **Day 2 – RAG Integration (Trends & Brand Voice)**
**Goal**: Connect RAG to fetch trending topics and user-specific brand data

**Tasks:**
- ✅ Set up FAISS or Pinecone vector store
- ✅ Add trend data + brand voice documents
- ✅ Create `rag_engine.py` to load and query relevant chunks
- ✅ Integrate into LLM using LangChain retrieval chain

**Output:**
- RAG-powered response with injected context
- Vector store populated and queryable

---

### 🔵 **Day 3 – Structured Output & JSON Formatting**
**Goal**: Let the agent return structured content calendars

**Tasks:**
- ✅ Define JSON schema for:
  - Instagram 7-day plan
  - Captions with hashtags
  - YouTube title + hook + thumbnail
- ✅ Create `output_formatter.py` to validate / parse JSON
- ✅ Add fallback response handling for incomplete output

**Output:**
- Clean JSON for frontend/API consumption
- Day-wise content calendar response

---

### 🟣 **Day 4 – Function Calling (Tool Integration)**
**Goal**: Enable the agent to call tools via function calling

**Tasks:**
- ✅ Implement tools in `functions.py`:
  - `get_trending_sounds()`
  - `generate_hashtags()`
  - `schedule_post()`
- ✅ Connect tools using OpenAI function calling (or LangChain tools)
- ✅ Handle tool execution responses inside agent

**Output:**
- Working function calls triggered by user queries
- Agent that auto-pulls sound trends or hashtags

---

### 🟠 **Day 5 – UI or API Frontend (Optional)**
**Goal**: Build a basic dashboard OR polish APIs for frontend team

**Tasks (choose based on time):**
- Option A: Build Next.js frontend with:
  - Chat UI
  - Display content calendar
  - Editable captions
- Option B: Finalize API docs for frontend devs

**Output:**
- Minimal creator dashboard OR
- Complete API with Swagger docs

---

### 🔴 **Day 6 – Testing, Refining, Demo Prep**
**Goal**: Polish UX and prepare for presentation

**Tasks:**
- ✅ Test full agent flow: prompt ➜ RAG ➜ JSON ➜ tools
- ✅ Add error handling + edge case handling
- ✅ Upload demo data (brand voice, trends)
- ✅ Record usage demo
- ✅ Create README + deployment instructions

**Output:**
- Final working demo
- Screenshots or screen recording
- README and deploy docs

---



