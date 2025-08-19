import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import random
from difflib import SequenceMatcher


conversation_history = []

context = {"last_intent": None, "follow_up": None}

intents = [
    {"tag": "greeting", "patterns": ["hi", "hello", "hey", "salam", "assalamualaikum", "good morning", "good afternoon"],
     "responses": ["Hello! How can I assist you today?", "Hi there! Need help with anything specific?", "Hey! Ask me anything about the university."]},

    {"tag": "farewell", "patterns": ["bye", "goodbye", "see you", "take care"],
     "responses": ["Goodbye! Take care.", "See you soon! Reach out if you have more questions.", "Bye for now! 😊"]},

    {"tag": "thanks", "patterns": ["thanks", "thank you", "appreciate it", "grateful", "many thanks"],
     "responses": ["You're welcome! 😊", "Glad I could help!", "Anytime! Feel free to ask more."]},

    {"tag": "what_can_you_do", "patterns": ["what can you do", "what do you know", "how can you help me", "what are you capable of"],
     "responses": ["I can help you with information about admissions, courses, hostel, fees, events, and much more at the university.", "I'm here to answer questions about university life — academics, scholarships, deadlines, and more. Just ask!"]},

    {"tag": "small_talk", "patterns": ["how are you", "what's up", "how's it going", "how are you doing"],
     "responses": ["I'm just a bot, but I'm doing great! Thanks for asking 😊", "All systems operational. Ready to help you!", "Feeling chatty today! What do you want to talk about?"]},

    {"tag": "follow_up", "patterns": ["can you tell me more", "what else", "anything else", "please explain more"],
     "responses": ["Sure! Just ask me something specific like 'tell me about the hostel' or 'what courses do you offer?'"]},

    {"tag": "random_talk", "patterns": ["tell me something interesting", "say something", "bored", "i want to talk"],
     "responses": ["Did you know that our university hosts an annual tech fest with coding, robotics, and gaming contests? 🤖"]},

    {"tag": "admissions", "patterns": ["how to apply", "admission process", "how do i get in", "can i still apply", "how do I start my application", "how do i apply", "how do i register", "registration process"],
     "responses": ["You can apply online through our university portal. The process is very simple!", "Start by creating an account on our admission portal and following the steps there."]},

    {"tag": "deadline", "patterns": ["admission deadline", "last date to apply", "deadline to apply", "when is the deadline", "application last date", "form submission date", "can I apply after deadline", "late admission"],
     "responses": ["The admission deadline is June 30th.", "Applications must be submitted before the end of June."]},

    {"tag": "documents", "patterns": ["what documents are required", "documents needed", "which documents to submit", "documents for admission"],
     "responses": ["You'll need scanned copies of your CNIC/B-form, academic transcripts, and recent photo."]},

    {"tag": "confirmation", "patterns": ["how will i know i got admitted", "confirmation email", "when will i get confirmation", "admission confirmed or not"],
     "responses": ["You'll receive an official confirmation via email and SMS if you're selected."]},

    {"tag": "merit_list", "patterns": ["merit list", "when is merit list", "will there be a merit list", "list of selected students"],
     "responses": ["Merit lists are usually announced a week after the deadline."]},

    {"tag": "courses", "patterns": ["courses offered", "programs available", "do you offer data science", "what degrees", "what programs do you have", "tell me about courses", "what subjects are offered", "do you offer software engineering", "can i study ai", "which departments do you have", "list your degrees", "what can i study there", "study options"],
     "responses": ["We offer BS in Data Science, Computer Science, Software Engineering, and Artificial Intelligence.", "Our programs include BSCS, BSDS, BSSE, and BSAI. Check our website for details."]},

    {"tag": "campus_life", "patterns": ["campus life", "what's student life like", "do you have clubs", "fun activities", "societies", "events on campus"],
     "responses": ["Student life here is vibrant — we have technical societies, sports, dramatics, and more!"]},

    {"tag": "fees", "patterns": ["how much is the fee", "tuition fee", "fee structure", "semester fees", "total fees", "what is the cost", "cost of program", "how much do I need to pay", "what are the charges", "what's the admission fee", "how much for cs", "how much for ai","how much for data science","what about hostel fee", "is hostel fee included", "fee with hostel"],
     "responses": ["The tuition fee for most programs is around PKR 120,000 per semester.", "You’ll need around 120k per semester. Admission and registration charges may apply separately.","You’ll need around 120k per semester. Admission and registration charges may apply separately.", "Hostel fee is separate and depends on room type. It ranges from PKR 30,000 to 50,000 per semester."]},
    {
    "tag": "hostel",
    "patterns": [
        "do you offer hostel?",
        "is hostel available?",
        "what are the hostel charges?",
        "tell me about hostel",
        "how much is the hostel fee?",
        "accommodation options?",
        "what's the cost of staying in hostel?",
        "does the university provide hostel?",
        "hostel facility?",
        "is hostel included in the fee?",
        "can I get a hostel seat?",
        "how to apply for hostel?",
        "hostel application process"
    ],
    "responses": [
        "Yes, hostel facilities are available for both boys and girls on campus.",
        "Hostel charges range from PKR 30,000 to 50,000 per semester depending on the room type.",
        "You can apply for hostel after confirming your admission — seats are limited.",
        "Accommodation includes shared rooms with basic facilities and mess services.",
        "The hostel fee is separate from tuition and must be paid at the start of each semester."
    ]
}

]

