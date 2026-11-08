import streamlit as st
import google.generativeai as genai
from PIL import Image

# הגדרת עיצוב הדף למובייל ולסגנון נקי עם אייקון חולצה
st.set_page_config(
    page_title="הסטייליסטית האישית",
    page_icon="👕",
    layout="centered"
)

st.title("👕 הסטייליסטית האישית שלך")
st.write("צצממי או העלי תמונה של הבגדים, וקבלו ייעוץ מהיר לבוקר יחד עם הסבר ללמידה בהמשך!")

# שדה להזנת מפתח ה-API החינמי של Gemini
st.sidebar.header("הגדרות")
api_key = st.sidebar.text_input("הכנס מפתח Google Gemini API:", type="password")

if not api_key:
    st.warning("נא להזין מפתח API כדי להתחיל. (ניתן לקבל מפתח חינמי לגמרי מ-Google AI Studio).")
else:
    genai.configure(api_key=api_key)
    # שימוש במודל החינמי המהיר שתומך בתמונות
    model = genai.GenerativeModel('gemini-1.5-flash')

    # העלאת תמונה מהטלפון
    uploaded_file = st.file_uploader("צניחי או בחרי תמונת בגדים:", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="הבגדים שנבחרו", use_column_width=True)

        if st.button("נתחי לי את ההופעה! ✨", type="primary"):
            with st.spinner("הסטייליסטית חושבת על שילוב מושלם..."):
                
                # ה-Prompt המדויק שהוגדר עבור אשתך
                prompt = """
                אתה סטייליסט אישי דיגיטלי אמפתי, חיובי, מעודד ומקצועי המותאם במיוחד לנשים.
                תפקידך לעזור למשתמשת להתאים בגדים (צבעים וסגנון אחד לשני) מתוך התמונה שסופקה.
                שמור תמיד על טון חם, מכיל, בונה ונעים. אל תתייחס למבנה גוף, אלא אך ורק לשילוב צבעים, טקסטורות וסגנון הפריטים אחד לשני.

                חובה לחלק את התשובה שלך לשני חלקים ברורים בדיוק לפי המבנה הבא:

                1. חלק ראשון - השורה התחתונה (לבוקר המהיר):
                - חיזוק חיובי ומחמיא על הבחירה.
                - ציון התאמה קצר (למשל: "עובד מעולה!", "דורש תיקון קטן").
                - 1-2 טיפים פרקטיים ומהירים לשדרוג המראה ברגע האמת.

                2. חלק שני - פינה ללמידה (לקריאה בזמן פנוי אחר כך):
                - תחת כותרת ברורה: "למה זה עובד? (להעשרה אחר כך)"
                - הסבר קצר ומקצועי על ה"למה" מאחורי השילוב (התייחסות למעגל הצבעים, איזון בין גזרות, או כללי סגנון) – כדי לבנות ביטחון וידע לעתיד.
                """

                try:
                    response = model.generate_content([prompt, image])
                    
                    # הצגת התוצאה למשתמשת
                    st.markdown("---")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"אירעה שגיאה בניתוח התמונה: {e}")