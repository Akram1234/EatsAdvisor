import streamlit as st

# Configuration of the page with title and emoji icon
st.set_page_config(
    page_title="EatsAdvisor - Personalized Diet Recommendations",
    page_icon="🍏",
)

# Title of the welcome page
st.title('Welcome to EatsAdvisor! 🍏')

# Sidebar with a simple call-to-action
st.sidebar.success("Explore personalized diet recommendations.")

# Placeholder for user interaction
st.write("### Start your health journey with EatsAdvisor today!")
# The 'Get Started' button is hypothetical, and you might want to implement functionality for what happens when a user clicks it.
get_started = st.button('Get Started')

if get_started:
    st.markdown(
        """
        Click the link to proceed to the diet recommendation page:
        [Go to Diet Recommendation](http://localhost:8501/Diet_Recommendation)
        """,
        unsafe_allow_html=True
    )

# Introduction section in the main page content
st.markdown("""
    ## Tailored Nutritional Guidance at Your Fingertips
    
    In the digital age, health consciousness is more than a trend—it's a lifestyle. EatsAdvisor is at the forefront, offering **personalized nutritional insights** and **diet recommendations** tailored just for you.

    Whether you're planning your meals or looking for a nutritional analysis, EatsAdvisor harnesses the power of data to curate meal plans and suggest recipes that align with your personal health goals.

    ### Discover What EatsAdvisor Offers:
    - **Personalized Nutritional Projections**: Get meal plans customized for your age, height, weight, gender, and daily meal frequency.
    - **Nutritional Analysis & Recipe Suggestions**: Find recipes based on specific nutritional needs, complete with detailed breakdowns.
    
    Dive into a seamless experience of healthy eating, backed by a comprehensive dataset from Kaggle that includes over half a million recipes!
""", unsafe_allow_html=True)



# Dataset information section
st.markdown("""
    ---
    ## Comprehensive Dataset
    Our application is powered by an extensive dataset that features:
    - **522,517 recipes**
    - **312 categories**
    - **28 insightful columns** ranging from RecipeId to detailed nutritional content.
""")

# Objective section
st.markdown("""
    ---
    ## Our Objective
    EatsAdvisor is committed to delivering:
    - **Personalized Nutritional Projections**: Tailored meal plans for your unique dietary needs.
    - **Nutritional Analysis & Recipe Suggestions**: Custom recipe recommendations based on your nutritional preferences.
""")

# Technological Approach section
st.markdown("""
    ---
    ## Technological Edge
    EatsAdvisor leverages cutting-edge technology:
    - **Nearest Neighbors Algorithm**: For an efficient, content-based recommendation engine.
    - **FastAPI**: Crafting a robust and responsive backend.
    - **Streamlit**: Delivering an engaging and intuitive frontend experience.
""")

# Deployment Strategy section
st.markdown("""
    ---
    ## Deployment Strategy
    We employ sophisticated tools to bring you a seamless application experience:
    - **Docker Containerization**: For consistency across various platforms.
    - **Scalability and Efficient Management**: To ensure that our app meets your needs at every turn.
    - **Service Integration with Docker-compose**: For a harmonious operation of our multi-component application.
""")

# Footer with call to action for visiting the GitHub repository
st.markdown("""
    ---
    ## Contribute or Learn More
    Interested in the technicalities or want to contribute? Check out the EatsAdvisor project on [GitHub](https://github.com/Akram1234/EatsAdvisor).
""")

