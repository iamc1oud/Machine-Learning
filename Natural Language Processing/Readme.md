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
