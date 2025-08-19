# University Chatbot 🤖🎓  

A **Tkinter + ttkbootstrap** based chatbot with a modern graphical interface designed to assist students with university-related queries.  

This chatbot answers questions about **admissions, courses, fees, hostel, deadlines, and campus life**, using simple **intent matching** and **natural language similarity**. It simulates a real chat with chat bubbles, emojis, and an interactive UI.  

---

## ✨ Features  

- 🎨 **Modern Dark GUI** — Built with Tkinter and ttkbootstrap for a professional look.  
- 💬 **Interactive Chat Bubbles** — User and bot messages are displayed in styled bubbles with emojis.  
- 🧠 **Intent Recognition** — Uses `difflib.SequenceMatcher` to detect intent from user input.  
- 📚 **University FAQs** — Handles common queries like admissions, fees, hostel, courses, and campus life.  
- 🔄 **Context Handling** — Maintains conversational flow with follow-up questions.  
- 📝 **Conversation History** — Keeps track of past messages for better responses.  
- 🚀 **Easy to Extend** — Add new intents and responses without touching core logic.  

---

---

## 🛠️ Installation  

1. **Clone the Repository**  
```bash
git clone https://github.com/your-username/University-Chatbot.git
cd University-Chatbot


▶️ Usage

Run the chatbot using:
python chatbot.py

When the app starts, a welcome message will guide you:

👋 Hi! I'm your university assistant. You can ask me about:

✅ Admissions

📚 Courses

💸 Fees

🏨 Hostel

📆 Deadlines

💬 Example Queries

"How do I apply?" → Admission process

"What courses do you offer?" → Programs offered

"What are the hostel charges?" → Hostel fee details

"How much is the fee for Data Science?" → Program-specific tuition info

"Tell me about campus life" → Clubs, events, and student activities

🧩 How It Works

User Input — The chatbot reads user queries from the input box.

Intent Matching — The input is compared against predefined patterns using similarity scoring.

Response Generation — A suitable response is selected randomly from matched intent.

Context Tracking — Stores the last intent to handle follow-up questions like “what about hostel?”.

Chat Display — Messages are shown as colorful chat bubbles in the GUI.

🔧 Customization

You can add new intents in the intents list inside chatbot.py.
Each intent has this structure:
{
  "tag": "sports",
  "patterns": ["do you have sports?", "sports activities?", "cricket team?", "football?"],
  "responses": [
    "Yes! Our university has active cricket, football, and basketball teams.",
    "We offer multiple sports activities including cricket, football, and athletics."
  ]
}
➡️ Add your tag, patterns, and responses, then restart the chatbot.

🛡️ Limitations

❌ Not AI-powered — works on simple pattern matching, not NLP/ML.

❌ Cannot answer out-of-scope questions (e.g., “What’s 2+2?”).

❌ Data (like fees/deadlines) is hardcoded — must be updated manually.

🚀 Future Improvements

✅ Add database/backend for dynamic updates

✅ Integrate ML/NLP (e.g., spaCy or Hugging Face) for smarter understanding

✅ Deploy as a web chatbot with Flask/Django

✅ Add voice input/output for accessibility

👨‍💻 Author

Developed with ❤️ by Sufwan Amir

📧 Email: sufwanamir99@gmail.com
🌐 LinkedIn: www.linkedin.com/in/sufwan-amir-2a0a54363