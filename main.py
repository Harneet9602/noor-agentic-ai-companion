from graph import app
from langchain_core.messages import HumanMessage
import uuid

# --- CONFIGURATION ---
print("\n" + "="*60)
print("      🌿 SEHAJ: Stateful Holistic AI Journal 🌿")
print("="*60)

# 1. User Setup
MY_NAME = input("\nFirst, what should I call you? (e.g., Honey): ").strip() or "User"
BOT_NAME = "SEHAJ"

# 2. Memory Configuration (Persistence)
# We use a persistent thread ID so the bot remembers you across messages.
thread_id = f"user_{MY_NAME}_persistent_thread"
config = {"configurable": {"thread_id": thread_id}}

def print_welcome_message():
    """Displays the menu of available agents."""
    print(f"\n✨ Hello, {MY_NAME}! I am {BOT_NAME}, your AI Life Companion.")
    print("I have a team of specialist agents ready to help you:\n")
    
    print("🧘‍♀️  THERAPIST (Serena)   | Emotional support, venting, and CBT.")
    print("🌿  HABIT (Noor)         | Lifestyle discipline, 'Core 4', and consistency.")
    print("⚡  FITNESS (Kai)        | Workouts, sleep tracking, and diet strategy.")
    print("🎓  PROFESSOR (Turing)   | Study planning, concepts, and research papers.")
    print("👾  GAMES (Pixel)        | Distraction, boredom killing, and trivia.")
    print("🛡️  SAFETY (Guardian)    | Crisis intervention and immediate help.")
    
    print("\n💡  TRY ASKING:")
    print("   • \"I'm feeling really anxious about my exams.\" (Routes to Professor/Therapist)")
    print("   • \"Make me a gym plan for glutes.\" (Routes to Fitness)")
    print("   • \"I'm bored, let's play a game.\" (Routes to Pixel)")
    print("   • \"I'm too lazy to clean my room.\" (Routes to Habit)")
    print("-" * 60 + "\n")

# --- MAIN LOOP ---
print_welcome_message()

while True:
    try:
        user_input = input(f"💬 {MY_NAME}: ")
        
        # Exit Condition
        if user_input.lower() in ['q', 'quit', 'exit', 'bye']:
            print(f"👋 Goodbye, {MY_NAME}. Stay balanced.")
            break

        # Skip empty inputs
        if not user_input.strip():
            continue
            
        # Prepare the state
        # We pass the user_name so every agent knows who they are talking to
        initial_state = {
            "messages": [HumanMessage(content=user_input)],
            "user_name": MY_NAME
        }

        # Run the Graph (The Brain)
        # config=config enables the Memory/Checkpointing
        result = app.invoke(initial_state, config=config)

        # Extract the Last Message (The Agent's Response)
        last_message = result['messages'][-1]
        
        print(f"\n✨ {BOT_NAME}: {last_message.content}\n")
        print("-" * 60)

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Tip: Make sure your GROQ_API_KEY is set in .env")