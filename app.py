import streamlit as st
import requests
from PIL import Image
import io

# إعداد الصفحة
st.set_page_config(page_title="مدرسة الأردن الأساسية المختلطة", layout="centered")

# تصميم CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #800000;
            color: white;
            font-family: 'Arial', sans-serif;
            padding: 20px;
        }
        h1, h2 {
            text-align: center;
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
        }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.markdown("<h1>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h2>شاهد كيف ستبدو بعد 20 أو 30 أو 40 سنة من التدخين</h2>", unsafe_allow_html=True)

# مفتاح API
API_KEY = "42abcfa1f2744a0a98d3ac47c25d8473"

# رفع الصورة
uploaded_file = st.file_uploader("📷 قم برفع صورتك", type=["jpg", "jpeg", "png"])
age = st.selectbox("اختر عدد السنوات:", [20, 30, 40])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 صورتك الأصلية", use_column_width=True)

    if st.button("🔮 عرض صورتك بعد التدخين"):
        with st.spinner("⏳ جاري معالجة صورتك..."):
            try:
                url = "https://api.luxand.cloud/photo/age"
                headers = {"token": API_KEY}
                files = {"photo": uploaded_file.getvalue()}
                data = {"age": age}

                response = requests.post(url, headers=headers, files=files, data=data)

                if response.status_code == 200:
                    result_image = Image.open(io.BytesIO(response.content))
                    st.image(result_image, caption=f"📆 صورتك بعد {age} سنة من التدخين", use_column_width=True)
                else:
                    st.error(f"❌ حدث خطأ أثناء المعالجة: {response.status_code}")
                    st.text(response.text)

            except Exception as e:
                st.error("⚠️ فشل الاتصال بالخادم أو معالجة الصورة.")
                st.text(str(e))
