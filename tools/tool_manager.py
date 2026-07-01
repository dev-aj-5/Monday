import re

from click import prompt

from tools.calculator import evaluate
from tools.time import get_time
from tools.date import get_date
from tools.random import handle_random
from tools.uuid_tool import generate_uuid
from tools.internet.internet_manager import handle_internet

def handle_tool(prompt):

    prompt_lower = prompt.lower().strip()

    # ----------------------------
    # Time
    # ----------------------------

    if "time" in prompt_lower:

        return get_time()

    # ----------------------------
    # Date
    # ----------------------------

    if "date" in prompt_lower or "today" in prompt_lower:

        return get_date()

    # ----------------------------
    # UUID
    # ----------------------------

    if "uuid" in prompt_lower:

        return generate_uuid()

    # ----------------------------
    # Random
    # ----------------------------

    random_result = handle_random(prompt)

    if random_result is not None:

        return random_result

    # ----------------------------
# Calculator
# ----------------------------

    expression = prompt_lower

    expression = expression.replace("what's", "")
    expression = expression.replace("what is", "")
    expression = expression.replace("calculate", "")
    expression = expression.replace("solve", "")
    expression = expression.replace("?", "")
    expression = expression.strip()

    if re.fullmatch(r"[0-9+\-*/().\s]+", expression):

        try:

         return str(evaluate(expression))

        except Exception:

            return "I couldn't calculate that." 
        
# ----------------------------
# Internet Services
# ----------------------------

    internet_result = handle_internet(prompt)

    if internet_result is not None:
        return internet_result


    return None