import pandas as pd

keywords_df = pd.read_csv('Sample Keywords For Hadi Demo-2.csv')

article = """
Hyperwrite ensures my personal resources are being routed to where they’re needed the most. Yes, I still struggle with Writer’s Block. I think that’s a given in this industry that I’ve chosen. But trust me, streamlining the technical details of the writing process helps a ton.
With a powerful AI assistant doing most of the heavy lifting during content ideation, research, and information organization, it’s so much easier to stay focused and inspired on the task.

"""

def count_keyword_occurrences(keyword, text):
    return text.lower().count(keyword.lower())

keywords_df['Count'] = keywords_df['Keyword'].apply(lambda kw: count_keyword_occurrences(kw, article))

keywords_df.to_csv('Output Sample Keywords For Hadi Demo-2.csv', index=False)

keywords_df
