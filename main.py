import pandas as pd

keywords_df = pd.read_csv('keywordfile.csv')

article = """Add the article here"""

def count_keyword_occurrences(keyword, text):
    return text.lower().count(keyword.lower())

keywords_df['Count'] = keywords_df['Keyword'].apply(lambda kw: count_keyword_occurrences(kw, article))

keywords_df.to_csv('Output Sample Keywords For Hadi Demo-2.csv', index=False)

keywords_df
