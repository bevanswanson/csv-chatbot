# csv-chatbot
trsti

A chatbot that lets you use an LLM to query a CSV.

## Get Started

Install the requirements using `pip install -r requirements.txt`

To run the chatbot using streamlit, use `streamlit run app/streamlit-app.py`

This requires either an OpenAI API key, or a compiled local LLM model.

Note: If you want to use a local model, uncomment the relevant code in the `streamlit-app.py` (janky, I know).


## Important

Remember, this is being sent to a public model, so do not upload any files you wouldn't want uploaded publicly.


## Generate fake data

If you want to generate fake data, run `python generate-mock-data.py` for a pollution list you can query.
