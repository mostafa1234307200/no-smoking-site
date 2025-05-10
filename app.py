import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

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
            r = r.point(lambda i: min(i + 15, 255))  # زيادة الاحمرار

            # تعديل قناة اللون الأخضر لزيادة اللون الأصفر قليلًا
            g = g.point(lambda i: min(i + 5, 255))  # زيادة الأصفر

            # دمج القنوات المعدلة
            warm_image = Image.merge("RGB", (r, g, b))

            # 6. إضافة تأثيرات إضافية بناءً على العمر
            if age == 20:
                # تأثير خفيف للتدخين بعد 20 سنة
                enhancer = ImageEnhance.Contrast(warm_image)
                final_image = enhancer.enhance(1.1)  # زيادة التباين بنسبة 10% لإعطاء تأثير خفيف
            elif age == 30:
                # تأثير متوسط للتدخين بعد 30 سنة
                enhancer = ImageEnhance.Contrast(warm_image)
                final_image = enhancer.enhance(1.3)  # زيادة التباين بنسبة 30% لإعطاء تأثير متوسط
            elif age == 40:
                # تأثير قوي للتدخين بعد 40 سنة
                enhancer = ImageEnhance.Contrast(warm_image)
                final_image = enhancer.enhance(1.5)  # زيادة التباين بنسبة 50% لإعطاء تأثير قوي

            # 7. إظهار الصورة النهائية مع تأثيرات التدخين
            st.image(final_image, caption=f"📆 صورتك بعد {age} سنة من التدخين", use_column_width=True)
