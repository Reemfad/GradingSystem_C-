import os
from dotenv import load_dotenv

load_dotenv()

# LLM configuration
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))

# Safety / limits
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))

# Validation
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY not set in environment")

## The added difference 
import os
from dotenv import load_dotenv

load_dotenv()


