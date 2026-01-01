import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from config import llm

def create_data_agent(csv_path: str):
    df = pd.read_csv(csv_path)

    return create_pandas_dataframe_agent(
        llm,
        df,
        verbose=False,
        allow_dangerous_code=True
    )
