import streamlit as st
from streamlit_option_menu import option_menu

# شريط جانبي للتنقل مع الأيقونات
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # عنوان القائمة
        options=["Dataset Overview", "Data Preparation", "Purchases Prediction", "Meet Our Team"],  # الأقسام
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
    
    # إضافة صورة افتتاحية
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E0.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    # إضافة العنوان والنص
    st.markdown("## Dataset Overview")
    st.markdown("""
    The dataset consists of four sheets, each providing key insights into different aspects of customer information:

    - **Customer Demographic**: Contains details about customers' age, gender, and other demographic attributes.

    - **New Customer List**: Includes information on newly acquired customers.

    - **Customer Address**: Stores address details such as state, postcode, and country.

    - **Transactions**: Records all transaction details, including product purchases and sales data.
    """)
    
    st.markdown("## Customers Sheets")
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E2.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    
    st.markdown("## Customers Address Sheet")
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E3.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    st.markdown("## Transactions Sheet")
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E4.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    st.markdown("## ERD Diagram")
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E6.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

elif selected == "Data Preparation":
    st.markdown("## EData Cleaning Process :")
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E7.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    st.markdown("## Handling missing values:")
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E8.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    st.markdown("## Handling Invalid Age Entries:")
    st.markdown("""
    Issue: Some age values, such as 174, were clearly unrealistic, suggesting data entry errors or anomalies.

    Solution: Removed the rows with these erroneous values to maintain the integrity of the dataset.

    """)

   
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E9.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    st.markdown("## State Abbreviations Inconsistency:")
    st.markdown("""
    Issue: The state column included a mix of full state names and abbreviations, such as 'NSW' and 'New South Wales’.

    Solution: Replaced all abbreviations with the corresponding full state names to ensure uniformity.
    
    """)

    

elif selected == "Purchases Prediction":



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
