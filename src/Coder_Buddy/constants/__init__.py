PUBLIC_FOLDR_PATH = "public"
import os

# LLM_MODEL_ID = "us.meta.llama3-3-70b-instruct-v1:0"
# LLM_REGION = "us-east-1"

LLM_MODEL_ID=os.getenv("MODEL_NAME")


# ------------ Coding in Loop ----------------

PIPELINE_NAME="coding_in_loop"
ARTIFACT_DIR="artifacts"