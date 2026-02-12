from graph import app
from langchain_core.messages import HumanMessage
import uuid

print("Mental Health Bot (Type 'q' to quit)")
MY_NAME = input("What should I call you? ")
BOT_NAME = "Noor🤍"
# --- MEMORY CONFIGURATION ---
# OPTION A: Long-Term Memory (Recommended)
# Noor will remember you even if you close the code and come back tomorrow.
thread_id = f"user_{MY_NAME}_persistent_thread" 

# OPTION B: Short-Term Memory
# thread_id = str(uuid.uuid4()) # Uncomment this if you want a fresh start every time.

# Create the config dictionary that LangGraph needs to save checkpoints
config = {"configurable": {"thread_id": thread_id}}

def print_welcome_message():
    print("\n" + "="*50)
    print(f"🌿  Hello, {MY_NAME}! I am {BOT_NAME},your AI Companion.  🌿")
    print("="*50)
    print("\nI am here to help you balance your Mind, Body, and Soul.")
    print("I have three distinct modes to support you:\n")
    
    print("🧘‍♀️  THERAPIST MODE (Emotional Support)")
    print("    - Vent about stress, anxiety, or relationships.")
    print("    - Get CBT-based reflection and grounding.")
    
    print("⚡  HABIT COACH MODE (Action & Discipline)")
    print("    - Track your 10k steps, water, or study goals.")
    print("    - Get 'tough love' for procrastination.")
    
    print("🛡️  SAFETY MODE (Crisis Intervention)")
    print("    - Immediate resources if you feel unsafe.")
    
    print("\n💡  TRY SAYING:")
    print("    • \"I feel really overwhelmed with my studies today.\"")
    print("    • \"I just walked 10,000 steps!\"")
    print("    • \"I'm feeling lonely and overthinking everything.\"")
    print("    • \"I'm too lazy to clean my room, help me.\"")
    print("-" * 50 + "\n")

print_welcome_message()

while True:
    user_input = input(f"✨{MY_NAME}: ")
    if user_input.lower() in ['q','quit',"exit", 'bye']:
        print("👋 Goodbye! Take care of yourself.")
        break

    # Skip empty inputs
    if not user_input.strip():
        continue
    # Prepare the state 
    initial_state ={
        "messages": [HumanMessage(content=user_input)],
        "user_name": MY_NAME
        }
    

    try:
        result = app.invoke(initial_state,config=config)

        #The result contains the full updated state(history).
        #We want the very last message, which is the AI's response.
        last_message = result['messages'][-1]
        print(f"\n✨ {BOT_NAME}: {last_message.content}\n")

    except Exception as e:
        print(f"An error occurred: {e}")