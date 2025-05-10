import streamlit as st
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

# ✅ تنسيق CSS للخلفية والنصوص
st.markdown("""
    <style>
        .stApp {
            background-color: #800000;  /* خلفية عنابية */
            color: white;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        h1, h2 {
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border: none;
            border-radius: 4px;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ العنوان
st.markdown("<h1>📘 مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h2>🚭 كيف سيؤثر الدخان عليك بعد عشرين أو ثلاثين سنة؟</h2>", unsafe_allow_html=True)

# ✅ رفع الصورة واختيار عدد السنوات
uploaded_file = st.file_uploader("📷 ارفع صورتك (jpg أو png)", type=["jpg", "jpeg", "png"])
age = st.selectbox("اختر عدد السنوات:", [20, 30])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")  # تأكد من أن الصورة بصيغة RGB
    st.image(image, caption="🧍‍♂️ صورتك الأصلية", use_column_
