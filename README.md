# Welsh Summarisation Dataset
This repo holds the Welsh Summarisation Dataset and Python demo scripts and notebooks. It is being actively updated at the moment, so keep watching the space.

### Dataset
This is a collection of 513 Welsh texts (Wikipedia articles) and their summaries. Each of the articles - containing at least 500 tokens in length - was extracted along with its Wikipedia summary using the [WikipediaAPI](https://pypi.org/project/Wikipedia-API/). The raw files - containing the Wikipedia extracted articles and summaries as is - are available in [data.zip](data) in html and plain text formats and licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. The Python scripts for accessing the extracted and processed files can be viewed and used with [this colab file](dataset.ipynb) with the usage instruction as described below.

### Usage
For the dataset usage example, you can open [the notebook](dataset.ipynb) in Google Colab and by clicking the [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UCREL/welsh-summarisation-dataset/blob/main/dataset.ipynb)] run the following scripts.
- First clone the repository
```python
!git clone https://github.com/UCREL/welsh-summarisation-dataset.git
```
- Then import pickle and change directory to the cloned folder
```python
import os
import pickle as pkl
os.chdir('/content/welsh-summarisation-dataset')
```
- Then load the dataset file into memory
```python
with open('./data/dataset.pkl', "rb") as dataset_file:
  dataset = pkl.load(dataset_file)
```
- Check the first five rows of your dataset with `.head()`
```python
dataset.head()
```

![Dataset Screenshot](https://github.com/UCREL/welsh-summarisation-dataset/blob/main/img/dataset_screenshot.JPG?raw=true)

### Demo
Here is the link to [a simple demo](https://share.streamlit.io/ignatiusezeani/welsh-text-summarizer/main/streamlit/app.py) of the Welsh Text Summarisation tool.
[![Demo Screenshot](./img/demo_screenshot.JPG)](https://share.streamlit.io/ignatiusezeani/welsh-text-summarizer/main/app/app.py)

### Paper(s):
- **Introducing the Welsh Summarisation Dataset and Baseline Systems** (Submitted to LREC2022)


### Contacts
- [Ignatius Ezeani](https://github.com/IgnatiusEzeani)
- [Mahmoud El-Haj](https://github.com/drelhaj)
- [Jon Morris](https://github.com/jonmorris83)
- [Dawn Knight](https://github.com/DawnKnight-Cardiff)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
