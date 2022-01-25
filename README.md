# Welsh Summarisation Dataset
This repo holds the Welsh Summarisation Dataset and Python demo scripts and notebooks. It is being actively updated at the moment, so keep watching the space.

### Dataset
This is a collection of 513 Welsh texts (Wikipedia articles) and their summaries. Each of the articles - containing at least 500 tokens in length - was extracted along with its Wikipedia summary using the [WikipediaAPI](https://pypi.org/project/Wikipedia-API/). The raw files - containing the Wikipedia extracted articles and summaries - are stored in [data.zip](data) in html and plain text formats. The processed files are placed in a pickled pandas dataframe [dataset.pkl](data) which can be viewed with [this colab file](dataset.ipynb).

![Dataset Screenshot](https://github.com/UCREL/welsh-summarisation-dataset/blob/main/img/dataset_screenshot.JPG?raw=true)
### Usage

### Demo
Here is the link to [a simple demo](https://share.streamlit.io/ignatiusezeani/welsh-text-summarizer/main/streamlit/app.py) of the Welsh Text Summarisation tool.
[![Demo Screenshot](./img/demo_screenshot.JPG)](https://share.streamlit.io/ignatiusezeani/welsh-text-summarizer/main/streamlit/app.py)

### Paper(s):
- **Introducing the Welsh Summarisation Dataset and Baseline Systems** (Submitted to LREC2022)


### Contacts
- [Ignatius Ezeani](https://github.com/IgnatiusEzeani)
- [Mahmoud El-Haj](https://github.com/drelhaj)
- [Jon Morris](https://github.com/jonmorris83)
- [Dawn Knight](https://github.com/DawnKnight-Cardiff)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
