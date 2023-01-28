# Marginal Revolution Development Economics

This project explores the value of GPT and embeddings in summarizing and cataloging knowledge from an online course such as MRU's [Development Economics Course](https://mru.org/development-economics). We will see what value, if any, GPT yields in helping us pass an online exam. 

Marginal Revolution University (MRU) provides online courses in economics. They host their videos on YouTube, which allows us to pull their transcripts. After indexing their transcripts, I query them based on the exam questions and receive a natural language response, all powered by OpenAI's GPT API. 

I've found that it's surprisingly hard to pass their exam after "training" GPT on their course. There is likely room to improve in:

* Prompting / queries (less technical)
* Index structure of the transcripts (more technical)

Or maybe Tyler Cowen and Alex Tabarrok are just really good at writing exams that can't be passed by (relatively) naive implementations of GPT!

# Approach
1. Scrape the YouTube [playlist](http://youtube.com/playlist?list=PL-uRhZ_p-BM4pQXFm4hCmMR7LhTXje61m) for each video's transcript. `app.py` accomplishes this.
2. Store the transcript as a monolithic text file. I found that the transcript is a total of 171,619 words.
3. Use the [gpt-index](https://github.com/jerryjliu/gpt_index) library to index the transcript file and generate embeddings stored as a JSON file. `testing.py` does this. The relevant portions of the code are commented out because I moved on to to step 4.
4. Go to the Development Economics exam page. Use gpt-index functions to generate queries based on the exam questions. In `testing.py`, write your question in the `index.query` function.

An alternative approach to try might be to store the transcripts for each video, generate summaries for each video, and use the tree index approach. This might help warm-start your AI/bot's better understand themes that span multiple videos. 

# My attempt
The final exam is multiple choice format. This requires us to think a little creatively about how to prompt. OpenAI provides some [suggestions](https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md) on improving "reliability" that motivated my follow-on approach
The following are example questions and responses. I'll go through the first 3 questions and then only the highlights from then on. You can find my query/response history in `response.csv`.

Note: To the best of my ability, I answered the test naively. Even if I knew GPT was supplying the wrong answer, I didn't override the response. This is **not** how I would expect students would respond. If a student "knew" the answer, they're likely to not query GPT for the answer or nudge the queries in certain directions.

## Question 1 ✅
Verbatim question: 
```
Corruption in some instances may benefit economic growth because:
a) Bribing corrupt officials may clear the way for new investments
b) Corruption increases the quantity of spending in an economy
c) The data show that corrupt economies grow more rapidly
```
My question to GPT: `Let's think step by step. How can corruption can benefit economic growth`

Answer: 
```
Corruption can benefit economic growth by providing incentives for businesses to invest in a country. By providing bribes to government officials, businesses can gain access to resources and opportunities that would otherwise be unavailable. This can lead to increased investment, which can lead to increased economic growth. Additionally, corruption can lead to increased efficiency in government processes, as businesses can pay bribes to speed up the process of obtaining licenses and permits. This can lead to increased economic activity and growth. However, it is important to note that corruption can also lead to a decrease in the quality of bureaucracy and the rule of law, which can have a negative effect on economic growth. Therefore, it is important to ensure that corruption is monitored and punished in order to ensure that it does not have a negative effect on economic growth.
```
That sounds like answers a) to me.

## Question 2 ✅
TLDR; it didn't really like any of the answer choices. Which may mean it actually passed this one? Maybe I'm being generous here.

Verbatim question:
```Which is most likely true?:

a) Mainly economic growth causes more spending on education
 
b) Mainly more spending on quality education causes more economic growth
 
Both a) and b) are true and the causality runs both ways
```
My question to GPT: "Let's think step by step. What's the relationship between spending on education and economic growth?"

Answer:
```
The relationship between spending on education and economic growth is complex. Generally, it is accepted that education is one of the key factors in economic growth, but it is not the only factor. In order for a nation to experience take-off economic growth, it must get many different things right, including education. Poor educational systems can have a significant negative impact on economic growth, as evidenced by the lower test scores and lower economic growth rates in Latin American countries. However, it is not just the number of years of education that matters, but also the quality of education. Informing parents about the benefits of education can pay for itself many times over, and parents should diversify their educational investments rather than putting all their eggs in one basket. In regions where social capital is stronger, such as Northern Europe, most education tends to be supplied by the public sector. At the primary and secondary levels, this education tends to be quite strong, but it is important to note that in regions with lower social capital, private schools may be necessary to provide education to those who would otherwise not have access. Ultimately, the relationship between spending on education and economic growth is complex and depends on many factors.
```
My next question to GPT: "Let's think step by step. Does spending more on education cause economic growth?"

Answer:
```
No, more spending on education alone does not necessarily cause economic growth. It is important to consider the quality of education, not just the amount of money spent. Additionally, other factors such as infrastructure, social capital, and cultural practices must be taken into account. For example, in Sweden, the development of the country is coeval with the development of education, but it is difficult to determine which of the habits and norms are part of the education system and which are part of the broader Swedish code of success. In regions where social capital is stronger, such as Northern Europe, most education tends to be supplied by the public sector, which tends to be quite strong. However, in regions with lower social capital, private schools may be necessary, but they are typically not the highest quality schools. Therefore, it is important to consider the broader context when evaluating the impact of education on economic growth, including the level of social capital and the availability of public sector educational provision.
```

This struck me as odd because the answer narrows into "quality of education" as a lever, which is not what I asked. Oh wait! The original question is asking about spending on "quality of education!" I'm not really asking the right question here.

My next question to GPT: "Let's think step by step. Does more spending on quality education cause economic growth?"

Answer:
```
No, more spending on education alone does not necessarily cause economic growth. It is important to consider the quality of education, not just the amount of money spent. Additionally, other factors such as infrastructure, social capital, and cultural practices must be taken into account. For example, in Sweden, the development of the country is coeval with the development of education, but it is difficult to determine which of the habits and norms are part of the education system and which are part of the broader Swedish code of success. In regions where social capital is stronger, such as Northern Europe, most education tends to be supplied by the public sector, which tends to be quite strong. However, in regions with lower social capital, private schools may be necessary, but they are typically not the highest quality schools. Therefore, it is important to consider the broader context when evaluating the impact of education on economic growth, including the level of social capital and the availability of public sector educational provision
```

Hmmm. Let me try asking about the second option 

Verbatim question: `Let's think step by step. Does economic growth cause more spending on education?`

Answer:
```
No, economic growth does not necessarily cause more spending on education. Economic growth is a complex process that requires a nation to get many different things right, including education. However, getting education right alone may not yield large social returns. In some cases, such as in Latin American countries, bad educational systems have been a reason why economic growth has not been higher. Additionally, in some developing nations, parents may not understand the rate of return on education, and thus may not prioritize spending on education. In regions where social capital is stronger, such as Northern Europe, most education tends to be supplied by the public sector. At the primary and secondary levels, this education tends to be quite strong, but in regions with lower social capital, private schools may be necessary to provide education. However, these schools may not be the highest quality schools, as they are often low fee schools with large numbers of teachers, and may not provide the same quality of education as public schools in regions with higher social capital.
```
Ugh! I wouldn't be confident in the answers here solely using GPT

## Question 3 ✅
Verbatim question: 
```
Which of the following are not major problems for the contemporary Indian economy?:
a) Not enough investment in energy infrastructure
 
b) Low agricultural productivity
 
c) Tariffs have been set too low
 
d) Underutilization and inefficient use of female workers
```
My approach here will be to ask GPT about each answer choice. For instance, "Let's think step by step. Is investment in energy infrastructure a problem for the Indian economy?"

It gets the answer correct and only identifies one of these as the problem.

# Results
Question 1 ✅
2 ✅
3 ✅
4 ❌
5 ✅
6 ✅
7 ✅
8 ❌
9 ✅
10 ✅
11 ✅
12 ✅
13 ✅
14 ✅
15 ✅
16 ✅
17 ❌
18 ❌
19 ✅
20 ❌