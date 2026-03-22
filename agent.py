import os
from dotenv import load_dotenv
from google.adk.agents import Agent

# MOCKED CareerPilot AI - No API Keys Required
# This version behaves like an AI but uses high-quality predefined logic
# Perfect for demonstrations and submissions when Vertex AI is unavailable.

def suggest_skills(career_goal: str) -> str:
    """Mocked skill suggestion logic."""
    skills = {
        "cloud architect": "1. Google Cloud Professional Architect Certification\n2. Terraform & Infrastructure as Code\n3. Kubernetes & GKE\n4. Network Security & Identity IAM",
        "data scientist": "1. Python (Pandas, Scikit-learn)\n2. SQL & BigQuery\n3. Machine Learning Frameworks (TensorFlow/PyTorch)\n4. Data Visualization (Looker/Tableau)",
        "full stack developer": "1. React/Next.js for Frontend\n2. Node.js or Python for Backend\n3. Database Management (SQL/NoSQL)\n4. CI/CD & Cloud Deployment"
    }
    goal = career_goal.lower()
    for key in skills:
        if key in goal:
            return f"Top Skills for your goal:\n{skills[key]}"
    return f"To excel as a {career_goal}, focus on: 1. Core Technical Fundamentals 2. Domain Specialty 3. Cloud Infrastructure 4. Soft Skills (Communication & Leadership)."

def suggest_projects(career_goal: str) -> str:
    """Mocked project suggestion logic."""
    return f"Recommended Portfolio Projects for {career_goal}:\n1. End-to-End {career_goal} Dashboard\n2. Automated Cloud Migration Script\n3. AI-Powered Analysis Tool\n4. Open Source Contribution in your niche."

def resume_feedback(resume_text: str) -> str:
    """Mocked resume analyzer."""
    return "Resume Feedback:\n- Use more action verbs (e.g., 'Spearheaded', 'Optimized').\n- Quantify results (e.g., 'Improved performance by 30%').\n- Ensure technical keywords match your target role.\n- Keep it to 1-2 pages maximum."

def career_path_guide(current_role: str, target_role: str) -> str:
    """Mocked career path guide."""
    return f"Roadmap from {current_role} to {target_role}:\n- Phase 1 (0-3 mo): Foundation & Certification\n- Phase 2 (3-6 mo): Build 3 Major Projects\n- Phase 3 (6-9 mo): Networking & Application\n- Phase 4 (9-12 mo): Interview Prep & Landing the Job!"

# Define Sub-Agents (Mocked)
resume_agent = Agent(name="resume_agent", instruction="Analyze resumes.", tools=[resume_feedback])
skill_agent = Agent(name="skill_agent", instruction="Suggest skills.", tools=[suggest_skills])
project_agent = Agent(name="project_agent", instruction="Suggest projects.", tools=[suggest_projects, career_path_guide])

# Main Orchestrator
careerpilot_orchestrator = Agent(
    name="careerpilot_orchestrator",
    sub_agents=[resume_agent, skill_agent, project_agent],
    instruction="""
You are CareerPilot AI. You help users navigate their career.
When a user asks for a career plan or skills, use your tools to provide a professional response.
Always format your answer clearly with headers:
1. 🛤️ Career Roadmap
2. 💡 Essential Skills
3. 🏗️ Recommended Projects
4. 📄 Resume Tips
    """
)