# --- Similarity ---
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_response(user_input):
    user_input = user_input.lower()
    msg_entry = {"user": user_input}

    
    if any(word in user_input for word in ["fee", "fees", "cost", "charges", "payment", "price"]):
        context["last_intent"] = "fees"
        context["follow_up"] = "fees_detail"

        # Specific program fees
        if any(dept in user_input for dept in ["ai", "artificial intelligence"]):
            reply = "The fee for the AI program is around PKR 120,000 per semester. Hostel charges are extra."
        elif any(dept in user_input for dept in ["cs", "computer science"]):
            reply = "Computer Science tuition is around PKR 120,000 per semester. Hostel fee is not included."
        elif any(dept in user_input for dept in ["data science", "ds"]):
            reply = "Data Science costs approximately PKR 120,000 per semester, excluding hostel."
        elif any(dept in user_input for dept in ["software engineering", "se"]):
            reply = "Software Engineering also has a tuition of around PKR 120,000 per semester."

        # Hostel fee
        elif "hostel" in user_input or "accommodation" in user_input:
            reply = "Hostel charges range from PKR 30,000 to 50,000 depending on room type."

        # Breakdown
        elif any(x in user_input for x in ["breakdown", "structure", "details", "semester"]):
            reply = "Each semester includes tuition (~PKR 120,000), registration (~PKR 5,000), and misc. charges."

        # Total or everything
        elif any(x in user_input for x in ["total", "all", "everything", "complete"]):
            reply = "Total for one semester is around PKR 120,000 + optional hostel fee + other charges."

        # Ambiguous fee query
        else:
            reply = "The tuition fee is about PKR 120,000 per semester. Do you want program-specific or hostel fee too?"

        msg_entry["intent"] = "fees"
        msg_entry["bot"] = reply
        conversation_history.append(msg_entry)
        return reply

    # Follow-ups
    if context.get("follow_up") == "fees_detail":
        context["follow_up"] = None  # reset after handling
        if "hostel" in user_input:
            reply = "Hostel charges range from PKR 30,000 to 50,000 depending on room type."
        elif "semester" in user_input or "breakdown" in user_input or "structure" in user_input:
            reply = "Each semester includes tuition (~PKR 120,000), registration (~PKR 5,000), and misc. charges."
        elif any(dept in user_input for dept in ["ai", "cs", "computer science", "data science", "software engineering"]):
            reply = "All BS programs including CS, DS, SE, and AI have similar tuition — around PKR 120,000 per semester."
        else:
            reply = "Could you specify if you want semester-wise fees, hostel fees, or for a specific program?"
        msg_entry["intent"] = "fees"
        msg_entry["bot"] = reply
        conversation_history.append(msg_entry)
        return reply

    # Yes/no follow-up
    if user_input in ["yes", "yeah", "sure", "okay"] and context["last_intent"]:
        if context["last_intent"] == "fees":
            reply = "Would you like a semester-wise breakdown, hostel info, or something else?"
            context["follow_up"] = "fees_detail"
        elif context["last_intent"] == "courses":
            reply = "We have CS, DS, SE, and AI — which one interests you?"
        elif context["last_intent"] == "admissions":
            reply = "Visit our admission portal to begin. Need the link?"
        else:
            reply = "Alright!"
        msg_entry["intent"] = context["last_intent"]
        msg_entry["bot"] = reply
        conversation_history.append(msg_entry)
        return reply

    # Pattern-based intent match 
    best_score = 0
    best_match = None
    for intent in intents:
        for pattern in intent["patterns"]:
            score = similarity(pattern, user_input)
            if score > best_score and score > 0.6:
                best_score = score
                best_match = intent

    if best_match:
        context["last_intent"] = best_match["tag"]
        context["follow_up"] = None
        bot_reply = random.choice(best_match["responses"])
        msg_entry["intent"] = best_match["tag"]
        msg_entry["bot"] = bot_reply
        conversation_history.append(msg_entry)
        return bot_reply

    # History-based fallback
    for msg in reversed(conversation_history):
        if user_input in ["what about that?", "does that include hostel?", "and the rest?"] and "intent" in msg:
            if msg["intent"] == "fees":
                reply = "Yes, hostel charges are not included in tuition."
            elif msg["intent"] == "courses":
                reply = "All programs follow a semester system with core and elective courses."
            else:
                reply = "Let me clarify that."
            msg_entry["intent"] = msg.get("intent", None)
            msg_entry["bot"] = reply
            conversation_history.append(msg_entry)
            return reply

    fallback = "I'm not sure how to answer that. Try asking about admissions, fees, or courses."
    msg_entry["bot"] = fallback
    conversation_history.append(msg_entry)
    return fallback

