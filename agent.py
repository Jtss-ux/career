import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# ADVANCED HYBRID CareerPilot AI - Smart Model Routing
# Pro: High Complexity (Career Paths)
# Flash: Standard Tasks (Skills, Projects)
# Mocked: Last-resort fallback

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

class SmartGemini:
    """Intelligently routes requests to Pro, Flash, or Mocked fallback."""
    
    @staticmethod
    def query(prompt: str, preferred_model: str = "gemini-1.5-flash") -> str:
        if not GOOGLE_API_KEY:
            return "fallback" # Trigger mocked logic
        
        import google.generativeai as genai
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # Try preferred model first, then the other, then fail to mocked
        models_to_try = [preferred_model, "gemini-1.5-flash" if preferred_model == "gemini-1.5-pro" else "gemini-1.5-pro"]
        
        for model_name in models_to_try:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                print(f"Model {model_name} failed: {e}")
                continue
        
        return "fallback"

# --- TOOLS WITH SMART ROUTING ---

def suggest_skills(career_goal: str) -> str:
    prompt = f"Provide a detailed list of essential technical and soft skills for a {career_goal}."
    res = SmartGemini.query(prompt, preferred_model="gemini-1.5-flash")
    if res == "fallback":
        return f"Key Skills for {career_goal}:\n1. Technical Mastery\n2. Tool Proficiency\n3. Agile Mindset\n4. Team Collaboration"
    return res

def suggest_projects(career_goal: str) -> str:
    prompt = f"Suggest 3 high-impact portfolio projects for a {career_goal} to land a top job."
    res = SmartGemini.query(prompt, preferred_model="gemini-1.5-flash")
    if res == "fallback":
        return f"Projects for {career_goal}:\n1. End-to-end automation tool\n2. Professional Portfolio\n3. Open Source contribution"
    return res

def resume_feedback(resume_text: str) -> str:
    prompt = f"Analyze this resume text and provide 3 critical improvements: {resume_text}"
    res = SmartGemini.query(prompt, preferred_model="gemini-1.5-flash")
    if res == "fallback":
        return "Resume Tip: Use the X-Y-Z formula (Accomplished X, as measured by Y, by doing Z)."
    return res

def career_path_guide(current_role: str, target_role: str) -> str:
    # Uses PRO for deep reasoning on career transitions
    prompt = f"Create a comprehensive 4-phase transition roadmap from {current_role} to {target_role}. Be very detailed."
    res = SmartGemini.query(prompt, preferred_model="gemini-1.5-pro")
    if res == "fallback":
        return f"Roadmap for {target_role}:\nPhase 1: Skill Audit\nPhase 2: Project Building\nPhase 3: Certification\nPhase 4: Targeted Networking"
    return res

# --- AGENT ARCHITECTURE ---
resume_agent = Agent(name="resume_agent", tools=[resume_feedback])
skill_agent = Agent(name="skill_agent", tools=[suggest_skills])
project_agent = Agent(name="project_agent", tools=[suggest_projects, career_path_guide])

careerpilot_orchestrator = Agent(
    name="careerpilot_orchestrator",
    sub_agents=[resume_agent, skill_agent, project_agent],
    instruction="""You are CareerPilot AI.
Use Gemini 1.5 Pro for complex roadmaps and Gemini 1.5 Flash for skills/projects.
If APIs are down, provide structured advice from your built-in career benchmarks.
Always be encouraging and professional."""
)
