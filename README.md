# Luis:
Contribution concerns gathering and processing all articles and relevant data that was not published by the authors due to copyright.

The URLs were used to manually gather article's data along side tools such WayBackMachine (http://web.archive.org/). These articles are stored in the **1-raw-articles** directory, each paragraph as an individual line. A manual approach was necessary due to small variations between the article text (on the original web page) and the text the authors employed in their work. For example titles, subtitles, descriptions and captions, may or may not have been included. Making webscrapers not worth it. Additionally, some articles may have been updated since the authors conducted their work, hence the use of tools like WayBackMachine to try and get the correct article version.

After manually extracting articles, annotaions were split according to their corresponding articles (`process_annotations.py`). The raw articles were then split into individual sentences with the help of a SpaCy NLP model (done by the spacy parse component of the model, `process_sentences.py`) as well as a semi-manual approach (`check_sentences.py`) to handle any edge cases, where sentences did not correctly align with respective code_mentions in the their corresponding annotations.csv file. (All python files above can be found in X-utils). This step processes articles in the **2-matched** directory. Articles in this directory are grouped by event and then by orientation. Each event, orientation sub-directory  has 2 files ending in *"_annotaions.csv"* and *"_sent.txt*" created by the `process_annotations.py` and `process_sentences.py` scripts respectively, and may contain an additional file `edit_annotaions.py` if the sentence index needed to be adjusted in the *"_annotaions.csv"* (for example if there is a missing or extra sentence in the relevant *"_sent.txt*" file).

Note on how files were created and processed in the 2-matched:
- Running the `process_annotations.py`script creates **all** *"_annotaions.csv"* for each respective article in the **1-raw-articles** directory. It also creates the desired directory structure *event_{event_id} > orientation_{orientation_id}*.
- A new directory called **process_article** was created.
- I Copy and pasted a single article in the **process_article** directory, making sure that this was the only article in the directory (although `process_sentences.py` could be modified to included functionality involving processing multiple files)
- Running the `process_sentences.py` script will create the *{event_id}_{orientation_id}_sent.txt* file in the relevant event, orientation sub-directory.
- Check *{event_id}_{orientation_id}_sent.txt*, manually adjust any sentences that were not correctly split by the nlp sentensizer.
- Run `check_sentences.py` (when processing articles individually adjust the event_id (0-9) and orientation_id (LL, L M, R, RR) to match the article in question in the top most for loops). use the output to correct any simple mistakes. Create and run a edit_annotations file if needed.
- Repeat for all articles


# NewsWCL50
NewsWCL50 is the first, open access evaluation dataset for methods seeking to identify bias by word choice and labeling.

The dataset consists (besides some additional files such as the readme you are currently reading) of the following files:

| Name        | Description  | 
| ------------- |-------------|
| `Annotations.csv` | The annotations that we coded during the manual, deductive content analysis. The start and end columns represent the annotation's position as to the original text document in number of tokens. |
| `Codebook.pdf` | The codebook used to conduct the final deductive content analysis. |
| `urls.tsv` | Links each article to its URL so that you can gather the full text if you need to. |

For more information on the dataset, please have a look at our [paper](https://www.gipp.com/wp-content/papercite-data/pdf/hamborg2019a.pdf).

## CoNLL format for CDCR
To access the part of the dataset parsed for cross-document coreference resolution (CDCR) in CoNLL and JSON format with access to the full articles, please refer to this repository of [the diverse CDCR datasets](https://github.com/anastasia-zhukova/Diverse_CDCR_datasets). 

## Gathering the original news articles
NewsWCL50 only contains the annotated parts of the news articles. Due to copyright law, we cannot offer the original articles. However, you can quickly gather the original articles, if you need to work not only with our annotations but also the remainder of the text. In the file [urls.tsv](urls.tsv), each row represents a single article, identified uniquely by its event id, publisher id, and URL. For each article, visit that URL and copy the article's text, including the headline, into a text document. 

## How to cite
Please cite our [paper](https://www.gipp.com/wp-content/papercite-data/pdf/hamborg2019a.pdf) if you are using NewsWCL50:
```
@InProceedings{Hamborg2019a,
  author    = {Hamborg, Felix and Zhukova, Anastasia and Gipp, Bela},
  title     = {Automated Identification of Media Bias by Word Choice and Labeling in News Articles},
  booktitle = {Proceedings of the ACM/IEEE Joint Conference on Digital Libraries (JCDL)},
  year      = {2019},
  month     = {Jun.},
  location  = {Urbana-Champaign, USA}
}
```

You can find more information on this and other news projects on our [website](https://www.isg.uni-konstanz.de/projects/media-bias-analysis/).

## License
Licensed under the Attribution-ShareAlike 4.0 International (the "License"); you may not use NewsWCL50 except in compliance with the License. A copy of the License is included in the project, see the file [LICENSE](LICENSE).

Copyright 2018-2019 The NewsWCL50 team
