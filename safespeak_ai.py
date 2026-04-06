import streamlit as st

st.write("SafeSpeak 🚀 Stay Safe Speak Safe🕊️")

# ------------------------------
# Scam Detection
# ------------------------------
st.warning("⚠️ Never share OTP, PIN, or passwords with anyone.")

def detect_scam(message):
    scam_keywords = [
        "otp", "pin", "password", "bank", "account",
        "urgent", "immediately", "verify", "suspend",
        "click", "link", "login", "confirm", "digit",
        "free", "winner", "prize", "gift", "number",
        "send money", "transfer", "bkash", "nagad",
        "টাকা","ওটিপি","জরুরি","पैसा","ओटीपी","तुरंत","otp দিন", "bkash send korun", "nagad send korun",
        "account bondho", "verify korun", "taka pathan",
        "joldi korun", "offer paisen", "lottery paisen"
    ]

    threat_keywords = [
        "kill", "hack", "block", "delete", "threat",
        "or else", "last warning", "final notice"
    ]

    message_lower = message.lower()
    found = [word for word in scam_keywords + threat_keywords if word in message_lower]

    return len(found) > 0, found


# ------------------------------
# 🔥 Explanation Dictionary (NEW)
# ------------------------------
explanation_dict = {
    "otp": "Scammers use OTPs to gain access to your accounts.",
    "pin": "PIN codes can give full control of your account.",
    "password": "Sharing passwords leads to account hacking.",
    "bank": "Scammers pretend to be banks to gain trust.",
    "urgent": "Creates panic so you act without thinking.",
    "immediately": "Pushes you to act fast without verifying.",
    "verify": "Often used in fake verification scams.",
    "click": "May lead to phishing websites.",
    "link": "Links can contain malware or fake pages.",
    "login": "Fake login pages steal credentials.",
    "free": "Too-good-to-be-true offers are usually scams.",
    "winner": "Fake prize scams are very common.",
    "send money": "Direct financial fraud attempt.",
    "bkash": "Common in local mobile banking scams.",
    "nagad": "Used in Bangladesh-based scams.",
    "kill": "Threat language used to scare victims.",
    "hack": "Used to create fear and force action.",
    "or else": "Classic manipulation tactic.",
    "final notice": "Fake urgency to pressure users.",
    "টাকা": "money scam",
    "ওটিপি": "OTP scam",
    "জরুরি": "urgent scam",
    "पैसा": "money scam",
    "ओटीपी": "OTP scam",
    "तुरंत": "urgent scam",
}

# ------------------------------
# 🌐 Text Dictionary
# ------------------------------
text = {
    "English": {
        "title": "🛡️ SafeSpeak AI",
        "subtitle": "Detect scams & understand digital language",
        "scam_header": "🔍 Scam Detector",
        "input_msg": "Enter message:",
        "analyze": "Analyze Message",
        "safe": "✅ Message seems safe",
        "danger": "⚠️ Potential Scam Detected!",
        "risk": "📊 Risk Score",
        "grandma": "👵 Grandma Mode",
        "translate_input": "Enter slang / emoji message:",
        "translate_btn": "Explain Message",
        "no_slang": "No slang detected"
    },

    "বাংলা": {
        "title": "🛡️ SafeSpeak AI",
        "subtitle": "প্রতারণা শনাক্ত করুন এবং আধুনিক ভাষা বুঝুন",
        "scam_header": "🔍 প্রতারণা শনাক্তকরণ",
        "input_msg": "মেসেজ লিখুন:",
        "analyze": "বিশ্লেষণ করুন",
        "safe": "✅ মেসেজটি নিরাপদ মনে হচ্ছে",
        "danger": "⚠️ সম্ভাব্য প্রতারণা!",
        "risk": "📊 ঝুঁকি স্কোর",
        "grandma": "👵 সহজ ভাষা",
        "translate_input": "স্ল্যাং / ইমোজি লিখুন:",
        "translate_btn": "ব্যাখ্যা করুন",
        "no_slang": "কোন স্ল্যাং পাওয়া যায়নি"
    },

    "हिन्दी": {
        "title": "🛡️ SafeSpeak AI",
        "subtitle": "घोटालों का पता लगाएं और डिजिटल भाषा समझें",
        "scam_header": "🔍 स्कैम डिटेक्टर ",
        "input_msg": "संदेश दर्ज करें:",
        "analyze": "जांच करें",
        "safe": "✅ यह संदेश सुरक्षित लगता है",
        "danger": "⚠️ संभावित स्कैम!",
        "risk": "📊 जोखिम स्कोर",
        "grandma": "👵 आसान भाषा",
        "translate_input": "स्लैंग / इमोजी दर्ज करें:",
        "translate_btn": "समझाएं",
        "no_slang": "कोई स्लैंग नहीं मिला"
    }
}


