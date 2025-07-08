import os 
from openai import OpenAI
from dotenv import load_dotenv 


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model_name = os.getenv("MODEL")

system_prompt = """

You are a professional writer and content analyst.

Your task is to summarize the following YouTube video transcript into a clear, well-structured, and engaging written summary.

Steps:
1. Read and understand the transcript to determine the niche and type of content (e.g., tutorial, documentary, product review, news analysis, motivational talk, interview, vlog, etc.).
2. Based on the niche and type, design an appropriate structure with clear section headings (4–7 sections) that best present the information.  
   Example section headings (to adapt depending on the video): Introduction, Key Points, Step-by-Step Guide, Insights, Takeaways, Future Plans, Conclusion.
3. Write the summary in full sentences and paragraphs, using a professional yet approachable tone.
4. Make the summary easy to read, informative, and useful — as if writing an article for an educated general audience.
5. If certain expected details are missing from the transcript, simply omit them gracefully.

Output:
- A structured written summary with clear section headings tailored to the video type and topic.
- Do not output bullet points or raw text without structure.

Be thoughtful, adaptive, and informative.

"""


def get_llm_insights(transcript_text):
    response = client.chat.completions.create(
        model= model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript_text}
        ],
        temperature=0.3,
        max_tokens=1000

    )
    return response.choices[0].message.content

