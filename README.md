# Search Engine Challenge:

Build a service that allows students to search through coursebooks summaries which would make picking and buying a coursebook, a much better experience for students.
First we need to develop a local version of the system. Our bot scraped a website with book summaries, and stored them in 
​data.json​ in the ​summaries​ array. The summaries array is a small data example for local development. You should assume that the real service will have ~10^6 summaries.
Your goal is to code a search utility function/class that given a search query, searches the book summaries and returns the ​K​ most relevant ones. A search engine query is the set of keywords that users will type in order to find a relevant document. You are allowed to use only basic language (python/javascript) functionality.
The api of the search engine should be as follows:
 
```
Input: The input should be a user query ​of​ ​type​ ​string ​and​ number ​of items to ​return
query (string): eg. ​'is​ your problems' K (integer): eg. ​3
Output: List ​of​ K relevant summaries sorted according to order ​of relevance given a query. A summary ​is​ a dictionary that follows the
  schema: {​'summary​': string, ​'id​': integer} summaries: eg. [
{​'summary​':'​The Book ​in​ Three Sentences: Practicing meditation ​and​ mindfulness will make you ​at​ least ​10​ percent
happier....', ​'id​':​0​},
{​'summary​':'​The Book ​in​ Three Sentences: Finding
something important ​and​ meaningful ​in​ your life ​is​ the most productive use​ ​of​...', ​'id​':​48​},
{​'summary​':'​The Book ​in​ Three Sentences: Everything ​in life ​is​ an invention. ​If​ you choose to look ​at​ your life ​in​ a ​new
way...', ​'id​':​7​} ]
```

# To use the script :
1. Activate the virtual environment
    `` source venv/bin/activate``
2. Install the requirements ``pip install -r requirements.txt``
3. Run the main scripts ``python main.py``
4. Coverage `` coverage run -m unittest``

