import google.generativeai as genai
from config.settings import GEMINI_API_KEY, MODEL_NAME
from utils.logger import get_logger

logger = get_logger()

class GeminiService:

    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate_text_response(self, prompt, history=None):
        try:
            logger.info("Sending text request to Gemini")

            if history:
                chat = self.model.start_chat(history=history)
                response = chat.send_message(prompt)
            else:
                response = self.model.generate_content(prompt)

            logger.info("Received response from Gemini")
            return response.text

        except Exception as e:
            logger.error(f"Gemini text error: {str(e)}")
            return "⚠️ Error generating response. Please try again."

    def generate_multimodal_response(self, prompt, file_bytes, mime_type):
        try:
            logger.info("Sending multimodal request to Gemini")

            response = self.model.generate_content(
                [
                    {"mime_type": mime_type, "data": file_bytes},
                    prompt
                ]
            )

            logger.info("Received multimodal response")
            return response.text

        except Exception as e:
            logger.error(f"Gemini multimodal error: {str(e)}")
            return "⚠️ Error processing uploaded file."
