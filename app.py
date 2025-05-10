import streamlit as st
from PIL import Image, ImageEnhance

st.title("👵 تأثير شيخوخة بسيط على صورتك")

uploaded_file = st.file_uploader("📷 ارفع صورتك (jpg أو png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة الأصلية", use_column_width=True)

    if st.button("تطبيق تأثير الشيخوخة"):
        with st.spinner("⏳ جاري المعالجة..."):
            # 1. تقليل التشبع قليلاً
            converter = ImageEnhance.Color(image)
            less_color = converter.enhance(0.7)

            # 2. إضافة درجة صفراء خفيفة للبشرة (إيحاء الجلد المتقدم)
            r, g, b = less_color.split()
            r = r.point(lambda i: i + 10 if i < 245 else 255)
            g = g.point(lambda i: i + 10 if i < 245 else 255)
            aged = Image.merge("RGB", (r, g, b))

            # 3. زيادة الحدة قليلًا
            sharpness = ImageEnhance.Sharpness(aged)
            final = sharpness.enhance(1.3)

            st.image(final, caption="بعد تطبيق تأثير الشيخوخة", use_column_width=True)
