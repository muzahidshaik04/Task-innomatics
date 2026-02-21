# 🤖 AI Career Advisor Chatbot

A production-ready AI Career Advisor chatbot built using **Google Gemini 2.5 Flash API** and **Streamlit**.

This application provides structured career guidance, skill gap analysis, roadmap generation, resume PDF analysis, and resume image evaluation.

---

## 🔥 Features

### 🎯 Career Guidance
- Role comparison (Data Analyst vs Data Scientist vs ML Engineer)
- Skill gap analysis
- Step-by-step roadmap planning
- Interview preparation
- LinkedIn summary generation

### 📄 Resume PDF Analysis
- Extracts resume content
- ATS improvement suggestions
- Resume scoring (0–100)
- Missing skill detection
- Structured improvement plan

### 🖼 Resume Image Analysis
- Formatting evaluation
- ATS compliance check
- Visual hierarchy suggestions

### 🧠 AI Capabilities
- Multi-turn conversation memory
- Structured prompt engineering
- Domain-specific responses
- Modular Gemini API wrapper
- Logging and error handling

---

## 🏗 System Architecture

```
User (Streamlit UI)
        ↓
Chat Interface + File Upload
        ↓
Backend Service Layer
 ├── Prompt Manager
 ├── Memory Manager
 ├── Resume Parser
 ├── Image Analyzer
 ├── Gemini Service
        ↓
Google Gemini 2.5 Flash API
        ↓
Structured Response Rendering
```

---

## 🛠 Tech Stack

- Python 3.10+
- Streamlit
- Google Gemini 2.5 Flash API
- pdfplumber
- Pillow
- python-dotenv
- Logging module
- AWS EC2 (deployment-ready)

---

## 📂 Project Structure

```
career_advisor_bot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── config/
│   └── settings.py
│
├── services/
│   ├── gemini_service.py
│   ├── prompt_manager.py
│   ├── memory_manager.py
│   ├── resume_parser.py
│   └── image_analyzer.py
│
├── utils/
│   └── logger.py
│
└── logs/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-career-advisor-gemini.git
cd ai-career-advisor-gemini
```

---

### 2️⃣ Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key_here
MODEL_NAME=models/gemini-2.5-flash
```

⚠️ Never commit `.env` to GitHub.

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

Open in browser:
```
http://localhost:8501
```

---

## ☁️ AWS EC2 Deployment

1. Launch EC2 instance (Ubuntu recommended)
2. Install Python & venv
3. Clone repository
4. Create `.env` file
5. Install dependencies
6. Run:

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

Open port 8501 in security group.

---

## 🧠 Prompt Engineering Strategy

- Structured system prompts
- Role-based constraints
- Domain-specific formatting
- Reusable prompt templates
- Multi-turn context preservation

---

## 🔐 Security Practices

- No hardcoded API keys
- Environment-based configuration
- Modular architecture
- Logging for debugging
- Separation of concerns

---

## 📈 Future Improvements

- JSON structured output parsing
- Resume scoring algorithm engine
- RAG-based career knowledge base
- Docker containerization
- CI/CD integration
- Public hosted demo

---

## 🎯 Ideal Use Cases

- Students planning AI careers
- Freshers preparing for Data Science roles
- Resume optimization for tech jobs
- Interview preparation
- Skill roadmap planning

---

## 👨‍💻 Author

Shaik Muzahid  
Aspiring Data Scientist | AI Enthusiast  

---

⭐ If you found this project useful, consider giving it a star!
