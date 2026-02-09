🚀 Career Pilot AI

### AI-Powered Career Guidance for Education, Inclusion & Empowerment

*Guiding students from confusion to clarity through intelligent career support.*

Career Pilot AI is an end-to-end AI career guidance platform designed to support **education, inclusion, and empowerment**, especially for students who lack access to structured career mentorship.

This project was built as a working prototype for social impact — combining AI guidance, structured roadmaps, and curated learning resources into one unified platform.

---

# 🌐 Live Website Link
https://monumental-squirrel-f578ad.netlify.app 
(The working of the website might take some time.)


# 💡 Core Features

## 🤖 AI Career Chatbot

* Ask career-related questions
* Get structured and practical guidance
* Personalized responses using AI

## 📄 Resume Analyzer in the Chatbot

* Upload PDF/DOCX resume
* Detect strengths & skill gaps
* Suggest improvements and career roles

## 🧠 Career Quiz in Chatbot

* Collects interests & background
* Generates career recommendations
* Suggests roadmap for improvement

## 🗺️ AI Roadmap Generator

* Enter any career (Data Analyst, Pilot, Designer, etc.)
* Select level (Beginner/Intermediate/Advanced)
* Generates structured phase-wise roadmap
* Includes checklist + progress tracker

## 📚 Smart Course Recommender

* Search by role or skill
* Courses fetched from curated database
* Shows platform + link + skills covered

---

# 🏗️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* Hosted on Netlify

### Backend

* FastAPI (Python)
* OpenAI API (AI responses)
* Pandas (course filtering)
* Resume parsing (PDF/DOCX)
* Hosted on Render/Vercel

### Database

* Custom CSV course database (multi-platform)

---

# 🧠 How It Works (Architecture)

User → Frontend UI → FastAPI Backend → API
↓
Course DB / Resume Parser
↓
AI Response → Frontend Display

---

# 🎯 Problem We Solve

Many students — especially in developing regions — face:

* Lack of career guidance
* Confusion about skills and job paths
* No personalized roadmap
* Limited access to mentors

Career Pilot AI acts as a **virtual career mentor**, available anytime.

---

# 📁 Repository Structure

```
career-pilot-ai/
│
├── frontend/
│   ├── index.html
│   ├── chatbot.html
│   ├── roadmap.html
│   ├── courses.html
│
├── main.py
├── requirements.txt
├── multi_platform_courses.csv
└── README.md
```

---

# ⚙️ Run Locally (Optional)

## 1. Clone repo

```
git clone https://github.com/your-username/career-pilot-ai.git
cd career-pilot-ai
```

## 2. Install dependencies

```
pip install -r requirements.txt
```

## 3. Add environment variable

Create `.env`

```
OPENAI_API_KEY=your_key_here
```

## 4. Run backend

```
uvicorn main:app --reload
```

## 5. Open frontend

Open index.html in browser

---

# 🌍 Social Impact

Career Pilot AI supports:

**Education** → Clear learning direction
**Inclusion** → Accessible to all students
**Empowerment** → Confidence through clarity

> “Talent is everywhere. Opportunity is not.
> Career Pilot AI helps bridge that gap.”

---

# 🔮 Future Scope

* Local language support
* Government & college integration
* Student progress dashboards
* AI skill-gap tracking
* Mobile app version

---

# 👩‍💻 Built For

Hackathons • Students • Career Guidance • Social Good

---

# ❤️ Note

This project was built with the belief that
**right guidance at the right time can change a life.**

---

# 🏁 Final Note for Reviewers

This is a fully functional deployed prototype, not just a concept.

It demonstrates how AI can be used responsibly for
**education, inclusion, and empowerment at scale.**
