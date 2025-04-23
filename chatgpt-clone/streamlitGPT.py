import streamlit as st
from openai import OpenAI

st.title('ChatGPT Like')

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

# Inicializa o modelo e as mensagens na sessão
if "openai_model" not in st.session_state:
    st.session_state['openai_model'] = 'gpt-3.5-turbo'

if "messages" not in st.session_state:
    st.session_state['messages'] = []

# Exibe as mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Input do usuário
if prompt := st.chat_input('What is up?'):
    instructions = "Responda as perguntas do usuário de maneira informal"

    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Adiciona instrução do sistema antes da resposta
    chat_history = [{"role": "system", "content": instructions}] + st.session_state.messages

    # Gera resposta da IA
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state['openai_model'],
            messages=chat_history,
            stream=True,
        )
        response = st.write_stream(stream)

    # Salva resposta no histórico
    st.session_state.messages.append({"role": "assistant", "content": response})
