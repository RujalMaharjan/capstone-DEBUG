import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Chatbot")

# Sidebar for instructions and settings
with st.sidebar:
    st.title("💬 Welcome to Chatbot")
    st.title("by Debug Thugs")
    st.write('This chatbot uses Gemini')

# Store chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state['chat_history']:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state['chat_history'] = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

def get_response(message):
    url = 'http://aiback-service:5000/api/chat'  # Updated backend URL
    data = {'message': message}
    try:
        response = requests.post(url, json=data)
        response_data = response.json()
        return response_data.get('response')
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # User input
    input_message = st.chat_input(disabled=False)
    if input_message:
        st.session_state['chat_history'].append({"role": "user", "content": input_message})
        with st.chat_message("user"):
            st.write(input_message)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_response(input_message)
                placeholder = st.empty()
                placeholder.markdown(response)
                st.session_state['chat_history'].append({"role": "assistant", "content": response})

if __name__ == '__main__':
    main()