import streamlit as st
from langchain_core.messages import HumanMessage
from graph import app
import uuid

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SEHAJ AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (THE PASTEL THEME) ---
st.markdown("""
    <style>
    /* MAIN BACKGROUND: Soft Cream */
    .stApp {
        background-color: #FFFDF5;
    }
    
    /* SIDEBAR: Soft Lavender */
    section[data-testid="stSidebar"] {
        background-color: #F3E5F5;
        border-right: 2px solid #E1BEE7;
    }
    
    /* CHAT BUBBLES */
    /* AI (Sehaj): Soft Mint Green */
    div[data-testid="stChatMessage"] {
        background-color: #F1F8E9;
        border: 1px solid #C5E1A5;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    
    /* USER: Soft Sky Blue */
    div[data-testid="stChatMessage"].st-emotion-cache-1c7y2kd {
        background-color: #E3F2FD;
        border: 1px solid #90CAF9;
    }
    
    /* HEADERS */
    h1, h2, h3 {
        color: #5D4037; /* Warm Brown text */
        font-family: 'Helvetica', sans-serif;
    }
    
    /* BUTTONS: Soft Peach Pills */
    .stButton>button {
        background-color: #FFCCBC;
        color: #5D4037;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #FFAB91;
        transform: scale(1.05);
    }
    
    /* TOGGLES */
    .stToggle {
        color: #4A148C;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SESSION STATE SETUP ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Universal Welcome Message
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "🌿 **Hello! I am Sehaj.** \n\nI am your Holistic AI Companion. I am here to balance your Mind, Body, and Soul. \n\nHow are you feeling right now?"
    })

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user_generic_persistent_session"

# --- 4. SIDEBAR (The Control Center) ---
with st.sidebar:
    # UNIQUE LOGO AREA
    st.markdown("## 🌿 **SEHAJ AI**")
    st.caption("Stateful Holistic AI Journal")
    st.markdown("---")
    
    # USER SETTINGS
    st.subheader("⚙️ Preferences")
    # Default is now generic "Friend"
    user_name = st.text_input("What should I call you?", value="Friend")
    
    # TOGGLES
    strict_mode = st.toggle("🔥 Beast Mode (Strict Coaching)", value=False)
    
    st.markdown("---")
    
    # AGENT EXPLAINER (The "Roster")
    st.subheader("🤖 The Squad")
    
    with st.expander("🧘‍♀️ **Serena** (Therapist)", expanded=True):
        st.write("For emotions, venting, and CBT. *Warm & Gentle.*")
        
    with st.expander("🌿 **Noor** (Habit Coach)"):
        st.write("For discipline, consistency, and 'Core 4'. *Zen & Stoic.*")
        
    with st.expander("⚡ **Kai** (Fitness)"):
        st.write("For gym splits, macros, and sleep data. *Tough & Technical.*")
        
    with st.expander("🎓 **Turing** (Professor)"):
        st.write("For study plans and research papers. *Smart & Organized.*")

    with st.expander("👾 **Pixel** (Games)"):
        st.write("For boredom, trivia, and anxiety distraction. *Playful.*")
        
    st.markdown("---")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.rerun()

# --- 5. MAIN INTERFACE ---

# HEADER
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("# 🌿") # Big Icon
with col2:
    st.markdown("# Sehaj AI")
    st.markdown(f"*{user_name}'s Personal Sanctuary*")

# QUICK ACTIONS (Generic Examples)
st.markdown("### ⚡ Quick Actions")
q1, q2, q3, q4 = st.columns(4)

# Function to handle button clicks
def quick_action(text):
    st.session_state.messages.append({"role": "user", "content": text})
    # Force a rerun to process the message immediately
    st.rerun()

if q1.button("💪 Gym Plan"):
    quick_action("I want a glute focused workout plan.")
    
if q2.button("🥺 I'm Sad"):
    quick_action("I feel really heavy and overwhelmed today.")
    
if q3.button("📚 Study Help"):
    quick_action("I need research papers on Deep Learning.")
    
if q4.button("🎲 Play Game"):
    quick_action("I'm bored, let's play Atlas!")

st.markdown("---")

# --- 6. CHAT LOGIC ---

# Display History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input
user_input = st.chat_input("Type here... (e.g., 'I am procrastinating' or 'Help me sleep')")

if user_input:
    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Backend Processing
    with st.spinner("✨ Sehaj is thinking..."):
        try:
            # Config
            config = {"configurable": {"thread_id": st.session_state.thread_id}}
            
            # Input State
            prompt_content = user_input
            if strict_mode:
                prompt_content += " (Note: The user wants TOUGH LOVE/STRICT mode)."

            input_state = {
                "messages": [HumanMessage(content=prompt_content)],
                "user_name": user_name
            }
            
            # Invoke Graph
            result = app.invoke(input_state, config=config)
            
            # Get Response
            bot_response = result['messages'][-1].content
            
            # Display Response
            with st.chat_message("assistant"):
                st.markdown(bot_response)
            
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            
        except Exception as e:
            st.error(f"❌ Connection Error: {e}")