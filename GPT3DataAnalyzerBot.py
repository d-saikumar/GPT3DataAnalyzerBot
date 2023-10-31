# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:22:48 2023

@author: Sai
"""

import pandas as pd
import openai

# Set your OpenAI API key
openai.api_key = 'OPENAPI_KEY'
#Read the dataset
data = pd.read_excel('sample_data.xlsx')

def generate_response(prompt, dataset):
    full_prompt = f"{prompt}\n\nDataset Information:\n{dataset}"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=full_prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

prompt = "Please analyze the dataset and provide insights."
dataset_info = data.describe().to_string()
response = generate_response(prompt, dataset_info)