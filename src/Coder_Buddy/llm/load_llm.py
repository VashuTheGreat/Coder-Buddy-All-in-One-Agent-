# from langchain_aws import ChatBedrockConverse

from langchain_groq import ChatGroq

from src.Coder_Buddy.constants import LLM_MODEL_ID


llm=ChatGroq(
    model=LLM_MODEL_ID,
    
    # region_name=LLM_REGION,
)

# llm=ChatBedrockConverse(
#     model=LLM_MODEL_ID,
#     region_name=LLM_REGION,
# )