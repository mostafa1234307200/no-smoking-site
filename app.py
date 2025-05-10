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
    st.image(image, caption="🧍‍♂️ صورتك الأصلية", use_column_width=True)  # تم إغلاق القوس بشكل صحيح

    if st.button("🔮 عرض تأثير التدخين عليك"):
        with st.spinner("⏳ جاري تطبيق التأثير..."):

            # 1. تقليل التشبع (ألوان باهتة) لجعل الصورة تبدو قديمة
            less_color = ImageEnhance.Color(image).enhance(0.5)

            # 2. زيادة التباين لإبراز الملامح أكثر
            more_contrast = ImageEnhance.Contrast(less_color).enhance(1.3)

            # 3. إضافة صبغة صفراء خفيفة (محاكاة لتأثيرات الشيخوخة على الجلد)
            r, g, b = more_contrast.split()
            r = r.point(lambda i: min(i + 15, 255))  # زيادة الصبغة الحمراء قليلاً
            g = g.point(lambda i: min(i + 10, 255))  # زيادة الصبغة الخضراء قليلاً
            yellow_tone = Image.merge("RGB", (r, g, b))

            # 4. زيادة الحدة (لتبرز تفاصيل الوجه)
            sharper = ImageEnhance.Sharpness(yellow_tone).enhance(1.7)

            # 5. تطبيق فلتر لتحسين التفاصيل (إبراز التجاعيد والعمر)
            aged = sharper.filter(ImageFilter.DETAIL)

            # عرض النتيجة النهائية
            st.image(aged, caption=f"📆 صورتك بعد {age} سنة من التدخين", use_column_width=True)
