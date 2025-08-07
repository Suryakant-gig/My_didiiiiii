import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Title
st.title("💖 A Surprise for My Sister")

# Section 1: Choose Nickname
nickname = st.selectbox(
    "How should I call you today?",
    ["My DiiDiii", "Suniiiii Billii", "Moro Didiii"]
)

# Section 2: Personalized Message
st.subheader("💌 A Letter to You")
st.write(f"""
Dear {nickname},

You are my biggest supporter, my secret keeper, and my best friend.
Here's a little surprise to show how much I love you!

No matter how grown-up we get, you'll always be my {nickname} ❤️
""")

uploaded_files = st.file_uploader("Upload your favorite photos here 💕", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

if uploaded_files:
    for file in uploaded_files:
        st.image(file, caption=file.name, use_column_width=True)

# Section 4: Generate QR Code
st.subheader("📱 Want to Open This on Your Phone?")
site_url = st.text_input("Enter the site URL to generate QR code (or leave as default):", "https://share.streamlit.io/your-link")

if st.button("Generate QR Code"):
    qr = qrcode.make(site_url)
    buffer = BytesIO()
    qr.save(buffer)
    st.image(buffer.getvalue(), caption="Scan to open!", use_column_width=False)

# Footer
st.markdown("❤️ Made with love by your brother.")
