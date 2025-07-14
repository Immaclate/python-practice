def detect_emotion(text):
    if "happy" in text or "joy" in text:
        return "😊 Happy"
    elif "sad" in text or "low" in text:
        return "😢 Sad"
    elif "angry" in text or "mad" in text:
        return "😠 Angry"
    else:
        return "😐 Neutral"

user_input = input("How are you feeling today? ")
emotion = detect_emotion(user_input.lower())
print("Detected Emotion:", emotion)
