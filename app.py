import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
from io import BytesIO

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

# ✅ اسم المدرسة والعنوان
st.markdown("<h1>📘 مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h2>🚭 كيف سيؤثر الدخان عليك بعد عشرين أو ثلاثين سنة؟</h2>", unsafe_allow_html=True)

# ✅ رفع الصورة واختيار عدد السنوات
uploaded_file = st.file_uploader("📷 ارفع صورتك (jpg أو png)", type=["jpg", "jpeg", "png"])
age = st.selectbox("اختر عدد السنوات:", [20, 30])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="🧍‍♂️ صورتك الأصلية", use_column_width=True)

    if st.button("🔮 عرض تأثير التدخين عليك"):
        with st.spinner("⏳ جاري تطبيق التأثير..."):

            # 1. تقليل التشبع
            less_color = ImageEnhance.Color(image).enhance(0.5)

            # 2. زيادة التباين
            more_contrast = ImageEnhance.Contrast(less_color).enhance(1.3)

            # 3. إضافة صبغة صفراء
            r, g, b = more_contrast.split()
            r = r.point(lambda i: min(i + 15, 255))
            g = g.point(lambda i: min(i + 10, 255))
            yellow_tone = Image.merge("RGB", (r, g, b))

            # 4. زيادة الحدة
            sharper = ImageEnhance.Sharpness(yellow_tone).enhance(1.7)

            # 5. إبراز التجاعيد
            aged = sharper.filter(ImageFilter.DETAIL)

            # 6. إضافة تجاعيد اصطناعية
            wrinkle_overlay = Image.open("wrinkles_overlay.png").convert("RGBA")
            wrinkle_overlay = wrinkle_overlay.resize(image.size)
            aged_with_wrinkles = Image.alpha_composite(aged.convert("RGBA"), wrinkle_overlay)
            aged_with_wrinkles = aged_with_wrinkles.convert("RGB")

            # 7. تغبيش موضعي لمحاكاة ترهل الجلد
            face_area = (100, 100, 400, 400)  # اضبط حسب حجم الصورة
            mask = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rectangle(face_area, fill=255)
            blurred = aged_with_wrinkles.filter(ImageFilter.GaussianBlur(radius=4))
            final_image = Image.composite(aged_with_wrinkles, blurred, mask)

            # ✅ عرض النتيجة
            st.image(final_image, caption=f"📆 صورتك بعد {age} سنة من التدخين", use_column_width=True)

            # ✅ تعليق توعوي
            st.markdown("🚭 <b>تذكّر:</b> التدخين لا يؤثر فقط على مظهرك، بل على صحتك العامة والقلب والرئة!", unsafe_allow_html=True)

            # ✅ زر تحميل الصورة
            buf = BytesIO()
            final_image.save(buf, format="PNG")
            buf.seek(0)
            st.download_button(
                label="📥 تحميل الصورة المعدلة",
                data=buf,
                file_name="aged_face.png",
                mime="image/png"
            )
