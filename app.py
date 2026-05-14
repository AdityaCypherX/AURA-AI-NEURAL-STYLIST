import streamlit as st
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AURA AI | Fashion Architect",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.main {
    background-color: #0a0a12;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #112240;
    border-right: 2px solid #64ffda;
}

.stButton>button {
    background: linear-gradient(45deg,#64ffda,#48cae4);
    color: black;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px #64ffda;
}

.result-box {
    padding:20px;
    border-radius:15px;
    background: rgba(255,255,255,0.05);
    border:1px solid #64ffda;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# MEDIAPIPE FACE DETECTION
# -----------------------------------

mp_face = mp.solutions.face_detection

face_detector = mp_face.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.5
)

# -----------------------------------
# SKIN DETECTION FUNCTION
# -----------------------------------

def detect_skin_tone(img_array):

    # Convert RGB → BGR
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Face Detection
    results = face_detector.process(img_array)

    # No face found
    if not results.detections:
        return None, None, None, None, None

    h, w, _ = img_bgr.shape

    # First detected face
    detection = results.detections[0]

    bbox = detection.location_data.relative_bounding_box

    x = int(bbox.xmin * w)
    y = int(bbox.ymin * h)
    bw = int(bbox.width * w)
    bh = int(bbox.height * h)

    # Safety boundaries
    x = max(0, x)
    y = max(0, y)

    # Draw rectangle
    cv2.rectangle(
        img_bgr,
        (x, y),
        (x + bw, y + bh),
        (0, 255, 0),
        3
    )

    # Crop face
    face = img_bgr[y:y+bh, x:x+bw]

    # Convert face to HSV
    hsv = cv2.cvtColor(face, cv2.COLOR_BGR2HSV)

    # Skin color range
    lower_skin = np.array([0, 30, 60], dtype=np.uint8)
    upper_skin = np.array([25, 255, 255], dtype=np.uint8)

    # Skin mask
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Noise removal
    kernel = np.ones((3,3), np.uint8)

    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # Extract skin
    skin = cv2.bitwise_and(face, face, mask=mask)

    # Get skin pixels
    skin_pixels = hsv[:, :, 2][mask > 0]

    if len(skin_pixels) == 0:
        return None, None, None, None, None

    avg_skin = np.mean(skin_pixels)

    # -----------------------------------
    # COMPLEXION CLASSIFICATION
    # -----------------------------------

    if avg_skin > 170:

        complexion = "Fair / Light"
        colors = "Emerald Green, Navy Blue, Lavender"
        undertone = "Cool"

    elif avg_skin > 130:

        complexion = "Medium / Olive"
        colors = "Mustard, Teal, Earthy Browns"
        undertone = "Warm"

    elif avg_skin > 90:

        complexion = "Tan / Mid-Dark"
        colors = "White, Sky Blue, Royal Purple"
        undertone = "Neutral"

    else:

        complexion = "Deep Dark"
        colors = "Bright Red, Cobalt Blue, Gold"
        undertone = "Bold"

    # Convert images for Streamlit
    detected_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    skin_img = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)

    return complexion, colors, undertone, detected_img, skin_img

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.markdown(
        "<h1 style='color:#64ffda;'>🛡️ AURA AI</h1>",
        unsafe_allow_html=True
    )

    st.write("---")

    st.info("Capture your face for AI skin analysis")

    st.warning("Use good lighting for best accuracy")

    img_file = st.camera_input("📸 Open Camera")

    analyze_btn = st.button("🔍 ANALYZE MY STYLE")

    st.write("---")

    st.markdown("""
    ### 📖 About Project

    AURA AI uses:
    
    ✔ MediaPipe Face Detection  
    ✔ OpenCV Skin Segmentation  
    ✔ AI Fashion Recommendation  

    to analyze real facial skin tones
    and suggest personalized fashion colors.
    """)

# -----------------------------------
# MAIN LAYOUT
# -----------------------------------

col1, col2 = st.columns([1, 1.2])

# -----------------------------------
# LEFT SIDE
# -----------------------------------

with col1:

    st.header("📷 Live Camera Feed")

    if img_file:

        image = Image.open(img_file)

        img_array = np.array(image)

        st.image(
            img_array,
            width="stretch"
        )

    else:

        st.warning("Waiting for image...")

# -----------------------------------
# RIGHT SIDE
# -----------------------------------

with col2:

    st.header("🧠 AI Fashion Dashboard")

    if analyze_btn and img_file:

        with st.spinner("Analyzing skin tone..."):

            complexion, colors, undertone, detected_img, skin_img = detect_skin_tone(img_array)

        # No face detected
        if complexion is None:

            st.error("Face/Skin not detected properly")

        else:

            st.success("Analysis Complete")

            # Face Detection Image
            st.image(
                detected_img,
                caption="Detected Face",
                width="stretch"
            )

            # Skin Detection Image
            st.image(
                skin_img,
                caption="Detected Skin Region",
                width="stretch"
            )

            # Result Card
            st.markdown(f"""
            <div class="result-box">

            <h2 style="color:#64ffda;">
            Analysis Result
            </h2>

            <p>
            <b>Detected Complexion:</b>
            {complexion}
            </p>

            <p>
            <b>Undertone:</b>
            {undertone}
            </p>

            <p>
            <b>Recommended Palette:</b>

            <span style="color:#48cae4;">
            {colors}
            </span>
            </p>

            <hr>

            <p>
            <i>
            Fashion AI suggests these colors
            will enhance your natural appearance.
            </i>
            </p>

            </div>
            """, unsafe_allow_html=True)

            # -----------------------------------
            # AMAZON LINKS
            # -----------------------------------

            st.subheader("🛒 Recommended Fashion")

            items = [
                "Shirt",
                "Blazer",
                "Kurta",
                "Sneakers"
            ]

            cols = st.columns(4)

            first_color = colors.split(",")[0].strip()

            for i, item in enumerate(items):

                search = first_color.replace(" ", "+")

                url = f"https://www.amazon.in/s?k={search}+{item}"

                cols[i].markdown(f"[{item}]({url})")

            # -----------------------------------
            # REPORT DOWNLOAD
            # -----------------------------------

            report = f"""
AURA AI REPORT

Detected Complexion:
{complexion}

Undertone:
{undertone}

Recommended Colors:
{colors}

AI Fashion Recommendation:
These colors will enhance your natural appearance.
"""

            st.download_button(
                "📥 Download Report",
                report,
                file_name="aura_ai_report.txt"
            )

    elif analyze_btn:

        st.error("Please capture image first")