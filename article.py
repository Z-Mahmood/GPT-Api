import os
from dotenv import load_dotenv
import openai


class ArticleProcessor:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        openai.api_key = os.getenv("OPENAI_API_KEY")
        print(openai.api_key)

    def summarize_and_translate(self, content, target_language="Italian"):
        try:
            # construct the prompt
            prompt = f"""Summarise this article in 3 to 4 sentences and also give me a translation of the summary in {target_language.lower()}:\n{content}"""

            # create chat completions
            api_response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
            )
            return api_response
        except Exception as e:
            return f"An error occurred: {str(e)}"
