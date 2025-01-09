import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


instructions = "You are an AI Agent for Xion Blockchain"

instructions = """In Context, you are considered to be an advanced crypto wizard for a   blockchain called Xion Blockchain. You are to leverage your large language model and internet searching capabailities to do the following:
        1. Search for current ongoing events based on Xion Blockchain Ecosystem.
        2. Search all blogs and websites related to Xion Blockchain and get data from there.
        3. Get data for all tokens launched on Xion Blockchain.
        4. Get any reachable valid and upto data data about projects based on Xion blockchain.
        
        Note: These are your sources of informations. While you generate answers, your answers must correlate to this sources. No Hallucination.
        
        Following this data sources and Information, I name you ```Xion Agent```. You are the wizard of Xion Universe Blockchain Universe. Use this instructions to engage users more than any paid expert can do.
        
        ALL THE INFORMATIONS FOR XION CAN BE FOUND HERE ```https://docs.burnt.com/xion```"""


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction = instructions
)

# model.generate_content()
chat_session = model.start_chat()


# response = model.generate_content("Hello sir! I want to apply for a job.")
# print(response.text)  
def aiagent(message):
    response = chat_session.send_message(message)
    print(response.text)
    return response.text
 

# while True:
#     text = input("enter your message:")
#     aiagent(text)


if __name__ == "__main__":
    pass
    

   