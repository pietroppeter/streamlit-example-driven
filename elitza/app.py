import streamlit as st
from elitza.eliza import Eliza
import base64

b = base64.b64encode(bytes("your string", "utf-8"))  # bytes
base64_str = b.decode("utf-8")  # convert bytes to string


@st.cache_data
def load_eliza():
    eliza = Eliza()
    eliza.load("elitza/doctor.txt")
    return eliza


weird_unicode = "℘"

Messages = list[dict[str, str]]


def decode(encoded_string: str) -> Messages:
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode("utf-8")
    message_list = decoded_string.split(weird_unicode)
    messages = [
        {
            "role": "assistant" if i % 2 == 0 else "user",
            "content": m,
        }
        for i, m in enumerate(message_list)
    ]
    return messages


def encode(messages: Messages) -> str:
    s = weird_unicode.join([m["content"] for m in messages])
    encoded_bytes = base64.b64encode(s.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")
    return encoded_string


def app():
    eliza = load_eliza()
    st.title(":robot_face: E:orange[lit]ZA")
    st.markdown("[ELIZA](https://github.com/wadetb/eliza) with streamlit")
    # todo: add more info about ELIZA, see https://en.wikipedia.org/wiki/ELIZA

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "encoded_messages" in st.experimental_get_query_params():
        encoded_messages = st.experimental_get_query_params()["encoded_messages"][0]
        st.experimental_set_query_params()
        st.session_state.messages = decode(encoded_messages)
        st.session_state.stopped = True

    if not st.session_state.messages:
        st.session_state.messages.append(
            {"role": "assistant", "content": eliza.initial()}
        )

    if "stopped" not in st.session_state:
        st.session_state.stopped = False

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state.stopped:
        st.markdown("Conversation with Eliza has ended.")
        if st.button("Bookmark the conversation as url"):
            encoded_messages = encode(st.session_state.messages)
            st.experimental_set_query_params(encoded_messages=encoded_messages)
        if st.button("Restart"):
            st.session_state.messages = []
            st.session_state.stopped = False
            st.rerun()
        st.stop()

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = eliza.respond(prompt)
        if response is None:
            with st.chat_message("assistant"):
                st.markdown(eliza.final())
            st.session_state.stopped = True
            st.rerun()
        else:
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)


if __name__ == "__main__":
    app()
