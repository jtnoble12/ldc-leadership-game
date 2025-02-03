import streamlit as st

def display_intro():
    st.title("Leading Disruptive Change (LDC) Leadership Simulation")
    st.write("You are the CEO of a fast-growing tech company facing a series of adaptive challenges.")
    st.write("Your ability to navigate uncertainty, balance paradoxes, and manage discomfort will determine your success.")

def get_choice(options):
    return st.radio("Choose your response:", options)

def evaluate_choice(choice, outcomes):
    outcome = outcomes[choice]
    st.subheader("Outcome:")
    st.write(outcome["text"])
    return outcome["score"]

def run_simulation():
    display_intro()
    score = 0
    
    # Scenario 1: Paradox Mindset
    st.subheader("Scenario 1: Strategic Dilemma")
    st.write("Your company must decide between investing in R&D or focusing on immediate profitability.")
    options = {
        "Go all-in on R&D": {"text": "Your company develops groundbreaking innovations, but financial instability leads to layoffs.", "score": 5},
        "Focus on immediate profitability": {"text": "Your stock price rises in the short term, but competitors out-innovate you.", "score": 4},
        "Adopt a balanced approach": {"text": "You sustain profitability while preparing for long-term growth.", "score": 8}
    }
    choice = get_choice(list(options.keys()))
    score += evaluate_choice(choice, options)
    
    # Scenario 2: Comfort with Discomfort
    st.subheader("Scenario 2: Managing Employee Burnout")
    st.write("Employees are burning out under extreme deadlines. How do you handle this?")
    options = {
        "Push them harder": {"text": "Productivity rises temporarily but key employees leave.", "score": 4},
        "Introduce flexible work schedules": {"text": "Morale improves, but deadlines slip.", "score": 6},
        "Set clear deadlines with recovery periods": {"text": "Employees remain motivated and deadlines are mostly met.", "score": 9}
    }
    choice = get_choice(list(options.keys()))
    score += evaluate_choice(choice, options)
    
    # Scenario 3: Leading Through the Fog
    st.subheader("Scenario 3: Technological Disruption")
    st.write("A major technological disruption threatens your core business. How do you respond?")
    options = {
        "Ignore it and focus on past success": {"text": "Your company slowly declines as competitors adapt.", "score": 3},
        "Pivot immediately": {"text": "You pivot too quickly, alienating customers.", "score": 5},
        "Analyze trends and gradually adapt": {"text": "You balance risk and adaptation, securing long-term growth.", "score": 8}
    }
    choice = get_choice(list(options.keys()))
    score += evaluate_choice(choice, options)
    
    st.subheader(f"Your Final Leadership Score: {score}/27")
    if score >= 20:
        st.success("Excellent! You successfully navigated disruptive change with strategic foresight.")
    elif score >= 15:
        st.warning("Good job! You made strong decisions but could refine your approach.")
    else:
        st.error("You struggled with the challenges. Consider integrating more adaptive strategies.")

if __name__ == "__main__":
    run_simulation()
