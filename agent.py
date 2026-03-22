import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# HYBRID CareerPilot AI - Supports Gemini API Key OR Mocked Fallback
# If GOOGLE_API_KEY is found in Render/Environment, it uses real AI.
# If no key is found, it uses the high-quality pre-written career scripts.

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# --- MOCKED FALLBACK LOGIC ---
def get_mock_response(tool_name: str, query: str) -> str:
    mock_data = {
        "skills": f"Essential Skills for {query}:\n1. Technical Proficiency\n2. Cloud Fundamentals\n3. Problem Solving\n4. Communication",
        "projects": f"Projects for {query}:\n1. Industry Case Study\n2. Open Source Patch\n3. Personal Portfolio App",
        "resume": "Resume Tip: Focus on quantifiable achievements and use active keywords.",
        "roadmap": f"Roadmap for {query}:\nPhase 1: Foundations\nPhase 2: Building Projects\nPhase 3: Certification\nPhase 4: Hiring"
    }
    return mock_data.get(tool_name, "I recommend reaching out to a mentor for specialized advice.")

# --- AI TOOL WRAPPERS ---
def suggest_skills(career_goal: str) -> str:
    if GOOGLE_API_KEY:
        try:
            import google.generativeai as genai
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Suggest top technical skills for: {career_goal}")
            return response.text
        except Exception as e:
            return get_mock_response("skills", career_goal)
    return get_mock_response("skills", career_goal)

def suggest_projects(career_goal: str) -> str:
    if GOOGLE_API_KEY:
        try:
            import google.generativeai as genai
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Suggest 3 portfolio projects for: {career_goal}")
            return response.text
        except Exception:
            return get_mock_response("projects", career_goal)
    return get_mock_response("projects", career_goal)

def resume_feedback(resume_text: str) -> str:
    if GOOGLE_API_KEY:
        try:
            import google.generativeai as genai
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Review this resume summary: {resume_text}")
            return response.text
        except Exception:
            return get_mock_response("resume", resume_text)
    return get_mock_response("resume", resume_text)

# --- Define Sub-Agents ---
resume_agent = Agent(name="resume_agent", instruction="Analyze resumes.", tools=[resume_feedback])
skill_agent = Agent(name="skill_agent", instruction="Suggest skills.", tools=[suggest_skills])
project_agent = Agent(name="project_agent", instruction="Suggest projects.", tools=[suggest_projects])

# --- Main Orchestrator ---
careerpilot_orchestrator = Agent(
    name="careerpilot_orchestrator",
    sub_agents=[resume_agent, skill_agent, project_agent],
    instruction="""
You are CareerPilot AI. Help users with career advice.
If you have an API key, use it to provide deep insights.
If not, provide structured advice from your built-in knowledge.
    """
)
