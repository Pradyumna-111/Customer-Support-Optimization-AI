import litellm

litellm.enable_prompt_caching = False
litellm.turn_off_message_caching = True
from crew import crew

ticket = {
    "ticket": """
    I have been trying to cancel my subscription for the past two weeks but the
    cancel button on the billing page is not working. I keep getting charged every
    month even though I no longer use the service. I already contacted support twice
    but got no response. I need this resolved immediately or I will dispute the
    charges with my bank.
    """
}

result = crew.kickoff(inputs=ticket)

print(result)