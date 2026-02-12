import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from graph import app  # Importing your existing LangGraph
import uuid

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Noor 🤍 | Agentic AI Companion",
    page_icon="🌿",
    layout="centered"
)

# --- CUSTOM CSS FOR "ZEN" VIBE ---
st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
    }
    .stTextInput input {
        border-radius: 20px;
    }
    /* Hide Streamlit Menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("Noor 🤍")
st.caption("Your Agentic Lifestyle Architect (Mind • Body • Soul)")

# --- SIDEBAR: USER PROFILE ---
with st.sidebar:
    st.header("👤 User Profile")
    user_name = st.text_input("What should I call you?", value="Honey")
    
    st.divider()
    
    st.markdown("### 🛠️ Mode Status")
    st.info("System acts as a **Supervisor** routing to:")
    st.markdown("- 🧘‍♀️ **Therapist** (Emotional)")
    st.markdown("- ⚡ **Habit Coach** (Discipline)")
    st.markdown("- 🛡️ **Safety** (Crisis)")
    
    # "Reset Memory" Button (Optional, clears UI history)
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# --- SESSION STATE INITIALIZATION ---
# 1. Store the Chat History for the UI
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"🌿 Hello, {user_name}! I am Noor. How is your heart and mind today?"}
    ]

# 2. Store a Thread ID for LangGraph Memory (Persistence)
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# --- DISPLAY CHAT HISTORY ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user", avatar="👤").write(msg["content"])
    else:
        st.chat_message("assistant", avatar="🌿").write(msg["content"])

# --- CHAT INPUT & PROCESSING ---
if user_input := st.chat_input(f"Share your thoughts, {user_name}..."):
    
    # 1. Display User Message Immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user", avatar="👤").write(user_input)

    # 2. Prepare State for LangGraph
    initial_state = {
        "messages": [HumanMessage(content=user_input)],
        "user_name": user_name  # Passing the dynamic name!
    }
    
    config = {"configurable": {"thread_id": st.session_state.thread_id}}

    # 3. Get Response from Noor (The Graph)
    with st.spinner("Noor is listening..."):
        try:
            # We invoke the graph!
            response = app.invoke(initial_state, config=config)
            
            # Extract the actual text content from the last message
            bot_response = response['messages'][-1].content
            
            # 4. Display AI Response
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            st.chat_message("assistant", avatar="🌿").write(bot_response)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
