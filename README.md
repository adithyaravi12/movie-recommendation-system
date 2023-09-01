
# Netflix dataset EDA and building a Movie/TV series recommendation system using streamlit

## Roadmap:
- **Exploratory Data Analysis (EDA) -** During the initial stages of my project, I delved into Exploratory Data Analysis (EDA) to make sense of the dataset I had downloaded. This involved digging into the data, cleaning it up, and visualizing it to gain insights into its structure and characteristics. I removed any features that didn't seem relevant, aiming to streamline the dataset for further analysis.
- **Approach -** When it came to building a recommendation system, I looked up on google and came across content based filtering system and collaborative filtering system. I decided to take a content-based filtering approach. I figured that utilizing the descriptions of movies and TV series would be a easiest way to make recommendations. I employed cosine similarity, a technique that calculates the cosine of the angle between vectors representing the descriptions. This helped me measure the similarity between different titles based on their content, giving me a foundation for the recommendation engine.
- **Initial Attempt with Flask: -**  I initially tried to implement the recommendation system using Flask, a Python web framework that combines the python backend with html, css and javascript frontend. While Flask offered great flexibility, I realized that it demanded a deeper understanding of backend development, which I am still learning. The complexity was a bit overwhelming for my current skill level and was hitting on multiple errors and "Error 404" while trying to launch the app, so I felt that I needed a simpler solution.
- **Transition to Streamlit -** Streamlit proved to be incredibly user-friendly and intuitive, allowing me to focus more on the frontend and user experience rather than getting bogged down in backend intricacies. I quickly set up text input boxes and buttons for users to interact with and display the recommendations seamlessly.




## Prerequisites 

- **Install streamlit:** Since the app works on the base of streamlit, this package is necessary to execute the program
```bash
    pip install streamlit
```


## Installation

To run this project on local machine follow these steps

- Clone or download the repository as zip file and extracrt it.
- Install necessary dependancies
- Download the dataset in the same destination where the files has been extracted.
- Open a terminal, navigate to the project directory containing your script, and run the Streamlit app.

```bash
  streamlit run app.py
```
    
## Resource
- [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)


## Demo

Insert gif or link to demo


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Reference
- [Introduction To Recommender Systems- 1: Content-Based Filtering And Collaborative Filtering](https://towardsdatascience.com/introduction-to-recommender-systems-1-971bd274f421)
- [Build A Machine Learning Web App From Scratch](https://www.youtube.com/watch?v=xl0N7tHiwlw)
- [Streamlit Documentation](https://docs.streamlit.io/library/get-started)
- [Custom Streamlit Background Image/Color Gradient through CSS](https://www.youtube.com/watch?v=pyWqw5yCNdo)
- [How to Hide Menu & Customize The Footer in Streamlit Apps](https://www.youtube.com/watch?v=MeOjN5tb51U)
## Feedback

I greatly value feedback as an essential tool for my growth. If you have any feedback to share, please share it at adithyaravi0312@gmail.com. Your insights are immensely appreciated and contribute to my continuous improvement.








## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/adithyaravi12)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adithyaravi12/)


