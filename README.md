
# EatsAdvisor
In the forthcoming digital age landscape, a growing emphasis is predicted on health consciousness and the demand for personalized online nutritional resources. The proposed EatsAdvisorproject aims to cater to this anticipated demand by conceptualizing a web application offering personalized nutritional insights based on user-specific inputs.


## Dataset
The dataset proposed for integration is available on Kaggle. It contains 522,517 recipes spanning 312 categories, with 28 columns, providing a comprehensive data backbone for the envisioned application.
- **Columns**: RecipeId, Name, CookTime, PrepTime, TotalTime,RecipeIngredientParts, Calories, FatContent,SaturatedFatContent, CholesterolContent, SodiumContent,CarbohydrateContent, FiberContent, SugarContent, ProteinContent,RecipeInstructions.

## Objective

The proposal outlines the development of a dual-faceted web application:
- **Personalized Nutritional Projections:** With inputs like Age, Height, Weight, Gender, and Meals per day, the application will endeavor to generate curated meal plans for breakfast, lunch, and dinner.
- **Nutritional Analysis & Recipe Suggestions:** By allowing users to input specific nutritional elements such as calories, fat content, and protein, the application will aim to generate a list of suitable recipes, complete with an in-depth nutritional breakdown.

## Technological Approach:
- **Machine Learning Model**: The recommendation engine for EatsAdvisor will be conceptualized using the Nearest Neighbors algorithm. This unsupervised learning model will target efficient neighbor searches to align with user requirements.
- **Backend Development**: The backend foundation will be envisaged using FastAPI, a modern Python-based web framework renowned for its quick processing and operational efficacy.
- **Frontend Framework**: For creating a user-centric interface, the application will be designed using Streamlit, an open-source app framework in Python. Given Streamlit's compatibility with a myriad of Python libraries, it is deemed suitable for this data-driven project.

## Deployment Strategy

- **Application Containerization:** The proposal envisions using Docker to ensure a standardized application experience across diverse environments. Owing to the anticipatedmulti-faceted nature of the project, incorporating a multi-container strategy will be imperative.
- **Scalability and Management:** Docker's inherent scalability and efficient management capabilities will be harnessed to handle the complexities of this ambitious project.
- **Service Integration with Docker-compose:** Docker-compose is proposed to ensure seamless integration and coordination among the diverse project components, all defined within a structured YAML file.

