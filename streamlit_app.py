import streamlit as st
import requests
import json
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="BaliTour.AI",
    page_icon="🌺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CONSTANTS ---
API_URL = "http://localhost:8000/api"

# --- CUSTOM CSS & STYLING ---
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(90deg, #FF5A5F 0%, #FF8A65 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #555;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Chat Message Styling */
    .stChatMessage {
        background-color: transparent;
    }
    div[data-testid="stChatMessageContent"] {
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    div[data-testid="chatAvatarIcon-user"] {
        background-color: #FF5A5F !important;
    }
    div[data-testid="chatAvatarIcon-assistant"] {
        background-color: #2E86C1 !important;
    }
    
    /* Agent Badges */
    .agent-badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 5px;
        color: white;
    }
    .badge-weather { background-color: #F1C40F; color: #333; }
    .badge-culture { background-color: #9B59B6; }
    .badge-travel { background-color: #2ECC71; }
    .badge-transport { background-color: #E67E22; }
    .badge-itinerary { background-color: #3498DB; }
    .badge-default { background-color: #95A5A6; }

    /* Quick Action Buttons */
    .quick-btn {
        margin: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
def get_agent_color(agent_name):
    colors = {
        "weather": "badge-weather",
        "culture": "badge-culture",
        "travel": "badge-travel",
        "transport": "badge-transport",
        "itinerary": "badge-itinerary"
    }
    return colors.get(agent_name.lower(), "badge-default")

# --- MAIN UI ---

# Header
st.markdown("<h1 class='main-header'>🌺 BaliTour.AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Your Intelligent Companion for the Island of Gods</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # st.image("...", width=60) # Commented out due to load error
    st.markdown("## 🌺 BaliTour.AI")
    
    st.markdown("---")
    
    # 1. Trip Settings
    with st.expander("🛠️ Trip Settings", expanded=True):
        travel_style = st.selectbox("Travel Style", ["Relaxed", "Adventure", "Cultural", "Party"], index=2)
        budget_range = st.select_slider("Budget", options=["Backpacker", "Moderate", "Luxury"], value="Moderate")
        st.caption(f"Preference: {travel_style} | {budget_range}")
    
    # 2. Tools
    with st.expander("⚙️ Developer Tools", expanded=False):
        if st.button("🧹 Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        st.checkbox("Show Inspect Mode", value=False, help="Show raw JSON data from agents")

    # 3. About
    with st.expander("ℹ️ About System", expanded=False):
        st.info("Orchestrating 5 Agents:")
        st.markdown("""
        - 🌦️ **Weather Agent**: Open-Meteo
        - 🎭 **Culture Agent**: ChromaDB RAG
        - 🚕 **Transport Agent**: OpenRouteService
        - 📅 **Itinerary Agent**: Logic Engine
        - 🌏 **Travel Agent**: Groq LLM
        """)
        st.caption("v1.0.0 | System Online 🟢")

# Initialize Chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Om Swastyastu! 🙏 I am your personal AI guide for Bali. How can I help you plan your trip today?"}
    ]

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# Quick Suggestions (only show if chat is empty-ish)
if len(st.session_state.messages) < 2:
    st.markdown("### 💡 **Try asking:**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🇬🇧 Plan a 3-day cultural trip to Ubud", use_container_width=True):
            st.session_state.prompt_input = "Plan a 3-day cultural trip to Ubud"
        if st.button("🇮🇩 Bagaimana cuaca di Kuta besok?", use_container_width=True):
            st.session_state.prompt_input = "Bagaimana cuaca di Kuta besok?"
        if st.button("🇧🇱 Punapi gatra ring Pura Besakih?", use_container_width=True):
            st.session_state.prompt_input = "Punapi gatra ring Pura Besakih?"
            
    with col2:
        if st.button("🇬🇧 Find me a cheap hotel near Canggu", use_container_width=True):
            st.session_state.prompt_input = "Find me a cheap hotel near Canggu"
        if st.button("🇮🇩 Berikan rekomendasi tempat melukat", use_container_width=True):
            st.session_state.prompt_input = "Berikan rekomendasi tempat melukat di Bali"

# Chat Input (Handle button clicks via session state magic or standard input)
# Check for prompt_input in session state
if "prompt_input" in st.session_state and st.session_state.prompt_input:
    user_input_val = st.session_state.prompt_input
    # Clear it immediately to prevent re-trigger on simple reruns without action
    st.session_state.prompt_input = None 
else:
    user_input_val = None

user_input = st.chat_input("Type your question here...")

if user_input:
    prompt = user_input
elif user_input_val:
    prompt = user_input_val
else:
    prompt = None
# Handle button click simulation if implemented (complex in Streamlit, keeping simple)

if prompt:
    # 1. User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Assistant Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Thinking Animation
        with st.status("🧠 **Orchestrating Agents...**", expanded=True) as status:
            time.sleep(0.5) # UX pause
            st.write("🔍 Analyzing Intent...")
            
            try:
                payload = {"query": prompt}
                response = requests.post(f"{API_URL}/agent-chat", json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    final_ans = data.get("response", "No response.")
                    agents_used = data.get("agents_used", [])
                    
                    st.write("✅ Agents coordinated successfully.")
                    status.update(label="**Response Ready!**", state="complete", expanded=False)
                    
                    # Construct badges HTML
                    badges_html = ""
                    if agents_used:
                        for agent in agents_used:
                            css_class = get_agent_color(agent)
                            badges_html += f"<span class='agent-badge {css_class}'>{agent.upper()}</span>"
                        badges_html = f"<div style='margin-bottom:10px;'>{badges_html}</div>"
                    
                    # Render Final Output
                    full_content = badges_html + final_ans
                    message_placeholder.markdown(full_content, unsafe_allow_html=True)
                    
                    st.session_state.messages.append({"role": "assistant", "content": full_content})
                    
                else:
                    status.update(label="❌ Error", state="error")
                    st.error(f"API Error: {response.text}")
            
            except Exception as e:
                status.update(label="❌ Connection Failed", state="error")
                st.error(f"Connection Error: {e}")