# --- GUI Setup ---
root = tk.Tk()
root.title("University Chatbot 🤖")
root.geometry("600x500")
style = Style(theme="darkly")

header = ttk.Label(root, text="🎓 University Chatbot", font=("Segoe UI", 20, "bold"))
header.pack(pady=10)

frame = ttk.Frame(root)
frame.pack(fill="both", expand=True, padx=10)

chat_canvas = tk.Canvas(frame, bg="#1e1e1e", highlightthickness=0)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=chat_canvas.yview)
chat_frame = ttk.Frame(chat_canvas)
chat_frame.bind("<Configure>", lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all")))
chat_canvas.create_window((0, 0), window=chat_frame, anchor="nw")
chat_canvas.configure(yscrollcommand=scrollbar.set)
chat_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# --- Chat bubbles ---
def insert_bubble(canvas, text, sender):
    bubble = tk.Frame(chat_frame, bg="#1e1e1e", padx=5, pady=5)
    color = "#fbb1d4" if sender == "user" else "#add8e6"
    anchor = "e" if sender == "user" else "w"
    emoji = "👩‍🎓" if sender == "user" else "🤖"
    justify = "right" if sender == "user" else "left"
    label = tk.Label(bubble, text=f"{emoji} {text}", bg=color, fg="black", font=("Segoe UI", 11), wraplength=380, justify=justify, padx=10, pady=5)
    label.pack()
    bubble.pack(anchor=anchor, pady=5, padx=10)
    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

# --- Message sender ---
def send_message(event=None):
    user_input = entry_var.get().strip()
    if not user_input:
        return
    insert_bubble(chat_canvas, user_input, "user")
    entry_var.set("")
    bot_reply = get_response(user_input)
    root.after(500, lambda: insert_bubble(chat_canvas, bot_reply, "bot"))

# --- Input box ---
bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill="x", pady=10, padx=10)

entry_var = tk.StringVar()
entry_box = ttk.Entry(bottom_frame, textvariable=entry_var, font=("Segoe UI", 11))
entry_box.pack(side="left", fill="x", expand=True, padx=(0, 10))
entry_box.bind("<Return>", send_message)

send_btn = ttk.Button(bottom_frame, text="Send", command=send_message)
send_btn.pack(side="right")

# --- Welcome Message ---
welcome_text = (
    "👋 Hi! I'm your university assistant. You can ask me about:\n\n"
    "✅ Admissions\n📚 Courses\n💸 Fees\n🏨 Hostel\n📆 Deadlines\n\n"
    "💬 Try: 'how do I apply?' or 'what courses do you offer?'"
)
root.after(500, lambda: insert_bubble(chat_canvas, welcome_text, "bot"))

# --- Mainloop ---
root.mainloop()



