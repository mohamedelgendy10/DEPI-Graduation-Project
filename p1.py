import streamlit as st
from streamlit_option_menu import option_menu

# شريط جانبي للتنقل مع الأيقونات
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # عنوان القائمة
        options=["Dataset Overview", "Data Preparation", "RFM Analysis", "Meet Our Team", "Predictions"],  # الأقسام
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

    st.markdown("## Job title has 195 value:")
    st.markdown("""
    Solution: Used function to categorize all values into 10 categories
 
    """)
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E10.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    st.markdown("## Missing Customer IDs in the Main Table:")
    st.markdown("""
    Issue: Some customer IDs were present in the address table but had no matching records in the main customer table.

    Solution: Removed these entries from the address table to ensure that all customer IDs have corresponding records in the main table

    """)

    st.markdown("## Handling Missing Values:")
    st.markdown("""
    Customers Table:

    Missing Last Names: Several customer records had empty values in the last_name column, resulting in incomplete names.

    Solution: Combined the first_name and last_name columns into a new full_name column to fill in the gaps.

    Missing Job Titles, Industry Categories, and Tenure: Some records had missing values, leading to incomplete data.

    Solution: Replaced missing entries in the job_title and job_industry_category columns with 'N/A' and set missing tenure values to 0 to indicate that the data was unavailable.

    """)
    
    st.markdown("## Transactions Table:")
    st.markdown("""
    Several columns, such as brand, product_line, product_class, and product_size, had missing values, causing incomplete records.
    Solution:
    Filled Missing Categorical Values: Used .fillna('N/A') to replace all missing values in these columns for consistency.
    Filled Missing Numerical Values: Used KNN Imputer to estimate missing values in online_order, standard_cost, and product_first_sold_date by finding the 3 closest matches from the data.
    
    """)
    
    st.markdown("## Data Merging:")
    st.markdown("""
    Problem: There were two separate tables:
    Old Customers Table: Contained customer records with assigned IDs.
    New Customers Table: Included new customer records without IDs.
    This separation made it challenging to have a unified dataset for complete analysis.
    
    Solution:
    Assign IDs to New Customers: Created unique IDs for new customers starting from 4001 to avoid conflicts with existing IDs.
    
    Merge Customer Information: Combined the old and new customer tables based on shared columns such as name, gender, and date of birth.
    
    Merge Address Data: Unified address details like address, postcode, state, country, and property valuation for both old and new customers.
    
    """)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E11.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E12.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E13.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E14.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)




elif selected == "RFM Analysis":

    st.markdown("## RFM Analysis Overview")
    st.markdown("""
    RFM analysis is a method used to assess and categorize customers based on their purchasing behavior.
    
    RFM Components:
    
    Recency (R): Measures how long it has been since a customer last made a purchase. Customers who have bought more recently are more likely to make repeat purchases.
    
    Frequency (F): Represents how often a customer makes purchases. Customers who buy more frequently are typically more engaged and loyal.
    
    Monetary Value (M): Indicates the total amount a customer has spent over a specific period. Customers who spend more are generally viewed as more valuable.

    """)
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E15.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    st.markdown("## Benefits of RFM Analysis:")
    st.markdown("""
    Customer Segmentation: Helps identify and group customers based on their purchase behavior, enabling targeted marketing strategies.
    Personalized Marketing: Allows businesses to tailor campaigns and offers based on each segment’s buying habits.
    Customer Retention: Helps focus on high-value and recently active customers, improving retention rates and customer loyalty.
    Optimized Resource Allocation: Guides businesses in allocating resources effectively by prioritizing high-potential customers.
    Increased ROI: By targeting the right customers, RFM analysis can lead to better marketing results and higher returns on investment.
    Improved Customer Understanding: Provides deep insights into customer preferences, allowing businesses to enhance the overall customer experience.

    """)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E16.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E17.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    st.markdown("## Customer Segmentation:")
    st.markdown("""
    Customers can be classified into segments such as Champions, Loyal Customers, or At Risk, each requiring distinct strategies. The current segmentation prioritizes Recency and Frequency for the following reasons:
    
    Simplified Analysis: By summation the three rank values
    
    Behavior vs. Revenue: Although Monetary value is significant for measuring a customer’s financial impact, categories like Champions and Loyal Customers are defined more by their purchasing behavior—how often and how recently they buy—making these metrics ideal for strategies aimed at customer engagement.

    """)
    
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E18.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E19.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E20.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E21.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E22.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E23.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E24.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E25.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E26.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E27.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E28.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)



elif selected == "Predictions":
    
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E29.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E30.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)
    
    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E31.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E32.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E33.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E34.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)

    intro_image_url = "https://raw.githubusercontent.com/mohamedelgendy10/DEPI-Graduation-Project/main/E35.jpg"  # الرابط المباشر للصورة الافتتاحية
    st.image(intro_image_url, caption="", use_column_width=True)
    
elif selected == "Meet Our Team":
    st.title("Meet Our Team")
    
    # تنظيم الفريق في صفين
    st.write("---")
    col1, col2 = st.columns([1, 1])

    # العضو الأول - Mohamed Elgendy
    with col1:
        st.markdown("### Mohamed Elgendy")
        st.markdown("****")
        linkedin_icon_mohamed = """
            <a href="https://www.linkedin.com/in/mohamed-rezk-elgendy" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        """
        st.markdown(linkedin_icon_mohamed, unsafe_allow_html=True)

    # العضو الثاني - Member 2
    with col2:
        st.markdown("###Ahmed Elsayed Mohamed ")
        st.markdown("****")
        linkedin_icon_member2 = """
            <a href="https://www.linkedin.com/inahmed-elsayed-406366218?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Bx%2FiMBw" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        """
        st.markdown(linkedin_icon_member2, unsafe_allow_html=True)

    st.write("---")

    col3, col4 = st.columns([1, 1])

    # العضو الثالث - Member 3
    with col3:
        st.markdown("###Abdelerahman Mohamed faried")
        st.markdown("**r**")
        linkedin_icon_member3 = """
            <a href="https://www.linkedin.com/in/abdelrahman-mohamed-7750532a6" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        """
        st.markdown(linkedin_icon_member3, unsafe_allow_html=True)

    # العضو الرابع - Member 4
    with col4:
        st.markdown("###Mennatullah Muhammad Mahmoud ")
        st.markdown("****")
        linkedin_icon_member4 = """
            <a href="https://www.linkedin.com/in/mennatullah-muhammad-b15826232/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        """
        st.markdown(linkedin_icon_member4, unsafe_allow_html=True)
