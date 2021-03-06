# POP!   --- Burst your Bubble

This past election has made it abundantly clear that we live in very isolated bubbles, reinforced by social media like Facebook and Twitter. At this point, it seems like there is little base of shared knowledge on which to have political discussion. Since the election, there has been a lot of talk of not only blatantly fake news, but the much more pervasive and insidious *biased news*. Visualizations like the Wall Street Journal’s [Red vs. Blue Facebook feed](http://graphics.wsj.com/blue-feed-red-feed/) highlight how different both sides see the world.
 
Until election day, many didn’t even realize how isolated we are. Well, we think it’s time to *pop* our bubbles.

### We introduce the POP chrome extension

The POP chrome extension can track what news articles you’ve been reading and automatically detect if they are biased left or right. Over time, POP can help you keep tabs on how one-sided the news you’ve been reading is.

### Powered by PopAI, the artificial intelligence that detects bias in your news reading behavior

In the past 48 hours, we had our PopAI read thousands of news articles from different news sources. By looking at millions of words and analyzing the context in which they’re used, PopAI now understands the meaning of words. Given a news article, it has learned to extract its meaning and predict bias. If the news article contains images, PopAI’s bias prediction is augmented by a Clarifai model trained to detect political bias in images.
 
PopAI combines the power of deep learning for text analysis with Clarifai's cutting-edge computer vision technology.

## Start POPing Your Bubble!
 
You can install the POP chrome extension from the [Chrome Web Store](https://chrome.google.com/webstore/category/extensions). Once installed, you can start saving the articles you read by clicking on the extension button in your browser. The extension will also open a side panel showing stats on your reading pattern.

## Technical Details

### Data
 
We trained PopAI with multiple data sources. News articles from the Guardian, we scraped using the Guardian API and news articles from biased news sources we obtained from the [fake news Kaggle challenge](https://www.kaggle.com/mrisdal/fake-news)
 
### Machine Learning Pipeline
 
We used [Exponential Family Embeddings](https://github.com/mariru/exponential_family_embeddings) to extract semantic features of the vocabulary words. Embeddings are a powerful unsupervised text analysis technique that helps cope with the curse of dimensionality. Discrete representations of text are mapped into a continuous embedding space, which captures the semantics of the text.
 
For each news article we then extract a feature vector, by averaging the word embeddings of the words that appear in the article.
 
The article features are then fed into a neural network which predicts whether an article is biased towards the left towards the right or unbiased.
 
The PopAI training pipeline is implemented in [tensorflow](http://tensorflow.org/), and scales to big data.

### Backend - Django Web Framework

### Frontent - Chrome Extension
