from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import json
import pandas as pd
import pdfplumber
import docx2txt
from typing import List
from openai import OpenAI

# ======================================================
# INIT
# ======================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment")

client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI(title="Career Pilot – Unified AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Hackathon safe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ======================================================
# MODELS
# ======================================================

class RoadmapRequest(BaseModel):
    career: str
    level: str

class QueryRequest(BaseModel):
    query: str

class ChatBody(BaseModel):
    message: str

# ======================================================
# COURSES ENGINE
# ======================================================

csv_path = os.path.join(BASE_DIR, "multi_platform_courses.csv")
df_courses = pd.read_csv(csv_path).fillna("")

df_courses["Roles"] = df_courses["Roles"].str.lower()
df_courses["Skills"] = df_courses["Skills"].str.lower()
df_courses["Title of Course"] = df_courses["Title of Course"].str.strip()

def filter_courses(query: str) -> List[dict]:
    query = query.lower().strip()

    filtered_df = df_courses[
        df_courses["Roles"].str.contains(query, na=False)
        | df_courses["Skills"].str.contains(query, na=False)
    ].head(6)

    return [
        {
            "course_title": row["Title of Course"],
            "role": row["Roles"].title(),
            "skills": row["Skills"].title(),
            "platform": row["Platform"],
            "url": row["URL"]
        }
        for _, row in filtered_df.iterrows()
    ]

@app.post("/get-courses")
def get_courses(data: QueryRequest):
    results = filter_courses(data.query)
    return {
        "query": data.query,
        "total_results": len(results),
        "results": results
    }

# ======================================================
# PERSONALIZED ROADMAP (NO HOURS)
# ======================================================

@app.post("/generate-roadmap")
async def generate_roadmap(req: RoadmapRequest):
    try:
        prompt = f"""
You are a senior career mentor and curriculum designer.

Create a realistic, job-ready learning roadmap.

Career: {req.career}
Skill Level: {req.level}

Rules:
- 3 to 5 phases
- 4 to 6 tasks per phase
- Practical, industry-relevant tasks
- Clear progression from fundamentals to job readiness
- No fluff

Return ONLY valid JSON in this format:

{{
  "career": "{req.career}",
  "total_duration": "X months",
  "phases": [
    {{
      "name": "",
      "duration": "",
      "tasks": []
    }}
  ]
}}

No markdown.
No explanation.
Only JSON.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return json.loads(response.choices[0].message.content)

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON returned by AI")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ======================================================
# AI HELPERS
# ======================================================

def extract_text(file):
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "\n".join([page.extract_text() or "" for page in pdf.pages])
    elif file.filename.endswith(".docx"):
        return docx2txt.process(file.file)
    return ""

def ask_ai(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content

# ======================================================
# RESUME ANALYZER
# ======================================================

@app.post("/api/resume/upload")
async def upload_resume(file: UploadFile = File(...)):
    text = extract_text(file)

    prompt = f"""
You are an expert career counselor and technical recruiter.

Analyze the resume and provide:
1. Top 3 career matches
2. Strengths
3. Skill gaps
4. 3-month learning roadmap
5. Resume improvement tips

Resume:
{text}
"""

    return {"result": ask_ai(prompt)}

# ======================================================
# QUIZ ANALYZER (FOR DEMO)
# ======================================================

@app.post("/api/quiz/submit")
async def submit_quiz(quiz: dict):
    prompt = f"""
Analyze the user profile and provide:
1. Ranked career matches
2. Missing skills
3. 6-month learning roadmap

User data:
{quiz}
"""
    return {"result": ask_ai(prompt)}

# ======================================================
# CHATBOT
# ======================================================

@app.post("/api/chat")
async def chat(body: ChatBody):
    prompt = f"""
You are Career Pilot AI, a professional career mentor.

Respond clearly, practically, and honestly.
Focus on career clarity, skills, and next steps.

User:
{body.message}
"""
    return {"reply": ask_ai(prompt)}

# ======================================================
# HEALTH CHECK
# ======================================================

@app.get("/")
def home():
    return {"status": "Career Pilot Backend Running Successfully"}