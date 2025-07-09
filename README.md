# 📄 **YouTube Transcript Summarizer (GPT-powered)**


🎥🔍 A **Streamlit app** that extracts the transcript from a YouTube video and summarizes it into a clear, structured, and engaging article using **OpenAI GPT**.

----
in this project i use the following laibrary :
----
streamlit : for a simple frontend.
youtube_transcript_api : to get the youtube video from the link (youtube ID)
openai : i use it for the gpt llm so i use gpt-4o-mini because the token limit is hight and its cheap

----
## 🚀 Features
----

✅ Paste a YouTube video URL.  
✅ Automatically fetch and display the transcript (if available).  
✅ Generate a professional, structured summary powered by GPT.  
✅ Gracefully handles errors if captions are unavailable or disabled.


----
📂 Setup
----

1️⃣ Clone this repository

2️⃣ Install dependencies:
pip install streamlit youtube-transcript-api openai python-dotenv

3️⃣ Configure your environment variables:
rename the .env to .env .exemple 
Edit .env and fill in your API key and preferred GPT model.

4️⃣ Run the app: 
streamlit run main.py / then the app gonna popup in the browser 

----
💻 How to Use:
----

✅ Once the app is running in your browser:

Enter a valid YouTube video URL in the input box.
Example:
https://www.youtube.com/watch?v=dQw4w9WgXcQ NB: it should be in the form of the previese link because i didnt do regex for the other links form :)


The app will extract and display the transcript (if captions are available).

Click the "Generate Summary" button.

Wait for the GPT model to process the transcript and generate a clear, structured summary.

Read or copy the summary for your own use!




