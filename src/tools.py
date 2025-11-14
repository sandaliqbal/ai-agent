import uuid
from langchain.tools import tool


@tool
def order_lookup(order_id: str):
    """Look up order status by order ID."""
    # Replace with DB/API call to order management
    # Stub: Return fake order info
    if not order_id:
        return "Please provide an order id."
    return f"Order {order_id}: Status=Shipped, ETA=2025-11-10, Items: 2"


@tool
def create_ticket(summary: str, user_email: str = None):
    """Create a support ticket with the given summary and optional user email."""
    # Replace with real ticketing system integration
    ticket_id = str(uuid.uuid4())[:8]
    # store to DB or call external API
    return f"Ticket created: {ticket_id}. Summary: {summary[:120]}"


@tool
def check_weather(location: str) -> str:
    """Return the weather forecast for the specified location."""
    return f"It's always sunny in {location}"
