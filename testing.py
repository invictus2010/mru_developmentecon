from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import os
from dotenv import load_dotenv

load_dotenv()

#documents = SimpleDirectoryReader('transcript').load_data()
index = GPTSimpleVectorIndex.load_from_disk('index.json')

response = index.query("Economy A has lots of human capital, Economy B has less human capital. Since Economy A has lots of human capital the price of such capital is low. Since Economy B has less human capital the price of human capital is high. Workers with lots of human capital, therefore, should prefer (all else equal) to work in Economy B.", verbose=True)
print(response)
#index.save_to_disk('index.json')