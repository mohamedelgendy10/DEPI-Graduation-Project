import streamlit as st
from streamlit_option_menu import option_menu

# تهيئة التصميم
st.set_page_config(page_title="Your App Title", page_icon="🌍", layout="wide")

# إضافة تنسيق مخصص باستخدام markdown و CSS
st.markdown("""
    <style>
    .main-menu {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 5px;
    }
    .menu-item {
        font-size: 20px;
        color: #007bff;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .menu-item:hover {
        color: #0056b3;
    }
    .icon {
        color: #28a745;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية باستخدام القائمة المخصصة
with st.sidebar:
    selected = option_menu(
        menu_title=None,  # إزالة العنوان لتبدو القائمة احترافية
        options=["🏠 Home", "📊 Dataset Overview", "📈 RFM Analysis", "🔮 Purchases Prediction", "💼 Meet Our Team"],  # الأقسام مع الأيقونات
        icons=["house", "bar-chart-line", "graph-up-arrow", "graph-down-arrow", "people-fill"],  # أيقونات الأقسام
        menu_icon="list",  # أيقونة القائمة
        default_index=0,  # الخيار الافتراضي
        orientation="horizontal",  # جعل القائمة أفقية مثل المواقع الاحترافية
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "green", "font-size": "25px"},
            "nav-link": {
                "font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#0d6efd"},
        }
    )

# عرض المحتوى بناءً على القسم المختار
st.markdown("---")  # خط فاصل لتوضيح مكان المحتوى

if selected == "🏠 Home":
    st.title("Welcome to the App")
    st.write("This is the home section of your app.")

elif selected == "📊 Dataset Overview":
    st.title("Dataset Overview")
    st.markdown("### Overview of the Dataset")
    st.write("This section provides detailed information about the dataset.")

elif selected == "📈 RFM Analysis":
    st.title("RFM Analysis")
    st.markdown("### RFM Analysis Overview")
    st.write("Here you can perform RFM analysis.")

elif selected == "🔮 Purchases Prediction":
    st.title("Purchases Prediction")
    st.markdown("### Purchases Prediction Overview")
    st.write("Here you can predict future purchases based on historical data.")

elif selected == "💼 Meet Our Team":
    st.title("Meet Our Team")
    st.write("Team members introduction.")
    st.image("https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/mohamed_image.png", caption="Mohamed Elgendy", width=100)  # رابط صورة محمد
