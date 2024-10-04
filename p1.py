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

if selected == "Meet Our Team":
    st.title("Meet Our Team")
    
    # تفاصيل الفريق
    team_members = [
        {"name": "Mohamed Elgendy", "role": "Project Lead", "linkedin": "www.linkedin.com/in/mohamed-rezk-elgendy"},
        {"name": "Member 2", "role": "Data Analyst", "linkedin": "https://www.linkedin.com/in/member2"},
        {"name": "Member 3", "role": "Developer", "linkedin": "https://www.linkedin.com/in/member3"},
        {"name": "Member 4", "role": "Data Scientist", "linkedin": "https://www.linkedin.com/in/member4"}
    ]

    # تنظيم أعضاء الفريق
    for member in team_members:
        col1, col2 = st.columns([1, 9])
        with col1:
            st.image("https://cdn-icons-png.flaticon.com/512/174/174857.png", width=30)  # أيقونة LinkedIn
        with col2:
            st.markdown(f"**{member['name']}**")
            st.markdown(f"*{member['role']}*")
            st.markdown(f"[![LinkedIn]('https://cdn-icons-png.flaticon.com/512/174/174857.png')](https://{member['linkedin']})")
