import streamlit as st
import requests

st.set_page_config(
    page_title="Enterprise Secure RAG",
    layout="wide"
)

st.title("Enterprise Secure RAG System")

st.markdown("---")

query = st.text_input(
    "Ask Enterprise Question"
)

if st.button("Submit Query"):

    if query.strip() == "":

        st.warning("Please enter a query")

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={
                    "query": query
                }
            )

            data = response.json()

            st.success("Query Processed Successfully")

            st.subheader("Query")

            st.write(data["query"])

            st.subheader("Retrieved Results")

            for index, result in enumerate(
                data["results"]
            ):

                st.markdown(
                    f"### Result {index + 1}"
                )

                st.write(result["content"])

                st.json(result["metadata"])

        except Exception as e:

            st.error(str(e))