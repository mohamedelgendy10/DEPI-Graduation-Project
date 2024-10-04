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
    logo_left_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/images%20(2).png"  # الشعار الأيسر
    st.image(logo_left_url, width=125)  # حجم الشعار 50 بيكسل

# إضافة الشعار في أقصى اليمين
with col2:
    logo_right_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/20231126120517!%D9%88%D8%B2%D8%A7%D8%B1%D8%A9_%D8%A7%D9%84%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA_%D9%88%D8%AA%D9%83%D9%86%D9%88%D9%84%D9%88%D8%AC%D9%8A%D8%A7_%D8%A7%D9%84%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA.png"  # الشعار الأيمن
    st.image(logo_right_url, width=125)  # حجم الشعار 50 بيكسل

# عرض المحتوى بناءً على القسم المختار
st.markdown("---")  # خط فاصل لتوضيح مكان المحتوى

# قسم Dataset Overview مع صورة افتتاحية
if selected == "Dataset Overview":
    st.title("Dataset Overview")

    # إضافة صورة افتتاحية
    intro_image_url = "https://path_to_your_intro_image.png"  # ضع رابط الصورة الافتتاحية هنا
    st.image(intro_image_url, caption="Welcome to the Dataset Overview Section", use_column_width=True)

    # إضافة المحتوى الخاص بالقسم
    st.markdown("### Overview of the Dataset")
    st.markdown("""
    This section provides detailed information about the dataset used in this project.
    You will see the structure of the data, the variables, and their basic statistics.
    """)

    # تحميل البيانات
    uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                data = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                data = pd.read_excel(uploaded_file)

            st.success("Dataset loaded successfully!")

            # عرض هيكل البيانات
            st.markdown("### Data Shape")
            st.write(f"Number of rows: {data.shape[0]}")
            st.write(f"Number of columns: {data.shape[1]}")

            # عرض الإحصاءات الوصفية
            st.markdown("### Descriptive Statistics")
            st.write(data.describe())

            # عرض الأعمدة
            st.markdown("### Column Names and Types")
            st.write(data.dtypes)

            # معاينة البيانات (أول 5 صفوف)
            st.markdown("### Data Preview (First 5 Rows)")
            st.write(data.head())
        
        except Exception as e:
            st.error(f"Error loading dataset: {e}")
    else:
        st.info("Please upload a dataset to start the overview.")
