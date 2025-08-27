"""
Study Buddy Chatbot - A simple Telegram bot to help students with study techniques
and time management using spaCy NLP.
"""

import logging
import spacy
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
    print("spaCy model loaded successfully")
except OSError:
    print("Please download the spaCy model first: python -m spacy download en_core_web_sm")
    nlp = None

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Conversation states
MAIN_MENU = 1

class StudyBuddyBot:
    def __init__(self):
        self.study_data = {
            'pomodoro': "Pomodoro Technique: Study for 25 mins, break for 5 mins. Repeat 4x, then take a 15-30 min break.",
            'focus': "Focus Tips: Remove distractions, use website blockers, study in a quiet space, set clear goals.",
            'time_management': "Time Management: Use a planner, prioritize tasks, break big tasks into smaller ones, set deadlines.",
            'memorization': "Memorization: Use flashcards, spaced repetition, teach someone else, create associations.",
            'motivation': "Motivation: Set rewards, remember your goals, study with friends, take care of your health."
        }
        
        self.fallback_responses = [
            "I specialize in study tips! Try asking about time management or focus techniques.",
            "I'm here to help with studying. Want tips on Pomodoro or memorization?",
            "Study questions are my specialty! Ask me about time management or focus strategies.",
            "I can help with study techniques like Pomodoro, focus tips, or time management!"
        ]

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send welcome message and main menu"""
        welcome_text = """Hello! I'm your Study Buddy!

I can help you with:
• Pomodoro technique
• Focus strategies  
• Time management
• Memorization tips
• Motivation advice

What study help do you need today?"""

        keyboard = [
            ['Pomodoro', 'Focus Tips'],
            ['Time Management', 'Memorization'],
            ['Motivation', 'Random Tip']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

        await update.message.reply_text(welcome_text, reply_markup=reply_markup)
        return MAIN_MENU

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Process user messages with spaCy NLP"""
        if nlp is None:
            await update.message.reply_text("I'm experiencing technical difficulties. Please try again later.")
            return MAIN_MENU

        user_message = update.message.text.lower()
        
        if user_message in ['start over', 'restart', 'menu']:
            return await self.start(update, context)
            
        response = self.get_study_response(user_message)
        await update.message.reply_text(response)
        return MAIN_MENU

    def get_study_response(self, message):
        """Get appropriate response using spaCy NLP"""
        doc = nlp(message.lower())
        
        # Check for study-related topics using semantic similarity
        topic_similarities = {}
        
        for topic in self.study_data.keys():
            topic_doc = nlp(topic)
            similarity = doc.similarity(topic_doc)
            topic_similarities[topic] = similarity
        
        # Find the best matching topic
        best_topic = max(topic_similarities, key=topic_similarities.get)
        
        if topic_similarities[best_topic] > 0.3:  # Similarity threshold
            return self.study_data[best_topic]
        elif any(word in message for word in ['tip', 'advice', 'suggestion']):
            return random.choice(list(self.study_data.values()))
        else:
            return random.choice(self.fallback_responses)

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Cancel the conversation"""
        await update.message.reply_text("Happy studying! 📖 Remember to take breaks and stay hydrated!")
        return ConversationHandler.END

def main():
    """Main entry point for the Study Buddy Bot"""
    # Load Telegram token (replace with your actual token)
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
    
    if TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("Please replace TOKEN with your actual Telegram bot token")
        return
    
    # Create application
    application = Application.builder().token(TOKEN).build()
    bot = StudyBuddyBot()

    # Add conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', bot.start)],
        states={
            MAIN_MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message)
            ]
        },
        fallbacks=[CommandHandler('cancel', bot.cancel)]
    )

    application.add_handler(conv_handler)

    # Start the Bot
    print("Study Buddy Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
