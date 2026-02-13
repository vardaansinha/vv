import streamlit as st
import time
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(page_title="For My Valentine 💕", page_icon="💘")

# -----------------------
# Styling
# -----------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #ffdde1, #ee9ca7);
        text-align: center;
    }
    .big-text {
        font-size: 48px;
        font-weight: bold;
        color: #b30059;
        margin-top: 20px;
    }
    .reason-text {
        font-size: 26px;
        color: #800040;
        margin-top: 40px;
    }
    .final-text {
        font-size: 42px;
        font-weight: bold;
        color: #660033;
        margin-top: 60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------
# Title
# -----------------------
st.markdown('<div class="big-text">A Very Important Question…</div>', unsafe_allow_html=True)

# -----------------------
# Cinematic Countdown
# -----------------------
local_tz = ZoneInfo("America/Los_Angeles")  # <-- adjust if needed

now = datetime.now(local_tz)

valentines_day = datetime(now.year, 2, 14, 0, 0, 0, tzinfo=local_tz)

if now > valentines_day:
    valentines_day = datetime(now.year + 1, 2, 14, 0, 0, 0, tzinfo=local_tz)

time_left = valentines_day - now

days = time_left.days
hours = time_left.seconds // 3600
minutes = (time_left.seconds % 3600) // 60
seconds = time_left.seconds % 60
st.markdown(
    f"""
    <div style="text-align:center; margin-top:30px;">
        <div style="
            font-size: 60px;
            font-weight: 800;
            letter-spacing: 4px;
            color: #b30059;
        ">
            {days:02d} : {hours:02d} : {minutes:02d} : {seconds:02d}
        </div>
        <div style="
            font-size: 16px;
            margin-top:10px;
            color: #660033;
            letter-spacing: 2px;
        ">
            DAYS &nbsp;&nbsp;&nbsp;&nbsp; HOURS &nbsp;&nbsp;&nbsp;&nbsp; MINUTES &nbsp;&nbsp;&nbsp;&nbsp; SECONDS
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -----------------------
# Session State
# -----------------------
if "stage" not in st.session_state:
    st.session_state.stage = 0

# -----------------------
# Stage 0
# -----------------------
if st.session_state.stage == 0:
    if st.button("💌 Open"):
        st.session_state.stage = 1
        st.rerun()

# -----------------------
# Stage 1
# -----------------------
elif st.session_state.stage == 1:
    if st.button("💖 Start"):
        st.session_state.stage = 2
        st.rerun()

# -----------------------
# Stage 2 – Animated Reasons
# -----------------------
elif st.session_state.stage == 2:

    reasons = [
        "You genuinely are the strongest person I know. Through every thick and thin, you keep persevering and working hard, and that inspires me every single day.",
        "I love how sweet you are. At any point in time, you never fail to make me smile with the way you talk to me, tell me about your day, and look at me with those big eyes. From the beginning till the grave, I will always melt at your eyes.",
        "I was talking to my friends the other day, and I was telling them about how funny you are. You have a unique way of making me laugh and putting a smile on my face, even when you aren't trying to.",
        "You're my best friend. There is no other person I would rather be in a relationship with, and there is no other person that I would've rather been with during long-distance. Thank you so much for enhancing this experience.",
        "The value and impact you add is something I could have never imagined. I could never visualize life without you. You've made me realize how lucky I am that I have someone to miss."
    ]

    placeholder = st.empty()

    for reason in reasons:
        placeholder.markdown(
            f'<div class="reason-text">{reason}</div>',
            unsafe_allow_html=True
        )
        time.sleep(10)

    time.sleep(1)

    st.session_state.stage = 3
    st.rerun()

# -----------------------
# Stage 3 – Final Question
# -----------------------
elif st.session_state.stage == 3:

    st.markdown(
        '<div class="final-text">Will you be my Valentine? 💕</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes 💕"):
            st.balloons()
            st.success("Good decision cutie 😌💖")

    with col2:
        if st.button("Hell YEA 😎"):
            st.balloons()
            st.success("YOU CHOSE CORRECTLY YURRRR 💘✨")

# -----------------------
# Live Refresh Every Second
# -----------------------
time.sleep(1)
st.rerun()