# ------------------------------
# Slang + Emoji
# ------------------------------
slang_dict = {
    "omg": "oh my god (surprise)",
    "lol": "laughing out loud",
    "fr": "for real (serious)",
    "rn": "right now",
    "idk": "I don’t know",
    "brb": "be right back",
    "gtg": "got to go",
    "np": "no problem",
    "tbh": "to be honest",
    "imo": "in my opinion",

    "slayed": "did something extremely well",
    "ate": "did something very well",
    "bet": "okay / agreed",
    "cap": "lie",
    "no cap": "no lie / serious",
    "sus": "suspicious",
    "vibe": "feeling or mood",
    "lowkey": "a little bit / secretly",
    "highkey": "very / strongly",
    "rizz": "charm or flirting skill",
    "npc": "someone acting robotic or basic",
    "mid": "average / not impressive",
    "goat": "greatest of all time",

    "💀": "extremely funny",
    "🔥": "very good or exciting",
    "🤣": "laughing very hard",
    "😭": "crying or extreme emotion",
    "💅": "confidence / slayed",
    "👀": "interesting or suspicious",
    "🤡": "feeling foolish",
    "😎": "cool / confident",
    "😡": "angry",
}


def translate_slang(message):
    explained = []

    for key, value in slang_dict.items():
        if key in message.lower():
            explained.append(f"{key} → {value}")

    return explained



def calculate_risk(words):
    return min(len(words) * 15, 100)
def risk_label(score):
    if score < 30:
        return "🟢 Low Risk"
    elif score < 70:
        return "🟠 Medium Risk"
    else:
        return "🔴 High Risk"
# ------------------------------
# UI
# ------------------------------
# ------------------------------
# 🌐 Language Selector (TOP)
# ------------------------------


st.title("🛡️ SafeSpeak AI")
st.write("AI tool to detect scams & explain modern Gen-Z language")

lang = st.selectbox("🌐 Select Language", ["English", "বাংলা", "हिन्दी"])
# Scam Detector
st.header("🔍 Scam Detector")
msg = st.text_area("Enter message:")

if st.button("Analyze Message"):
    if not msg.strip():
        st.warning("Enter a message first")
    else:
        is_scam, words = detect_scam(msg)
        st.write("DEBUG words:", words)

    

        if is_scam:
            st.error("⚠️ Potential Scam Detected!")
            
            st.subheader("🚨 Detected Risk Words:")
            for w in words:
                st.write(f"- {w}")

            # ✅ ADD THIS BLOCK (RISK SCORE)
            score = calculate_risk(words)
            st.subheader("📊 Risk Score")
            st.progress(score)
            st.write(f"⚠️ Risk Level: {score}%")

            # 🔥 EXISTING PART (KEEP)
            st.subheader("🧠 Why this is dangerous:")
            for w in words:
                if w in explanation_dict:
                    st.write(f"👉 {w}: {explanation_dict[w]}")
                else:
                    st.write(f"👉 {w}: Suspicious keyword often used in scams.")

        else:
            st.success("✅ Message seems safe")


# Translator
st.header("👵 Grandma Mode")
msg2 = st.text_area("Enter slang / emoji message:")

if st.button("Explain Message"):
    if not msg2.strip():
        st.warning("Enter a message first")
    else:
        results = translate_slang(msg2)

        if results:
            st.subheader("Meaning:")
            for r in results:
                st.write(r)
        else:
            st.info("No slang detected")