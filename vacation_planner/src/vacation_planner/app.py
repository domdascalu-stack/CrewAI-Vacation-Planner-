
import streamlit as st
import requests

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Epic Vacation Planner",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
if "destination" not in st.session_state:
    st.session_state.destination = ""

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main background */
.stApp {
    background:
        radial-gradient(circle at top left, rgba(0,180,216,0.15), transparent 30%),
        radial-gradient(circle at bottom right, rgba(6,214,160,0.12), transparent 30%),
        linear-gradient(135deg, #f8fbff 0%, #eef7ff 100%);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.65);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.3);
}

/* Hero Title */
.hero-title {
    font-size: 4.5rem;
    font-weight: 800;
    text-align: center;
    line-height: 1.1;

    background: linear-gradient(
        90deg,
        #00B4D8,
        #06D6A0,
        #FFD166,
        #118AB2
    );

    background-size: 300% 300%;
    animation: gradientMove 8s ease infinite;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

/* Subtitle */
.hero-subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #5c6770;
    margin-bottom: 3rem;
    font-weight: 500;
}

/* Glass container */
.glass-card {
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(16px);
    border-radius: 30px;
    padding: 2.5rem;
    border: 1px solid rgba(255,255,255,0.35);
    box-shadow: 0 10px 35px rgba(0,0,0,0.08);
}

/* Input */
.stTextInput > div > div > input {
    border-radius: 18px;
    border: none;
    padding: 1rem;
    background: rgba(255,255,255,0.85);
    font-size: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

/* Main button */
.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: none;
    padding: 0.75rem 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    background: linear-gradient(135deg, #00B4D8, #06D6A0);
    color: white;
    box-shadow: 0 8px 20px rgba(0,180,216,0.25);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 24px rgba(0,180,216,0.35);
}

/* Destination cards */
.destination-card {
    background: rgba(255,255,255,0.7);
    border-radius: 20px;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 5px 18px rgba(0,0,0,0.06);
    transition: all 0.3s ease;
}

.destination-card:hover {
    transform: translateY(-5px);
}

/* Result Box */
.result-box {
    background: rgba(255,255,255,0.7);
    border-radius: 24px;
    padding: 2rem;
    margin-top: 2rem;
    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* Animation */
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Hide Streamlit Footer */
footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:

    st.markdown("## 🌎 Epic Menu")

    menu = st.selectbox(
        "Navigation",
        ["Plan Vacation", "About", "Contact"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("""
### ✨ Features

- AI Travel Planning
- Personalized Itineraries
- Local Food Discovery
- Hidden Gems
- Budget Suggestions
- Smart Recommendations
""")

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------
st.markdown(
    """
    <div class='hero-title'>
        🌴 Epic Vacation Planner ✈️
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='hero-subtitle'>
        Luxury AI-Powered Travel Planning Experience
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# API URL
# ---------------------------------------------------
API_URL = "https://7k2sclijkh.execute-api.us-west-2.amazonaws.com/default/vacation_planner01"

# ---------------------------------------------------
# PLAN PAGE
# ---------------------------------------------------
if menu == "Plan Vacation":

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    st.markdown("### 🌍 Choose Your Dream Destination")

    destination = st.text_input(
        "",
        value=st.session_state.destination,
        placeholder="✨ Bali, Tokyo, Maldives, Santorini..."
    )

    st.session_state.destination = destination

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 🔥 Popular Destinations")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🏖️ Bali"):
            st.session_state.destination = "Bali"
            st.rerun()

    with col2:
        if st.button("🗼 Tokyo"):
            st.session_state.destination = "Tokyo"
            st.rerun()

    with col3:
        if st.button("🌴 Maldives"):
            st.session_state.destination = "Maldives"
            st.rerun()

    with col4:
        if st.button("🇬🇷 Santorini"):
            st.session_state.destination = "Santorini"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("🚀 Generate My Luxury Vacation Plan"):

        if st.session_state.destination:

            with st.spinner("🌊 Crafting your dream escape..."):

                try:

                    response = requests.post(
                        API_URL,
                        json={"prompt": st.session_state.destination}
                    )

                    if response.status_code == 200:

                        data = response.json()

                        st.balloons()

                        st.success(
                            f"🎉 Your {st.session_state.destination} luxury itinerary is ready!"
                        )

                        st.markdown("## 🗺️ Your Personalized Vacation Plan")

                        vacation_plan = data["result"]

                        st.markdown(
                            f"""
                            <div class='result-box'>
                            {vacation_plan}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    else:
                        st.error(f"API Error: {response.status_code}")

                except Exception as e:
                    st.error(f"Error: {str(e)}")

        else:
            st.warning("Please select or enter a destination.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# ABOUT PAGE
# ---------------------------------------------------
elif menu == "About":

    st.markdown("## 🌊 About Epic Vacation Planner")

    st.write("""
Epic Vacation Planner is a next-generation AI travel experience powered by:

- Amazon Bedrock
- AgentCore Runtime
- CrewAI
- Streamlit

### ✨ What Makes It Special?

- Personalized luxury itineraries
- Local hidden gems
- Food recommendations
- Smart AI travel planning
- Beautiful modern experience
""")

# ---------------------------------------------------
# CONTACT PAGE
# ---------------------------------------------------
elif menu == "Contact":

    st.markdown("## 📞 Contact")

    st.write("""
### 🌴 Epic Vacation Planner

📧 support@epicvacationplanner.ai

🌍 Built with AI + Travel Passion
""")
```
