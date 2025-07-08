from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import streamlit as st
from insights import get_llm_insights
import re
# from llm

def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    """
    # This pattern ensures only the 11-character ID is captured
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})(?=[^\w-]|$)"
    match = re.search(pattern, url)
    return match.group(1) if match else None

youtube_url = st.text_input("input the video url", "the youtube url")
if youtube_url:
    video_id = extract_video_id(youtube_url)
    if video_id:
        st.write("Valid YouTube URL.", youtube_url)
        st.write("Extracted video ID:", video_id)
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            st.write(transcript_list)

            transcript_text = ""
            for line in transcript_list:
                transcript_text += line['text'] + "\n"

            st.text_area("Transcript", transcript_text, height=500)

            if st.button("Generate Summary"):
                with st.spinner("Generating summary..."):
                    summary = get_llm_insights(transcript_text[:11000])
                    st.success("insight:")
                    st.write(summary)
        except TranscriptsDisabled:
            st.error("❌ Transcripts are disabled for this video.")
        except NoTranscriptFound:
            st.error("❌ No transcript found. The video may not have captions.")
        except Exception as e:
            st.error(f"⚠️ Unexpected error: {e}")
    else:
        st.write("Invalid URL, input a valid URL link.")
