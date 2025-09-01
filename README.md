# IEMT302-s227542541 (I have combined the requirements.txt, .gitignore and README.md of different tasks)

# Telegram Chatbot (study_bot.py)
Problem Statement=
Students often struggle with effective study techniques, time management, and maintaining motivation. This chatbot provides:
1. Quick access to study techniques like Pomodoro method
2. Time management strategies for better productivity
3. Memorization tips for improved learning
4. Motivational advice to maintain focus
5. 24/7 availability for study support

How to Verify It Works=
1. Create Virtual Environment
2. Install Dependencies
3. Set Up Telegram Bot
4. Run the Bot

Testing the Bot
1. Basic Functionality Test
  •	Send /start → Should show welcome message with menu
  •	Click menu buttons → Should return appropriate study tips
  •	Type "pomodoro" → Should explain Pomodoro technique
  •	Type "time management" → Should give time management advice

2. NLP Testing
Test these phrases (spaCy should understand the similarity):
  •	"How to focus better?" → Focus tips
  •	"I need help memorizing" → Memorization tips
  •	"Study timing method" → Pomodoro technique
  •	"Getting motivated" → Motivation advice

3. Unexpected Input Testing
  •	"What's the weather?" → Fallback response
  •	"Tell me a joke" → Fallback response
  •	"Hello" → Fallback response
  •	Random words → Fallback response

4. Restart Functionality
  •	Type "start over" or "menu" → Should restart conversation

Limitations=
1. Basic NLP Understanding
  •	Uses simple semantic similarity matching
  •	Limited context awareness
  •	May misunderstand complex or ambiguous questions

2. Fixed Knowledge Base
  •	Only contains pre-programmed study techniques
  •	Cannot learn new information or adapt to individual needs
  •	No personalized advice based on user history

3. No Session Memory
  •	Doesn't remember previous conversations
  •	Each message is processed independently
  •	No continuity in multi-step queries

4. Unexpected Input Handling
When the bot encounters something unexpected:
  •	Provides friendly fallback responses redirecting to study topics
  •	Uses a list of pre-defined generic responses
  •	Never pretends to understand something it doesn't
  •	Always maintains focus on study-related assistance

5. Limited Depth
  •	Provides overviews, not detailed guides
  •	No step-by-step instructions or follow-up questions
  •	Basic explanations only

# Second Repo Experiment ()

# Machine Learning (Machine_learning.py)
This repository demonstrates the most basic form of machine learning: linear regression. It uses Python and scikit-learn to learn a relationship between input and output data.

What Is Linear Regression?
Linear regression is a supervised learning algorithm that models the relationship between a dependent variable (y) and one or more independent variables (X) using a straight line.

In this example, we use a perfect linear relationship:  
**y = 2x**

What the Code Does=

1. **Creates training data**:  
   - Inputs: `X = [[1], [2], [3], [4], [5]]`  
   - Targets: `y = [2, 4, 6, 8, 10]`

2. **Trains a model**:  
   - We use `LinearRegression()` from scikit-learn to learn the mapping from X to y.

3. **Makes predictions**:  
   - Predicts the output for new inputs: `X_test = [[6], [7]]`

4. **Visualizes the result**:  
   - Plots training data, model predictions, and test predictions using matplotlib.

How to Run It=
1. Clone the repo
2. Set up a virtual enviroment
3. Install dependencies
4. Run the script

You'll see a plot showing the training data, the regression line and predictions for new inputs.
