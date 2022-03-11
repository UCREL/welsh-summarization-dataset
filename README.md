# Set ddata’r Adnodd Creu Crynodebau
### Welsh Summarisation Dataset

Mae'r ystorfa hon yn cynnwys set ddata’r Adnodd Crynhoi Crynodebau a sgriptiau arddangos a llyfrau nodiadau Python. Mae'n cael ei diweddaru ar hyn o bryd, felly cofiwch gael golwg arni’n gyson.

### Set Ddata (Dataset)
Dyma gasgliad o 513 o destunau Cymraeg (erthyglau Wicipedia) a'u crynodebau. Tynnwyd pob erthygl – sydd yn cynnwys o leiaf 500 tocyn o ran hyd – ynghyd â'i grynodeb Wicipedia gan ddefnyddio [WikipediaAPI](https://pypi.org/project/Wikipedia-API/). Mae'r ffeiliau crai – sy'n cynnwys yr erthyglau a’r chrynodebau a dynnwyd o Wikipedia fel ag y maent yn ymddangos yno – ar gael ar ffurf [data.zip](data) mewn fformatau html a thestun plaen ac maent wedi'u trwyddedu o dan <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Drwydded Ryngwladol Creative Commons Attribution 4.0</a>. Gellir gweld y sgriptiau Python ar gyfer cyrchu'r ffeiliau a dynnwyd ac a broseswyd, a'u defnyddio gyda'r [ffeil ar y cyd](dataset.ipynb) hon a gellir gweld hefyd y cyfarwyddiadau ar sut i’w defnyddio, fel y maent wedi’u disgrifio isod.

*This is a collection of 513 Welsh texts (Wikipedia articles) and their summaries. Each of the articles - containing at least 500 tokens in length - was extracted along with its Wikipedia summary using the [WikipediaAPI](https://pypi.org/project/Wikipedia-API/). The raw files - containing the Wikipedia extracted articles and summaries as is - are available in [data.zip](data) in html and plain text formats and licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. The Python scripts for accessing the extracted and processed files can be viewed and used with [this colab file](dataset.ipynb) with the usage instruction as described below.*


### Defnydd (Usage)
Ar gyfer sampl o’r defnydd a wnaed o’r set ddata, gallwch agor y llyfr nodiadau yn Google Colab, a thrwy glicio [] cyn mynd ati i ddilyn y cyfarwyddiadau canlynol.


- Yn gyntaf, cloniwch yr ystorfa (*First clone the repository*)
```python
!git clone https://github.com/UCREL/welsh-summarisation-dataset.git
```
- Yna mewngludwch pickle a newid y cyfeiriadur i'r ffolder sydd wedi'i glonio (*Then import pickle and change directory to the cloned folder*)
```python
import os
import pickle as pkl
os.chdir('/content/welsh-summarisation-dataset')
```
- Yna llwythwch y ffeil set ddata i'r cof (Then load the dataset file into memory)
```python
with open('./data/dataset.pkl', "rb") as dataset_file:
  dataset = pkl.load(dataset_file)
```
- Nodwch bum rhes gyntaf eich set ddata gyda `.head()` (*Check the first five rows of your dataset with* `.head()`)
```python
dataset.head()
```
![Dataset Screenshot](https://github.com/UCREL/welsh-summarisation-dataset/blob/main/img/dataset_screenshot.JPG?raw=true)

### Arddangosiad (Demo)
- Dyma’r ddolen i [arddangosiad syml](https://share.streamlit.io/ignatiusezeani/welsh-text-summarizer/main/streamlit/app.py) o’r adnodd Crynhoi Testunau Cymraeg.
- *Here is the link to [a simple demo](https://share.streamlit.io/ignatiusezeani/welsh-text-summarizer/main/streamlit/app.py) of the Welsh Text Summarisation tool.
[![Demo Screenshot](./img/demo_screenshot.JPG)](https://share.streamlit.io/ignatiusezeani/welsh-text-summarizer/main/app/app.py)*

### Papurau (Papers):
- Ezeani, I., El- Haj, M.A., Morris, J. a Knight, D. (2022). **Cyflwyno Adnodd Crynhoi Setiau Data Cymraeg, a Systemau Sylfaenol (Introducing the Welsh Summarisation Dataset and Baseline Systems)**. Trafodaethau o Gynhadledd Gwerthuso Adnoddau Iaith (LREC) 2022, Mehefin 2022, Marseille, Ffrainc. [*Proceedings of the LREC (Language Resources Evaluation) 2022 Conference, June 2022, Marseille, France.*] (IF ACCEPTED)

- Morris, Jonathan, Ignatius Ezeani, Ianto Gruffydd, Katharine Young, Lynne Davies, Mahmoud El-Haj a Dawn Knight. 2022. **Creu crynodebau awtomatig o destunau Cymraeg (Welsh automatic text summarisation)**. Symposiwm Academaidd Technolegau Iaith Cymru 2022. Prifysgol Bangor, 28 Ionawr 2022. [*Wales Academic Symposium on Language Technologies 2022, Bangor University, 28 January 2022.*]

- Morris, Jonathan, Ignatius Ezeani, Ianto Gruffydd, Katharine Young, Lynne Davies, Mahmoud El-Haj a Dawn Knight. Forth. **Creu crynodebau awtomatig o destunau Cymraeg (Welsh automatic text summarisation)**. Yn dod.  Iaith a Thechnoleg yng Nghymru: Cyfrol II, gol. D. Prys. Bangor: Canolfan Bedwyr. [*Language and Technology in Wales: Volume II, ed. D. Prys. Bangor: Canolfan Bedwyr.*]

### Cysylltiadau (Contacts)
- [Ignatius Ezeani](https://github.com/IgnatiusEzeani)
- [Mahmoud El-Haj](https://github.com/drelhaj)
- [Jon Morris](https://github.com/jonmorris83)
- [Dawn Knight](https://github.com/DawnKnight-Cardiff)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
- Mae'r gwaith hwn wedi'i drwyddedu o dan <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Drwydded Ryngwladol Creative Commons Attribution 4.0.</a>.
- This work with all the accompanying resources is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
