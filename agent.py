import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# PREMIUM HYBRID CareerPilot AI - Top-Tier Edition
# Persona: Senior Career Strategist & Tech Architect
# Features: Smart Routing, Self-Healing, and Rich Visual Formatting

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

class SmartGemini:
    """Intelligently routes requests to Pro, Flash, or Premium Mocked fallback."""
    
    @staticmethod
    def query(prompt: str, preferred_model: str = "gemini-1.5-flash") -> str:
        # Add formatting instruction to every prompt to ensure 'Top-Tier' look
        formatting_instruction = "\n\nCRITICAL: Format your response beautifully using Markdown. Use bolding for emphasis, bullet points for lists, and emojis where appropriate to make it look premium and professional."
        full_prompt = prompt + formatting_instruction

        if not GOOGLE_API_KEY:
            return "fallback"
        
        import google.generativeai as genai
        genai.configure(api_key=GOOGLE_API_KEY)
        
        models_to_try = [preferred_model, "gemini-1.5-flash" if preferred_model == "gemini-1.5-pro" else "gemini-1.5-pro"]
        
        for model_name in models_to_try:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(full_prompt)
                return response.text
            except Exception:
                continue
        
        return "fallback"

# --- PREMIUM TOOLS WITH SMART ROUTING ---

def suggest_skills(career_goal: str) -> str:
    prompt = f"Act as a Senior Tech Architect. Provide a high-level skill matrix for an aspiring {career_goal}. Group skills by 'Hard Skills', 'Soft Skills', and 'Future-Proof Skills'."
    res = SmartGemini.query(prompt, preferred_model="gemini-1.5-flash")
    if res == "fallback":
        return f"""
### 💡 Essential Skill Matrix for **{career_goal}**

| Category | Skills |
| :--- | :--- |
| **Hard Skills** | Tech Stack Proficiency, System Architecture, Code Optimization |
| **Soft Skills** | Strategic Thinking, Stakeholder Management, Mentorship |
| **Future-Proof** | AI Integration, Sustainability in Tech, Cloud Resilience |

> *\"Skills are the architecture of your career success.\"*
"""
    return res

def suggest_projects(career_goal: str) -> str:
    prompt = f"Design 3 'Portfolio Killers' (high-impact projects) for a {career_goal}. These should be projects that impress FAANG-level recruiters."
    res = SmartGemini.query(prompt, preferred_model="gemini-1.5-flash")
    if res == "fallback":
        return f"""
### 🏗️ **Top-Tier Portfolio Projects** for {career_goal}

1.  **The Architect's Sandbox**: Build an auto-scaling cloud infrastructure for a high-traffic app.
2.  **AI-Driven Career Bot**: Create a RAG-based agent that analyzes industry trends.
3.  **Enterprise Security Audit**: Implement a Zero-Trust security layer for an open-source project.
"""
    return res

def resume_feedback(resume_text: str) -> str:
    prompt = f"Perform a high-level executive review of this resume summary. Focus on 'Impact' and 'Metrics': {resume_text}"
    res = SmartGemini.query(prompt, preferred_model="gemini-1.5-flash")
    if res == "fallback":
        return """
### 📄 **Executive Resume Feedback**

- **Quantify Impact**: Instead of "built apps," use "Built 5+ high-availability apps reducing latency by 40%."
- **Action Verbs**: Use 'Architected', 'Spearheaded', and 'Orchestrated'.
- **Keyword Optimization**: Ensure alignment with ATS (Applicant Tracking Systems).
"""
    return res

def career_path_guide(current_role: str, target_role: str) -> str:
    prompt = f"Design a 12-month Executive Roadmap to transition from {current_role} to {target_role}. Include quarterly milestones and key 'Win' metrics."
    res = SmartGemini.query(prompt, preferred_model="gemini-1.5-pro")
    if res == "fallback":
        return f"""
### 🚀 **12-Month Executive Roadmap**: {current_role} → {target_role}

*   **Q1: Foundations**: Skill Gap Analysis & Certification.
*   **Q2: Building**: Construction of Top-Tier Portfolio.
*   **Q3: Visibility**: Industry Networking & Public Contributions.
*   **Q4: Mastery**: Interview Preparation & Negotiation.

**Key Metric**: Weekly networking calls + 1 published tech article.
"""
    return res

# --- AGENT ARCHITECTURE ---
resume_agent = Agent(name="resume_agent", tools=[resume_feedback])
skill_agent = Agent(name="skill_agent", tools=[suggest_skills])
project_agent = Agent(name="project_agent", tools=[suggest_projects, career_path_guide])

careerpilot_orchestrator = Agent(
    name="careerpilot_orchestrator",
    sub_agents=[resume_agent, skill_agent, project_agent],
    instruction="""
You are **CareerPilot AI**, a Senior Career Strategist & Tech Architect.
Your mission is to provide world-class, insightful, and visually stunning career advice.

**Response Guidelines**:
1. Use **Rich Markdown** (Bold, Italics, Lists, Tables).
2. Be **Professional**, **Actionable**, and **Inspiring**.
3. Use **Emojis** to add visual flair (🚀, 🏗️, 💡).
4. For complex roadmaps, act like a high-end consultant.
"""
)
