import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# تهيئة التصميم
st.set_page_config(page_title="Your App Title", page_icon="🎉", layout="wide")

# تخطيط الأعمدة لإضافة الشعارين
col1, col2 = st.columns([1, 5])  # عمود للشعار الأيسر وآخر للمحتوى الأيمن

# إضافة الشعار في أقصى اليسار
with col1:
    logo_left_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/images%20(2).png"  # الشعار الأيسر
    st.image(logo_left_url, width=125)  # حجم الشعار 125 بيكسل

# إضافة الشعار في أقصى اليمين
with col2:
    logo_right_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/20231126120517!%D9%88%D8%B2%D8%A7%D8%B1%D8%A9_%D8%A7%D9%84%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA_%D9%88%D8%AA%D9%83%D9%86%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A7_%D8%A7%D9%84%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA.png"  # الشعار الأيمن
    st.image(logo_right_url, width=125)  # حجم الشعار 125 بيكسل

# شريط جانبي رأسي للتنقل مع الأيقونات
with st.container():  # استخدام الحاوية لتصميم أكثر احترافية
    st.sidebar.title("Main Menu")  # عنوان الشريط الجانبي
    selected = option_menu(
        menu_title=None,  # إزالة عنوان القائمة
        options=["Dataset Overview", "RFM Analysis", "Purchases Prediction", "Meet Our Team"],  # الأقسام
        icons=["info-circle", "bar-chart-line", "graph-up-arrow", "people-fill"],  # أيقونات الأقسام
        menu_icon="cast",  # أيقونة القائمة
        default_index=0,  # الخيار الافتراضي
        orientation="vertical"  # جعل القائمة رأسية
    )

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
    st.image("https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/mohamed_image.png", caption="Mohamed Elgendy", width=100)  # رابط صورة محمد

    st.markdown("""
    **Member 2**  
    Role: Data Analyst  
    Responsible for analyzing the data and deriving insights.
    """)
    st.image("https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/member2_image.png", caption="Member 2", width=100)  # رابط صورة العضو الثاني

    st.markdown("""
    **Member 3**  
    Role: Developer  
    Handles the backend development and ensures the app runs smoothly.
    """)
    st.image("https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/member3_image.png", caption="Member 3", width=100)  # رابط صورة العضو الثالث
