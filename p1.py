import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# شريط جانبي للتنقل مع الأيقونات
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # عنوان القائمة
        options=["Dataset Overview", "RFM Analysis", "Purchases Prediction", "Meet Our Team"],  # الأقسام
        icons=["info-circle", "bar-chart-line", "graph-up-arrow", "people-fill"],  # أيقونات الأقسام
        menu_icon="cast",  # أيقونة القائمة
        default_index=0,  # الخيار الافتراضي
    )

# تخطيط الأعمدة لإضافة الشعارين
col1, col2 = st.columns([5, 0.001])  # عمود للشعار الأيسر وآخر للمحتوى الأيمن

# إضافة الشعار في أقصى اليسار
with col1:
    logo_left_path = "https://github.com/mohamedelgendy10/DEPI-Graduation-Project/blob/main/images%20(2).png"  # تأكد من تحديث المسار حسب موقع الشعار لديك
    st.image(logo_left_path, width=125)  # حجم الشعار 50 بيكسل

# إضافة الشعار في أقصى اليمين
with col2:
    logo_right_path = "https://github.com/mohamedelgendy10/DEPI-Graduation-Project/blob/main/20231126120517!%D9%88%D8%B2%D8%A7%D8%B1%D8%A9_%D8%A7%D9%84%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA_%D9%88%D8%AA%D9%83%D9%86%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A7_%D8%A7%D9%84%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA.png"  # تأكد من تحديث المسار حسب موقع الشعار لديك
    st.image(logo_right_path, width=125)  # حجم الشعار 50 بيكسل

# عرض المحتوى بناءً على القسم المختار
st.markdown("---")  # خط فاصل لتوضيح مكان المحتوى
if selected == "Dataset Overview":
    st.title("Dataset Overview")
    st.markdown("### Overview of the Dataset")
    st.markdown("This section provides detailed information about the dataset used in this project, including the structure of the data, the variables, and their types.")
    # يمكنك إضافة تفاصيل إضافية حول البيانات هنا

elif selected == "RFM Analysis":
    st.title("RFM Analysis")
    st.markdown("### RFM Analysis Overview")
    st.markdown("Here you can perform RFM analysis.")
    # يمكنك إضافة محتوى إضافي حسب الحاجة

elif selected == "Purchases Prediction":
    st.title("Purchases Prediction")
    st.markdown("### Purchases Prediction Overview")
    st.markdown("Here you can predict future purchases based on historical data.")
    # يمكنك إضافة محتوى إضافي حسب الحاجة

elif selected == "Meet Our Team":
    st.title("Meet Our Team")
    
    # معلومات الفريق
    st.markdown("""
    **Mohamed Elgendy**  
    Project Lead  
    Mohamed is responsible for leading the project and ensuring its success.
    """)

    st.markdown("""
    **Member 2**  
    Role: Data Analyst  
    Responsible for analyzing the data and deriving insights.
    """)

    st.markdown("""
    **Member 3**  
    Role: Developer  
    Handles the backend development and ensures the app runs smoothly.
    """)

    # إضافة صور الفريق (تأكد من توفير المسار الصحيح للصور)
    st.image("path_to_mohamed_image.jpg", caption="Mohamed Elgendy", width=100)
    st.image("path_to_member2_image.jpg", caption="Member 2", width=100)
    st.image("path_to_member3_image.jpg", caption="Member 3", width=100)
