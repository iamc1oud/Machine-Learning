# Libraries Used
- NLTK
- genism
- pattern

# Tokenize Text Data
When we deal with text, we need to break it down into smaller pieces for analysis. This is
where tokenization comes into the picture. It is the process of dividing the input text into a
set of pieces like words or sentences. These pieces are called tokens.

# Converting words to their base forms using stemming
Working with text has a lot of variations included in it. We have to deal with different
forms of the same word and enable the computer to understand that these different words
have the same base form. For example, the word sing can appear in many forms such as
sang, singer, singing, singer, and so on. We just saw a set of words with similar meanings.
Humans can easily identify these base forms and derive context.
When we analyze text, it's useful to extract these base forms. It will enable us to extract
useful statistics to analyze the input text. Stemming is one way to achieve this. The goal of a
stemmer is to reduce words in their different forms into a common base form. It is basically
a heuristic process that cuts off the ends of words to extract their base forms. Let's see how
to do it using NLTK.<br>
The Porter stemmer is the least in terms of strictness and Lancaster is the strictest. If you
closely observe the outputs, you will notice the differences. Stemmers behave differently
when it comes to words like possibly or provision . The stemmed outputs that are
obtained from the Lancaster stemmer are a bit obfuscated because it reduces the words a
lot. At the same time, the algorithm is really fast. A good rule of thumb is to use the
Snowball stemmer because it's a good trade off between speed and strictness.

# Converting words to their base forms using lemmatization
Lemmatization is another way of reducing words to their base forms. In the previous
section, we saw that the base forms that were obtained from those stemmers didn't make
sense. For example, all the three stemmers said that the base form of calves is calv, which is
not a real word. Lemmatization takes a more structured approach to solve this problem.
The lemmatization process uses a vocabulary and morphological analysis of words. <br>It
obtains the base forms by removing the inflectional word endings such as ing or ed. This
base form of any word is known as the lemma. If you lemmatize the word calves, you
should get calf as the output. One thing to note is that the output depends on whether the
word is a verb or a noun.

# Dividing text data into chunks
Text data usually needs to be divided into pieces for further analysis. This process is known
as chunking. This is used frequently in text analysis. The conditions that are used to divide
the text into chunks can vary based on the problem at hand. This is not the same as
tokenization where we also divide text into pieces.<br> During chunking, we do not adhere to
any constraints and the output chunks need to be meaningful.
When we deal with large text documents, it becomes important to divide the text into
chunks to extract meaningful information.

# Building a category predictor
A category predictor is used to predict the category to which a given piece of text belongs.
This is frequently used in text classification to categorize text documents. Search engines
frequently use this tool to order the search results by relevance. For example, let's say that
we want to predict whether a given sentence belongs to sports, politics, or science. To do
this, we build a corpus of data and train an algorithm. This algorithm can then be used for
inference on unknown data.<br>
In order to build this predictor, we will use a statistic called TermFrequency – Inverse
Document Frequency (tf-idf). In a set of documents, we need to understand the importance
of each word. The tf-idf statistic helps us understand how important a given word is to a
document in a set of documents.
