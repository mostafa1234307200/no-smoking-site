import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

# إعداد الصفحة
st.set_page_config(page_title="حساب تأثير التدخين على صورتك", layout="centered")

# تصميم العنوان والخلفية
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

# العنوان
st.title("📘 تأثير التدخين على الوجه مع مرور الوقت")
st.markdown("🎥 شاهد كيف يمكن أن تتغير ملامح وجهك بعد سنوات من التدخين.")

# رفع الصورة
uploaded_file = st.file_uploader("📷 قم برفع صورتك", type=["jpg", "jpeg", "png"])
age = st.selectbox("اختر عدد السنوات:", [20, 30, 40])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")  # التأكد من أن الصورة بصيغة RGB
    st.image(image, caption="🧍‍♂️ صورتك الأصلية", use_column_width=True)

    if st.button("🔮 عرض تأثير التدخين على ملامحك"):
        with st.spinner("⏳ جاري تطبيق التأثير..."):

            # 1. تعزيز الإضاءة بشكل بسيط
            enhancer = ImageEnhance.Brightness(image)
            brighter_image = enhancer.enhance(1.1)  # زيادة الإضاءة بنسبة 10%

            # 2. إضافة تأثير لتغيير الألوان نحو درجات أكثر دافئة قليلاً
            enhancer = ImageEnhance.Color(brighter_image)
            color_adjusted_image = enhancer.enhance(1.2)  # زيادة الألوان بشكل بسيط

            # 3. زيادة الحدة قليلاً لتحسين التفاصيل
            enhancer = ImageEnhance.Sharpness(color_adjusted_image)
            sharper_image = enhancer.enhance(1.5)  # زيادة الحدة بنسبة 50%

            # 4. إضافة تأثير توهج خفيف
            glow_image = sharper_image.filter(ImageFilter.GaussianBlur(1))  # تأثير ضبابي خفيف لتوهج طبيعي

            # 5. تغيير لون البشرة (زيادة الاحمرار والأصفر لزيادة تأثير التدخين)
            r, g, b = glow_image.split()

            # تعديل قناة اللون الأحمر لزيادة الاحمرار بشكل بسيط
            r = r.point(lambda i: min(i + 30, 255))  # زيادة الاحمرار

            # تعديل قناة اللون الأخضر لزيادة اللون الأصفر قليلًا
            g = g.point(lambda i: min(i + 10, 255))  # زيادة الأصفر

            # دمج القنوات المعدلة
            warm_image = Image.merge("RGB", (r, g, b))

            # 6. إضافة خطوط للتجاعيد (يتم إضافة خطوط داكنة على الوجه لمحاكاة التجاعيد)
            draw = ImageDraw.Draw(warm_image)
            width, height = warm_image.size

            # إضافة خطوط تجاعيد حول العين والفم
            # خطوط العين
            draw.line((width * 0.35, height * 0.35, width * 0.45, height * 0.45), fill=(80, 80, 80), width=2)
            draw.line((width * 0.40, height * 0.38, width * 0.50, height * 0.48), fill=(80, 80, 80), width=2)

            # خطوط حول الفم
            draw.line((width * 0.35, height * 0.60, width * 0.45, height * 0.65), fill=(80, 80, 80), width=2)
            draw.line((width * 0.45, height * 0.63, width * 0.55, height * 0.68), fill=(80, 80, 80), width=2)

            # 7. إظهار الصورة النهائية مع التجاعيد
            st.image(warm_image, caption=f"📆 صورتك بعد {age} سنة من التدخين", use_column_width=True)
