import streamlit as st
from elitza.eliza import Eliza

@st.cache_data
def load_eliza():
    eliza = Eliza()
    eliza.load('elitza/doctor.txt')
    return eliza

def app():
    eliza = load_eliza()
    st.title(":robot_face: :balloon: E:orange[lit]za")
    st.markdown("[ELIZA](https://github.com/wadetb/eliza) with streamlit")
    # todo: add more info about ELIZA, see https://en.wikipedia.org/wiki/ELIZA

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": eliza.initial()})

    if "stopped" not in st.session_state:
        st.session_state.stopped = False 

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.session_state.stopped:
        st.markdown("Conversation with Eliza has ended.")
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
