
import streamlit as st
import requests
import json

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Epic Vacation Planner",
    page_icon="🌴",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');

.main-header {
    background: linear-gradient(45deg, #00C9A7, #00B4D8, #90E0EF, #FFD166, #06D6A0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Poppins', sans-serif;
    font-size: 4rem;
    font-weight: 700;
    text-align: center;
    animation: glow 2s ease-in-out infinite alternate;
}

.powered-by {
    text-align: center;
    font-weight: 900;
    background: linear-gradient(45deg, #06D6A0, #118AB2, #FFD166, #00B4D8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Poppins', sans-serif;
    font-size: 2rem;
    margin: 2rem 0;
    animation: pulse 1.5s infinite;
}

.vacation-input {
    background: linear-gradient(135deg, #48CAE4 0%, #90E0EF 100%);
    border: 3px solid transparent;
    border-radius: 25px;
    padding: 2.5rem;
    margin: 2rem 0;
    box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    position: relative;
}

.vacation-input::before {
    content: '';
    position: absolute;
    top: -3px;
    left: -3px;
    right: -3px;
    bottom: -3px;
    background: linear-gradient(45deg, #06D6A0, #00B4D8, #FFD166, #90E0EF);
    border-radius: 25px;
    z-index: -1;
    animation: borderGlow 3s ease-in-out infinite alternate;
}

@keyframes borderGlow {
    0% { opacity: 0.7; transform: scale(1); }
    100% { opacity: 1; transform: scale(1.02); }
}

@keyframes glow {
    from { text-shadow: 0 0 20px rgba(0,201,167,0.5); }
    to { text-shadow: 0 0 30px rgba(17,138,178,0.8); }
}

@keyframes pulse {
    0% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(1.08); opacity: 1; }
    100% { transform: scale(1); opacity: 0.8; }
}

.result-box {
    background: rgba(255,255,255,0.08);
    padding: 2rem;
    border-radius: 20px;
    margin-top: 2rem;
    border: 1px solid rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:
    st.markdown("### 🌎 Menu")

    menu = st.selectbox(
        "Navigation",
        ["Plan Vacation", "About", "Contact"],
        label_visibility="collapsed"
    )

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
    '<h1 class="main-header">🌴 Epic Vacation Planner ✈️</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="powered-by">Powered by Amazon Bedrock AgentCore</p>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# YOUR API URL
# ---------------------------------------------------
API_URL = "https://7k2sclijkh.execute-api.us-west-2.amazonaws.com/default/vacation_planner01"

# ---------------------------------------------------
# PLAN VACATION PAGE
# ---------------------------------------------------
if menu == "Plan Vacation":

    st.markdown('<div class="vacation-input">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        destination = st.text_input(
            "🌍 Dream Destination:",
            placeholder="✨ Bali, Tokyo, Maldives, Santorini..."
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # Popular destinations
    st.markdown("### 🔥 Popular Destinations")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🏖️ Bali", use_container_width=True):
            destination = "Bali"

    with col2:
        if st.button("🗾 Tokyo", use_container_width=True):
            destination = "Tokyo"

    with col3:
        if st.button("🌴 Maldives", use_container_width=True):
            destination = "Maldives"

    with col4:
        if st.button("🇬🇷 Santorini", use_container_width=True):
            destination = "Santorini"

    # Generate button
    if st.button("🚀 Plan My Epic Vacation", type="primary"):

        if destination:

            with st.spinner("🌊 Planning your dream vacation..."):

                try:

                    response = requests.post(
                        API_URL,
                        json={"prompt": destination}
                    )

                    if response.status_code == 200:

                        data = response.json()

                        st.balloons()

                        st.success(f"🎉 Your {destination} vacation plan is ready!")

                        st.markdown("## 🗺️ Your Epic Vacation Plan")

                        vacation_plan = data["result"]

                        st.markdown('<div class="result-box">', unsafe_allow_html=True)

                        st.markdown(vacation_plan)

                        st.markdown('</div>', unsafe_allow_html=True)

                    else:
                        st.error(f"API Error: {response.status_code}")

                except Exception as e:
                    st.error(f"Error: {str(e)}")

        else:
            st.warning("Please enter a destination")

# ---------------------------------------------------
# ABOUT PAGE
# ---------------------------------------------------
elif menu == "About":

    st.markdown("## 🌊 About Epic Vacation Planner")

    st.write("""
    Epic Vacation Planner is an AI-powered travel assistant built using:

    - Amazon Bedrock
    - AgentCore Runtime
    - CrewAI
    - Streamlit

    Features:
    - 🌍 Personalized itineraries
    - 🍴 Local food recommendations
    - 🏖️ Tourist attractions
    - 🗺️ Travel planning
    """)

# ---------------------------------------------------
# CONTACT PAGE
# ---------------------------------------------------
elif menu == "Contact":

    st.markdown("## 📞 Contact")

    st.write("""
    🌴 Epic Vacation Planner
    
    📧 support@epicvacationplanner.ai
    """)


