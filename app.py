import cv2
import face_recognition
import numpy as np

def increase_age(image_path, age_increase=20):
    # تحميل الصورة
    image = cv2.imread(image_path)

    # تحويل الصورة إلى RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # العثور على معالم الوجه
    face_landmarks_list = face_recognition.face_landmarks(rgb_image)

    if not face_landmarks_list:
        print("لم يتم العثور على أي وجه في الصورة.")
        return

    # تحديد معالم الوجه من أول وجه موجود
    face_landmarks = face_landmarks_list[0]

    # زيادة العمر عن طريق تغيير معالم الوجه (مؤقتًا باستخدام تضخيم)
    # يمكننا زيادة المسافة بين ملامح الوجه لتغيير ملامح الشيخوخة
    for facial_feature in face_landmarks:
        for point in face_landmarks[facial_feature]:
            point = (int(point[0] * 1.1), int(point[1] * 1.1))  # تضخيم النقاط لزيادة العمر

    # عرض الصورة مع التعديل (دون تغيير الصورة الأصلية)
    cv2.imshow("Aged Face", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# استخدام الكود
increase_age("path_to_your_image.jpg", age_increase=20)
