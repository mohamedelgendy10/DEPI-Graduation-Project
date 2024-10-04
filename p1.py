import streamlit as st
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
    logo_left_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/images%20(2).png"  # الشعار الأيسر
    st.image(logo_left_url, width=125)  # حجم الشعار 50 بيكسل

# إضافة الشعار في أقصى اليمين
with col2:
    logo_right_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/20231126120517!%D9%88%D8%B2%D8%A7%D8%B1%D8%A9_%D8%A7%D9%84%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA_%D9%88%D8%AA%D9%83%D9%86%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A7_%D8%A7%D9%84%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA.png"  # الشعار الأيمن
    st.image(logo_right_url, width=125)  # حجم الشعار 50 بيكسل

# عرض المحتوى بناءً على القسم المختار
st.markdown("---")  # خط فاصل لتوضيح مكان المحتوى

if selected == "Dataset Overview":
    st.title("Dataset Overview")
    
    # إضافة صورة افتتاحية
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E0.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="Welcome to the Dataset Overview", use_column_width=True)
    
    # محتوى القسم
    st.markdown("### Overview of the Dataset")
    st.markdown("""
    This section provides detailed information about the dataset used in this project.
    """)
    # يمكن إضافة المزيد من المحتويات هنا مثل تحميل البيانات أو عرض الجداول.
    
elif selected == "RFM Analysis":
    st.title("RFM Analysis")
    # محتوى قسم RFM Analysis

elif selected == "Purchases Prediction":
    st.title("Purchases Prediction")
    # محتوى قسم Purchases Prediction

elif selected == "Meet Our Team":
    st.title("Meet Our Team")
    
    # تنظيم الفريق في صفين
    st.write("---")
    col1, col2 = st.columns([1, 1])

    # العضو الأول - Mohamed Elgendy
    with col1:
        st.markdown("### Mohamed Elgendy")
        st.markdown("**Project Lead**")
        linkedin_icon_mohamed = """
            <a href="https://www.linkedin.com/in/mohamed-rezk-elgendy" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        """
        st.markdown(linkedin_icon_mohamed, unsafe_allow_html=True)

    # العضو الثاني - Member 2
    with col2:
        st.markdown("### Member 2")
        st.markdown("**Data Analyst**")
        linkedin_icon_member2 = """
            <a href="https://www.linkedin.com/in/member2" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        """
        st.markdown(linkedin_icon_member2, unsafe_allow_html=True)

    st.write("---")

    col3, col4 = st.columns([1, 1])

    # العضو الثالث - Member 3
    with col3:
        st.markdown("### Member 3")
        st.markdown("**Developer**")
        linkedin_icon_member3 = """
            <a href="https://www.linkedin.com/in/member3" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        """
        st.markdown(linkedin_icon_member3, unsafe_allow_html=True)

    # العضو الرابع - Member 4
    with col4:
        st.markdown("### Member 4")
        st.markdown("**Data Scientist**")
        linkedin_icon_member4 = """
            <a href="https://www.linkedin.com/in/member4" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        """
        st.markdown(linkedin_icon_member4, unsafe_allow_html=True)
