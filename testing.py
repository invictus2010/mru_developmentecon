from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import os
from dotenv import load_dotenv
import csv

load_dotenv()

#ocuments = SimpleDirectoryReader('transcript').load_data()
#index = GPTSimpleVectorIndex(documents)
index = GPTSimpleVectorIndex.load_from_disk('index.json')
#index.save_to_disk('index.json')
question = "You are taking a multiple choice test. To answer the question use the following procedure: 1) Read the question carefully 2) Read an answer 3) Evaluate whether that answer is a valid explanation to the question 4) Read and evaluate the next answer 5) return all answers that are valid explanations to the question Question: What is the main problem with microcredit Answer: 1) Petty entrepreneurship does not always yield such high returns 2) It is hard to pay back fifty or one hundred percent per annum on a regular basis 3) Savings is a cheaper way to keep liquid capital on hand"
response = index.query(question)
# Append question and response to csv file with columns: question, response"
with open('response.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow([question, response])
print(response)
