import streamlit as st
import random

# -----------------------------
# Page Setup
# -----------------------------

st.set_page_config(
    page_title="Customer Support Chatbot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Order Database
# -----------------------------

orders = {
    "ORD101": {
        "status": "Processing",
        "delivery": "Expected in 5 days"
    },
    "ORD102": {
        "status": "Shipped",
        "delivery": "Expected in 3 days"
    },
    "ORD103": {
        "status": "Out for Delivery",
        "delivery": "Arriving Today"
    },
    "ORD104": {
        "status": "Delivered",
        "delivery": "Delivered Successfully"
    }
}

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = None

# -----------------------------
# Header
# -----------------------------

st.title("🤖 Customer Support Chatbot")
st.write("Welcome! Ask me about orders, refunds, shipping, returns, and support.")

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.header("📌 Quick Topics")

    st.markdown("""
- 📦 Track Order
- ❌ Cancel Order
- 🚚 Shipping Information
- 💰 Refund Policy
- 🔄 Return Product
- ⚠️ Damaged Product
- 💳 Payment Methods
- 📞 Contact Support
- ⏰ Business Hours
""")

# -----------------------------
# Display Chat History
# -----------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------

prompt = st.chat_input("Ask your question...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    user_input = prompt.lower().strip()

    # -----------------------------
    # TRACK ORDER MODE
    # -----------------------------

    if st.session_state.mode == "track":

        order_id = prompt.upper().strip()

        if order_id in orders:

            reply = f"""
📦 Order Details

**Order ID:** {order_id}

**Status:** {orders[order_id]['status']}

**Delivery:** {orders[order_id]['delivery']}
"""

        else:

            reply = """
❌ Invalid Order ID

Available Demo IDs:

• ORD101
• ORD102
• ORD103
• ORD104
"""

        st.session_state.mode = None

    # -----------------------------
    # CANCEL ORDER MODE
    # -----------------------------

    elif st.session_state.mode == "cancel":

        order_id = prompt.upper().strip()

        if order_id in orders:

            if orders[order_id]["status"] == "Delivered":

                reply = f"""
❌ Order {order_id} cannot be cancelled because it has already been delivered.
"""

            else:

                reply = f"""
✅ Cancellation Request Submitted

Order ID: {order_id}

Current Status: {orders[order_id]['status']}

Our team will process your request shortly.
"""

        else:

            reply = """
❌ Invalid Order ID

Available Demo IDs:

• ORD101
• ORD102
• ORD103
• ORD104
"""

        st.session_state.mode = None

    # -----------------------------
    # DIRECT ORDER ID
    # -----------------------------

    elif prompt.upper().strip() in orders:

        order_id = prompt.upper().strip()

        reply = f"""
📦 Order Details

**Order ID:** {order_id}

**Status:** {orders[order_id]['status']}

**Delivery:** {orders[order_id]['delivery']}
"""

    # -----------------------------
    # INVALID ORDER ID
    # -----------------------------

    elif prompt.upper().startswith("ORD"):

        reply = """
❌ Invalid Order ID

Available Demo IDs:

• ORD101
• ORD102
• ORD103
• ORD104
"""

    # -----------------------------
    # GREETINGS
    # -----------------------------

    elif user_input in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:

        reply = """
👋 Hello!

Welcome to Customer Support.

How can I assist you today?
"""

    # -----------------------------
    # TRACK ORDER
    # -----------------------------

    elif any(text in user_input for text in [
        "track",
        "order status",
        "where is my order",
        "track my order",
        "status of my order"
    ]):

        st.session_state.mode = "track"

        reply = """
📦 Order Tracking

Please enter your Order ID.

Demo IDs:

• ORD101
• ORD102
• ORD103
• ORD104
"""

    # -----------------------------
    # CANCEL ORDER
    # -----------------------------

    elif "cancel" in user_input:

        st.session_state.mode = "cancel"

        reply = """
❌ Order Cancellation

Please enter your Order ID.

Demo IDs:

• ORD101
• ORD102
• ORD103
• ORD104
"""

    # -----------------------------
    # SHIPPING
    # -----------------------------

    elif any(text in user_input for text in [
    "when will my order be shipped",
    "shipping",
    "shipping information",
    "has my order shipped",
    "shipping time",
    "delivery time"
]):

        reply = """
🚚 Shipping Information

Orders are usually shipped within 24-48 hours.

Standard Delivery: 3-5 Business Days

Express Delivery: 1-2 Business Days
"""

    # -----------------------------
    # REFUND
    # -----------------------------

    elif "refund" in user_input:

        reply = """
💰 Refund Policy

Refunds are processed within 5-7 business days after approval.
"""

    # -----------------------------
    # RETURN
    # -----------------------------

    elif "return" in user_input:

        reply = """
🔄 Return Policy

Products can be returned within 7 days of delivery.
"""

    # -----------------------------
    # DAMAGED PRODUCT
    # -----------------------------

    elif any(text in user_input for text in [
        "damage",
        "damaged",
        "broken",
        "defect",
        "defective",
        "faulty",
        "not working"
    ]):

        complaint_id = "CMP" + str(random.randint(1000, 9999))

        reply = f"""
⚠️ Damaged Product Complaint Registered

Please:

1. Take photos of the product.
2. Keep the original packaging.
3. Submit a return request.

🎫 Complaint ID: {complaint_id}

Our support team will contact you shortly.
"""

    # -----------------------------
    # PAYMENT METHODS
    # -----------------------------

    elif any(text in user_input for text in [
        "payment",
        "upi",
        "cash on delivery",
        "cod",
        "pay",
        "payment method"
    ]):

        reply = """
💳 Accepted Payment Methods

• UPI

• Credit Card

• Debit Card

• Net Banking

• Cash On Delivery (COD)
"""

    # -----------------------------
    # CONTACT SUPPORT
    # -----------------------------

    elif any(text in user_input for text in [
        "contact",
        "support",
        "customer care",
        "customer care number",
        "support email",
        "help"
    ]):

        reply = """
📞 Contact Support

Email: support@shopmart.com

Phone: +91 9876543210

Monday - Saturday

9:00 AM to 6:00 PM
"""

    # -----------------------------
    # BUSINESS HOURS
    # -----------------------------

    elif any(text in user_input for text in [
        "hours",
        "timing",
        "working",
        "open",
        "customer service hours"
    ]):

        reply = """
⏰ Business Hours

Monday - Saturday

9:00 AM to 6:00 PM
"""

    # -----------------------------
    # THANK YOU
    # -----------------------------

    elif "thank" in user_input:

        reply = """
😊 You're welcome!

Have a great day.
"""

    # -----------------------------
    # DEFAULT
    # -----------------------------

    else:

        reply = """
❓ Sorry, I couldn't understand that.

Try asking:

• Track my order

• Cancel my order

• Where is my order?

• What is my order status?

• When will my order be shipped?

• Refund policy

• Return policy

• My product is damaged

• Payment methods

• Contact support
"""

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)