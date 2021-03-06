# Workflows for Computer-Assisted Language Comparison

@data-background:#f5f5f7
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---
@data-background:#f5f5f7
@style:text-align:center;
@style:font-size:100%;

## <font color = '#5b687c'>Workflows for Computer-Assisted Language Comparison</font>
----

<p style="text-align:center;color:#7687a1;font-weight:bold;font-size:110%;">State of the Art</p>
<p style="text-align:center">
<img src="img/calc-yinyang.png" alt="image" style="width:200px"></img>
</p>

<aside class='notes'>
Hello everyone, thanks for inviting me. I am Mei-Shin and I would like to introduce the workflows for computer-assisted language comparison.
</aside>
---
## @head:"Introduction"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/edictor-tutorial/calc-7.png" alt="img" style="width:1000px;text-align:center;"></img>
</p>

<aside class="notes">
Before I introduce our workflow in detail, I want to
explain quickly what we mean when talking about
“computer-assisted language comparison”.
</aside>
--
## @head:"Introduction"
### @subhead:"The Gap between Computational and Traditional Historical Linguistics"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/ba-talk/background-5-addon.jpg" alt="img" style="width:700px;text-align:center;"></img>
<aside class="notes">
The comparative method has been the key method of
historical linguistics since the 19th century. Originally,
it was applied to the Indo-European languages,
developed by scholars like R[ʁ]asmus R[ʁ]ask and Jacob
Grimm.
</aside>
--
## @head:"Introduction"
### @subhead:"The Gap between Computational and Traditional Historical Linguistics"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/ba-talk/background-11.jpg" alt="img" style="width:700px;text-align:center;"></img>

<aside class="notes">
Since then, it has been applied to many other language
families.
</aside>

--
## @head:"Introduction"
### @subhead:"The Gap between Computational and Traditional Historical Linguistics"
<p style='text-align:center'>
<img src = "http://lingulist.de/documents/talks/img/ba-talk/background-12.jpg" style='width:700px;text-align:center'></img>
</p>
<aside class='notes'>
But our knowledge of the history of most of these
language families is still rather fuzzy.
</aside>

--
## @head:"Introduction"
### @subhead:"The Gap between Computational and Traditional Historical Linguistics"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/calc-project/calc-5.jpg" style='width:900px;text-align:center'></img>
</p>
<aside class='notes'>
The reason is that the comparative method is very
tedious to apply. Also, comparing with computers, human lack of consistency and efficiency.
However, human annotation can achieve a high accuracy and a high
flexibility.

Computational methods, on the other hand, are by
nature consistent and efficient, but they lack accuracy
and flexibility.
</aside>

--
## @head:"Introduction"
### @subhead:"Computer-Assisted Disciplines"

<p style="text-align:center">
<img src="http://lingulist.de/documents/talks/img/calc-project/calc-7.jpg" style='width:900px;text-align:center'></img>
</p>

<aside class='notes'>
This calls for a new framework of computer-assisted
language comparison, following the idea in many
computer-assisted disciplines. By combining the
efforts, we can get the best of two worlds, the
efficiency of computers, and the accuracy of humans.
</aside>

--
## @head:"Introduction"
### @subhead:"Computer-Assisted Disciplines"

To allow humans and machines to work together successfully, it is important that:

* our data is both human- and machine-readable,
* we follow transparent guidelines when handling linguistic datasets,
* we offer interfaces that allow humans and machines to access the data at the same time.

<aside class='notes'>
The basic idea behind <b>computer-assisted</b> as opposed
to <b>computer-based</b> language comparison is to allow
scholars to do qualitative and quantitative research at
the same time.
</aside>

---
## @head:"CALC workflows"
### @subhead:"Overview"

<p style='text-align:center'>
<img src='img/HillList.png' style='width:700px;text-align:center'></img>
</p>

<aside class='notes'>
Our workflows for computer-assisted language
comparison have so far been intensively tested on a
small set of 8 Burmish languages, which we
investigated in collaboration with Nathan Hill, who
was responsible for the qualitative investigation of
the data and for the common discussion of new
computer-assisted methods which were then
implemented by Mattis List.

Our experience with this Burmish project allows us to
set up this workflow that starts from raw data to the
explicit identification of correspondence patterns
across multiple languages. At the moment, List and
Hill develop the workflow further to account also for
(semi)-automatic reconstructions, but in this talk, only
the identification of correspondence patterns will be
discussed.
</aside>

--
## @head:"CALC workflows"
### @subhead:"Details of the workflows"
<p style="text-align:center">
<img src="img/calc-workflow.png" alt="img" style="width:600px;text-align:center;"></img>
</p>
<aside class='notes'>
This picture presents the full workflow, it comprises 5
different processes at this moment, in which we
successively lift linguistic data from their raw form
up to a level where correspondence patterns across
cognate words have been automatically identified and
can be qualitatively inspected by the scholars.
Some technical terms on this picture may look
unfamiliar to you, but the ideas behind these
applications are actually being practiced by linguists
for quite some time already. In the following, we will
discuss these ideas in detail, and you find even more
detailed information in the handout accompanying
this talk.
</aside>
--
## @head:"CALC workflows"
### @subhead:"Materials and methods"

<p style ='text-align:center'>
<img src ='img/languages.png' style="width:500px"></img>
</p>

<ul >
<li style='font-size:70%'> Chén 陳其光 (2012). Miao and Yao language. 苗瑤语文</li>
<li style='font-size:70%'> 25 Hmong-Mien languages in the original (10 in our selection)</li>
<li style='font-size:70%'> 885 concepts in the original (313 in our selection, compatible with the Burmish Etymological dictionary project)</li>
</ul>

<aside class='notes'>
The data we use to illustrate our workflow was
originally collected by 陳其光, and later added in
digital form to the Wiktionary project.
Chén's collection of <b>frequent terms</b> comprises 885
different concepts translated into 25 varieties of
Hmong-Mien. In this talk, we extract 10 Hmong-Mien
languages for the demonstration, and the map here
presents the geographical locations of these
languages.
</aside>


--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
<p style='text-align:center'>
<img src="img/raw-machine.png" style="width:800px" alt="img"></img>
</p>

<aside class='notes'>
The first step is to convert raw data to a machine
readable format. I will try to explain in detail, what
this means.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
<p style='text-align:center'>
<img src="img/chen-illustration.png" style="width:800px" alt="img"></img>
</p>

<aside class="notes">
To see in detail, what this means, let’s have a look at
one exemplary page from Chén’s book, with the data,
as it has been prepared by the SEALANG project.
We can see that the data is essentially the same, but
that the rows and columns of the tabular form have
been swapped.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"

<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
     \t Baheng,east \t Baheng, west \t Qiandong, east \t Qiandong, wesst
七   \t  tsha³¹,tsjung⁴⁴ \t tshang⁴⁴    \t     shung⁵³    \t      shung²²
月亮 \t la⁰³lha⁵⁵ \t ʔa⁰³lha⁵⁵ \t la⁴⁴la⁴⁴ \t pau¹¹la³³
星星 \t la⁰³qang³⁵ \t qa⁰³qang³⁵ \t qei²⁴qei²⁴ \t tei⁴⁴qei⁴⁴
</div>

<aside class='notes'>
The problem of this type of data is that it is difficult to
interpret for a computer. This is because it contradicts
one fundamental principle of data organization: one
cell in a table should have only one kind of value.
But in the tables in Chen’s data, we can often see
multiple values in a cell, and often they are there to
indicate that a language has two or more expressions
for the same concept. They then separate these
synonyms by some character, a comma, a colon, a dot,
or a pipe. <b>(action)</b> This may look okay for humans, but
it will confuse any computer method, as the method
cannot guess what the human wants to say here.

(action is to type , ; and | in the cell)
</aside>

--
@class:scrollable
<div class="spreadsheet" data-delimiter="\t" style="width:1200px;height:600px;text-align:center;">
 ID \t DOCULECT        \t CONCEPT \t ENGLISH \t VALUE         \t FORM \t TOKENS \t NOTE
 1  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsja³¹     \t        \t
 2  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsjung⁴⁴    \t        \t variant
 2  \t Baheng, west    \t 七      \t SEVEN   \t tsjang⁴⁴      \t tsjang⁴⁴      \t        \t
 3  \t Qiandong, east  \t 七      \t SEVEN   \t sjung⁵³       \t sjung⁵³       \t        \t
 4  \t Qiandong, wesst \t 七      \t SEVEN   \t sjung²²       \t sjung²²       \t        \t
 5  \t Baheng, east    \t 月亮    \t MOON    \t la⁰³lha⁵⁵     \t la⁰³lha⁵⁵     \t        \t
 6  \t Baheng, west    \t 月亮    \t MOON    \t ʔa⁰³lha⁵⁵     \t ʔa⁰³lha⁵⁵     \t        \t
 7  \t Qiandong, east  \t 月亮    \t MOON    \t la⁴⁴la⁴⁴      \t la⁴⁴la⁴⁴      \t        \t
 8  \t Qiandong, wesst \t 月亮    \t MOON    \t pau¹¹la³³     \t pau¹¹la³³     \t        \t
 9  \t Baheng, east    \t 星星    \t STAR    \t la⁰³qang³⁵    \t la⁰³qang³⁵    \t        \t
 10 \t Baheng, west    \t 星星    \t STAR    \t qa⁰³qang³⁵    \t qa⁰³qang³⁵    \t        \t
 11 \t Qiandong, east  \t 星星    \t STAR    \t qei²⁴qei²⁴    \t qei²⁴qei²⁴    \t        \t
 12 \t Qiandong, wesst \t 星星    \t STAR    \t tei⁴⁴qei⁴⁴    \t tei⁴⁴qei⁴⁴    \t        \t
</div>

<aside class="notes">
We transform the wide format to a so-called longtable
format, which looks redundant at first sight, but
is the most easy-to-make way to provide data that is
machine-readable.
Each entry in this format consists of a unique id, a
language name (Doculect), a concept identifier (if it’s
not English then you can translate it into English), and
a value. The value is the original entry we find in the
source. This value is then further split, if it contains a
comma, and we add the other entry to the FORM
column. In this way, we can consistently handle
synonyms, but also keep track of the original data.

Now, the form is not yet computer-readable. Linguists
would not simply compare the word forms, but
computers don’t know what one sound is, and how the
sounds should be interpreted.
For this reason, we have to segment the data for the
computer, so the methods know which symbols form
one sound. We do this by adding spaces.
The most straightforward way is to segment by hand.
(action) But if we are dealing with hundreds of entries, it is
better to do this automatically.
(action is to type : )
tsja³¹ → tɕ (U+0255)a ³(U+00b3)¹(U+00b9) → tɕ a ³¹
ʔ (U+0294)
⁵ (U+2075)
⁴ (U+2074)
lh (U+026C)
ng(U+014b)


</aside>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
We recommend *Orthography Profiles* as a way to:

<ul>
<li> Convert arbitrary input data to IPA: </li>
  <ul style="list-style-type:none;">
    <li> tsj   ---->  tɕ </li>
    <li> ng    ---->   ŋ </li>
  </ul>
<li>And to segment the input data:</li>
   <ul style="list-style-type:none;">
      <li> tsja³¹  ----> tɕa³¹ ----> tɕ  a ³¹<li>
   </ul>
</ul>

<aside class="notes">
We recommend to use Orthography Profiles to
convert all kinds of transcriptions to consistent IPA
and segment the data at the same time.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
<div class="spreadsheet" data-delimiter="\t" style="width:100px;height:600px;text-align:center;">
Grapheme \t IPA
č        \t tʃ
ž        \t dʒ
th       \t tʰ
dh       \t d̤
sh       \t ʃ
a        \t a
aa       \t aː
tsj	 \t tɕ
la	 \t l a
</div>

<aside class="notes">
An orthography profile is nothing else than a table, in
which you list the combination of characters in the
original transcription in the first column, and how it
should be converted in a second column.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From raw data to machine-readable data"
@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t CONCEPT \t ENGLISH \t VALUE           \t FORM       \t TOKENS              \t COGIDS
 1  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsja³¹     \t tɕ a ³¹             \t
 2  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsjung⁴⁴   \t tɕ u ŋ ⁴⁴           \t
 3  \t Baheng, west    \t 七      \t SEVEN   \t tsjang⁴⁴        \t tsjang⁴⁴   \t tɕ a ŋ ⁴⁴           \t
 4  \t Qiandong, east  \t 七      \t SEVEN   \t sjung⁵³         \t sjung⁵³    \t ɕ u ŋ ⁵³            \t
 5  \t Qiandong, wesst \t 七      \t SEVEN   \t sjung²²         \t sjung²²    \t ɕ u ŋ ²²            \t
 6  \t Baheng, east    \t 月亮    \t MOON    \t la⁰³lha⁵⁵       \t la⁰³lha⁵⁵  \t l a ³/⁰ + ɬ a ⁵⁵    \t
 7  \t Baheng, west    \t 月亮    \t MOON    \t ʔa⁰³lha⁵⁵       \t ʔa⁰³lha⁵⁵  \t ʔ a ³/⁰ + ɬ a ⁵⁵    \t
 8  \t Qiandong, east  \t 月亮    \t MOON    \t la⁴⁴la⁴⁴        \t la⁴⁴la⁴⁴   \t l a ⁴⁴ + l a ⁴⁴     \t
 9  \t Qiandong, wesst \t 月亮    \t MOON    \t pau¹¹la³³       \t pau¹¹la³³  \t p ɔ ¹¹ + l a ³³     \t
 10 \t Baheng, east    \t 星星    \t STAR    \t la⁰³qang³⁵      \t la⁰³qang³⁵ \t l a ³/⁰ + q a ŋ ³⁵  \t
 11 \t Baheng, west    \t 星星    \t STAR    \t qa⁰³qang³⁵      \t qa⁰³qang³⁵ \t q a ³/⁰ + q a ŋ ³⁵  \t
 12 \t Qiandong, east  \t 星星    \t STAR    \t qei²⁴qei²⁴      \t qei²⁴qei²⁴ \t q ei ²⁴ + q ei  ²⁴  \t
 13 \t Qiandong, wesst \t 星星    \t STAR    \t tei⁴⁴qei⁴⁴      \t tei⁴⁴qei⁴⁴ \t t ei - ⁴⁴ + q ei ⁴⁴ \t
</div>

<aside class="notes">
And once we applied the profile, our data looks like
this. Note that the plus-sign here indicates, that the
word consists of two morphemes.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

<p style='text-align:center'>
<img src="img/machine-partial.png" style="width:800px" alt="img"></img>
</p>
<aside class="notes">
Now, we come to the second stage, in which we try to
infer partial cognates from our segmented words.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

<p style='text-align:center'>
<img src="img/partialcg.png" style="width:800px" alt="img"></img>
</p>

<aside class="notes">
Compounding is an important element of word
formation in South-East Asian languages. The
presence of compound words challenges the notion
that words can either be cognate or not. This picture
shows an example of words for “moon” in 4 Sinitic
languages, the words that should be cognates are
marked in the same color. For example, ŋuoʔ5, ŋiat5,
ȵy21, yɛ51 are all cognate with each other. But
Meixian has another morpheme which means “light”
in Mandarin Chinese, and Wenzhou has two
morphemes kuɔ35 vai13 after the moon morpheme.
If we allow words only to be cognate or not, we
probably should say that we have four different
cognates here.
To account for partial cognates in our data, we use a
different annotation schema. In this schema, we assign
each morpheme a cognate ID, and if two morphemes
have the same ID, they are thus meant to be cognate.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

<p align="middle"><img src="http://lingulist.de/documents/talks/img/calc-project/algo2.jpg" style="width:800px;align:middle;"></img></p>
<p style='text-align:center;font-size:60%;'>List et al. (2016). Using sequence similarity networks to identify partial cognates in multilingual wordlists. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Vol. 2, pp. 599-605).</p>

<aside class="notes">
With the method by Mattis List et al., proposed in
2016, we have a rather simple and efficient approach
to automatically search for cognates in linguistic
datasets.
Although the algorithm is not very complex, it would
go too far to explain the details here, I am afraid, and
therefore, I will only show this nice graph, that
illustrates the different stages, and tell you that the
core idea is to model the data with help of networks.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From segmented words to computer-inferred cognates"

@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t CONCEPT \t ENGLISH \t VALUE           \t FORM         \t TOKENS              \t COGIDS
 1  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsja³¹      \t tɕ a ³¹             \t 3
 2  \t Baheng, east    \t 七      \t SEVEN   \t tsja³¹,tsjung⁴⁴ \t tsjung⁴⁴    \t tɕ u ŋ ⁴⁴           \t 3
 3  \t Baheng, west    \t 七      \t SEVEN   \t tsjang⁴⁴        \t tsjang⁴⁴    \t tɕ a ŋ ⁴⁴           \t 3
 4  \t Qiandong, east  \t 七      \t SEVEN   \t sjung⁵³         \t sjung⁵³     \t ɕ u ŋ ⁵³            \t 3
 5  \t Qiandong, wesst \t 七      \t SEVEN   \t sjung²²         \t sjung²²     \t ɕ u ŋ ²²            \t 3
 6  \t Baheng, east    \t 月亮    \t MOON    \t la⁰³lha⁵⁵       \t la⁰³lha⁵⁵   \t l a ³/⁰ + ɬ a ⁵⁵    \t 1908 1907
 7  \t Baheng, west    \t 月亮    \t MOON    \t ʔa⁰³lha⁵⁵       \t ʔa⁰³lha⁵⁵   \t ʔ a ³/⁰ + ɬ a ⁵⁵    \t 1909 1907
 8  \t Qiandong, east  \t 月亮    \t MOON    \t la⁴⁴la⁴⁴        \t la⁴⁴la⁴⁴    \t l a ⁴⁴ + l a ⁴⁴     \t 1908 1907
 9  \t Qiandong, wesst \t 月亮    \t MOON    \t pau¹¹la³³       \t pau¹¹la³³   \t p ɔ ¹¹ + l a ³³     \t 1910 1907
 10 \t Baheng, east    \t 星星    \t STAR    \t la⁰³qang³⁵      \t la⁰³qang³⁵  \t l a ³/⁰ + q a ŋ ³⁵  \t 1874 1870
 11 \t Baheng, west    \t 星星    \t STAR    \t qa⁰³qang³⁵      \t qa⁰³qang³⁵  \t q a ³/⁰ + q a ŋ ³⁵  \t 　1872 1870
 12 \t Qiandong, east  \t 星星    \t STAR    \t qei²⁴qei²⁴      \t qei²⁴qei²⁴  \t q ei ²⁴ + q ei  ²⁴  \t 　1872 1870
 13 \t Qiandong, wesst \t 星星    \t STAR    \t tei⁴⁴qei⁴⁴      \t tei⁴⁴qei⁴⁴  \t t ei - ⁴⁴ + q ei ⁴⁴ \t 　1871 1870
</div>

<aside class='notes'>
If we apply this method to our data, we get results that
look as follows. All words are given cognate IDs by
the algorithm, depending on how many morphemes
they have, and if the IDs are identical, this means the
algorithm judges the words to be cognate.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

<p style='text-align:center'>
<img src="img/partial-alignment.png" style="width:800px" alt="img"></img>
</p>

<aside class="notes">
In the third stage, we want to align the cognates we
detected.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

<p align="middle"><img src='img/alignment.png' style="width:400px;align:middle;"></img></p>

Phonetic alignment techniques are well-known in historical linguistics and have been applied for quite some time now.

<aside class="notes">
Phonetic alignment techniques are well-known in
historical linguistics and have been applied for quite
some time now. As the figure shows here, cognate
words (here all meaning “seven”) are arranged into a
matrix so that corresponding segments are placed in
the same column. This is essential to identify sound
correspondences. Nowadays, we have stable
algorithms for multiple alignments that yield accuracy
scores almost comparable to the differences we would
expect between human annotators only, and we also
have web-based tools that facilitate manual
alignments greatly. This picture, for example, is taken
from the EDICTOR application, and I will show you
how to work with this tool in the last section. But
even if this helps to save some time, it is still tedious
to correct alignments manually.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

We propose *Template-Based Alignments* as an alternative to semi-automatically computed alignments.

* Languages with a rather restricted syllable structure can usually be aligned in a very consistent way by simply using a template.
* A typical Chinese syllable, for example, consists of *initial*, *medial*, *nucleus*, *coda* and *tone* (Wang 1996). Once we know the individual template of a Chinese word, we can easily align it with any other word, as long as we know the template.
<aside class='notes'>
We propose Template-Based Alignments as an
alternative to semi-automatically computed
alignments.
The major idea is, that languages with a rather
restricted syllable structure can usually be aligned in a
very consistent way by simply using a template.
A typical Chinese syllable, for example, consists of
*initial*, *medial*, *nucleus*, *coda* and *tone*
(Wang 1996). Once we know the individual template
of a Chinese word, we can easily align it with any
other word, as long as we know the template.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

<p align="middle"><img src='img/templates.png' style="width:1000px;align:middle;"></img></p>

<aside class='notes'>
Here is an example for this workflow, provided we
know the template for the words in our data. We start
from the tokens, and we use the Structure column to
provide information on the template. Now we use a
meta-template of the general syllable structure of the
languages, and then we drop all those columns, where
we do not find a sound.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

<p align="middle"><img src='img/orthotemplate.png' style="width:600px;align:middle;"></img></p>
<aside class='notes'>
The problem is of course, how to make the templates
for the words in our data? Here, we can again use
orthography profiles, along with a variant in which we
can provide rudimentary context, here expressed by
the circumflex symbol for the beginning of a word,
and the dollar sign for the end. We just add another
column, and in this column we provide the structure,
the template, for the given sub-sequence. You find
more information in the handout.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From cognates to alignments"

@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t ENGLISH \t TOKENS             \t STRUCTURE \t ALIGNMENT \t COGIDS
 1   \t Baheng, east   \t SEVEN   \t tɕ a ³¹             \t i n t     \t tɕ a - ³¹ \t 3
 2   \t Baheng, west   \t SEVEN   \t tɕ a ŋ ⁴⁴           \t i n c t   \t tɕ a ŋ ⁴⁴ \t 3
 3   \t Qiandong, east \t SEVEN   \t ɕ u ŋ ⁵³            \t i n c t   \t  ɕ u ŋ ⁵³ \t 3
 4   \t Qiandong, wesst\t SEVEN   \t ɕ u ŋ ²²            \t i n c t   \t ɕ u ŋ ²²  \t 3
 5   \t Baheng, east   \t MOON    \t l a ³/⁰ + ɬ a ⁵⁵    \t i n t + i n t \t l a ³/⁰ + ɬ a ⁵⁵\t 1908 1907
 6   \t Baheng, west   \t MOON    \t ʔ a ³/⁰ + ɬ a ⁵⁵    \t i n t + i n t \t ʔ a ³/⁰ + ɬ a ⁵⁵ \t 1909 1907
 7   \t Qiandong, east \t MOON    \t l a ⁴⁴ + l a ⁴⁴    \t i n t + i n t \t l a ⁴⁴ + l a ⁴⁴ \t 1908 1907
 8   \t Qiandong, wesst\t MOON    \t p ɔ ¹¹ + l a ³³    \t i n t + i n t \t p ɔ ¹¹ + l a ³³ \t 1910 1907
 9   \t Baheng, east   \t STAR    \t l a ³/⁰ + q a ŋ ³⁵ \t i n t + i n c t \t l a ³/⁰ + q a ŋ ³⁵ \t 1874 1870
 10  \t Baheng, west   \t STAR    \t q a ³/⁰ + q a ŋ ³⁵ \t　i n t + i n c t \t q a ³/⁰ + q a ŋ ³⁵ \t 1872 1870
 11  \t Qiandong, east \t STAR    \t q ei ²⁴ + q ei  ²⁴ \t　i n t + i n t \t q ei ²⁴ + q ei - ²⁴ \t  1872 1870
 12  \t Qiandong, wesst\t STAR    \t t ei - ⁴⁴ + q ei ⁴⁴\t　i n t + i n t \t t ei - ⁴⁴ + q ei - ⁴⁴\t 1871 1870
</div>
<aside class='notes'>
The output file then has two more columnes which is
called “Alignment” and “Structure”.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

<p style='text-align:center'>
<img src="img/alignment-strict.png" style="width:800px" alt="img"></img>
</p>

<aside class='notes'>
We are almost done, we now need to infer the strict
cross-semantic cognates from the data.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

* For a realistic analysis, we need to identify cognates not only within the same meaning slot, but across different concepts.
* However, our algorithm for automatic congate detection designed to search words with the same meaning.
* Therefore, we need to find *cross-semantic* partial (=normal) cognates in a second stage.

<aside class='notes'>
For a realistic analysis, we need to identify cognates
not only within the same meaning slot, but across
different concepts.
However, our algorithm for automatic congate
detection designed to search words with the same
meaning.
Therefore, we need to find cross-semantic partial
(=normal) cognates in a second stage.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

* For this task, we employ a new algorithm to <i>merge</i> cognates in our data into larger groups.
* The basic idea is to check if two alignments are compatible with each other, and to fuse them to form a bigger alignment, if this is the case.
* As a side effect, all words we identify in this way are <i>strictly</i> cognate, since our procedure does not allow to identify a morpheme in the same language to be cognate if this does not show the exact same form.

<aside class='notes'>
For this task, we employ a new algorithm to merge
cognates in our data into larger groups.
The basic idea is to check if two alignments are
compatible with each other, and to fuse them to form a
bigger alignment, if this is the case.
As a side effect, all words we identify in this way are
strictly cognate, since our procedure does not allow to
identify a morpheme in the same language to be
cognate if this does not show the exact same form.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

<!--<font color="red">add an illustrational graphic here, that shows how alignments that are compatible can be merged</font>-->

<p style='text-align:center'>
<img src="img/cross-semantic-picture.png" style="width:800px" alt="img"></img>
</p>
<aside class='notes'>
Here are some examples for the morphemes we found
in the data, which recur in different words.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

<p style='text-align:center'>
<img src="img/cross-semantic-table.png" style="width:800px" alt="img"></img>
</p>

<aside class='notes'>
Here we give another example to show you how
actually it is done. I would like to draw your attention
to the 東黔東 language. The tei²⁴ in Son and tei²⁴ in
Daughter were not in the same first analysis, in the
“cognacy” column, but now, after our analysis, in the
cross-semantic column, the algorithm found them to
be related, because the word is identical internally,
and our test with strict alignments accepted
this.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From alignments to strict, cross-semantic cognates"

@class:scrollable
<div class="spreadsheet" data-delimiter="\t" data-width="100" fontsize="12">
ID  \t DOCULECT        \t ENGLISH \t TOKENS             \t STRUCTURE \t ALIGNMENT \t CROSSIDS            \t COGIDS
 1   \t Baheng, east   \t SEVEN   \t tɕ a ³¹             \t i n t     \t tɕ a - ³¹ \t 3                  \t 3
 2   \t Baheng, west   \t SEVEN   \t tɕ a ŋ ⁴⁴           \t i n c t   \t tɕ a ŋ ⁴⁴ \t 3                  \t 3
 3   \t Qiandong, east \t SEVEN   \t ɕ u ŋ ⁵³            \t i n c t   \t  ɕ u ŋ ⁵³ \t 3                  \t 3
 4   \t Qiandong, wesst\t SEVEN   \t ɕ u ŋ ²²            \t i n c t   \t ɕ u ŋ ²²  \t 3                  \t 3
 5   \t Baheng, east   \t MOON    \t l a ³/⁰ + ɬ a ⁵⁵    \t i n t + i n t \t l a ³/⁰ + ɬ a ⁵⁵\t 1908 351 \t 1908 1907
 6   \t Baheng, west   \t MOON    \t ʔ a ³/⁰ + ɬ a ⁵⁵    \t i n t + i n t \t ʔ a ³/⁰ + ɬ a ⁵⁵ \t 41 351	\t 1909 1907
 7   \t Qiandong, east \t MOON    \t l a ⁴⁴ + l a ⁴⁴    \t i n t + i n t \t l a ⁴⁴ + l a ⁴⁴ \t 1908 351 \t 1908 1907
 8   \t Qiandong, wesst\t MOON    \t p ɔ ¹¹ + l a ³³    \t i n t + i n t \t p ɔ ¹¹ + l a ³³ \t 1910 351  \t 1910 1907
 9   \t Baheng, east   \t STAR    \t l a ³/⁰ + q a ŋ ³⁵ \t i n t + i n c t \t l a ³/⁰ + q a ŋ ³⁵ \t 1874 1834 \t 1874 1870
 10  \t Baheng, west   \t STAR    \t q a ³/⁰ + q a ŋ ³⁵ \t　i n t + i n c t \t q a ³/⁰ + q a ŋ ³⁵ \t 1872 1834 \t 1872 1870
 11  \t Qiandong, east \t STAR    \t q ei ²⁴ + q ei  ²⁴ \t　i n t + i n t \t q ei ²⁴ + q ei - ²⁴ \t  1872 1834 \t 1872 1870
 12  \t Qiandong, wesst\t STAR    \t t ei - ⁴⁴ + q ei ⁴⁴\t　i n t + i n t \t t ei - ⁴⁴ + q ei - ⁴⁴\t 1234 1834 \t 1871 1870
</div>
<aside class='notes'>
And this is, how this all looks in our table. You cannot
see many differences here, but you can see that the
morphemes in MOON have been added to other sets
of morphemes, and we generally find a lot of crosssemantic
cognates in our data.
</aside>
--
<p style='text-align:center'>
<img src="img/strict-soundcorrespondence.png" style="width:800px" alt="img"></img>
</p>
<aside class='notes'>
We can now start to search for sound correspondence
patterns.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From strict cognates to sound correspondence patterns"

<p style="text-align:center">
<img src="img/sound-correspondence-classic.png" alt="img" style="width:900px;text-align:center;"></img>
</p>

<aside class='notes'>
Most linguists are probably familiar with this kind of
representation: Clackson shows, how sound
correspondence patterns are distributed over the Indo-
European languages.
But if we look at tables like this one, there are several
problems. <b>We don’t know the frequency of the
occurrence of each of the patterns, we do not know
the number of cognates in each individual
language, or the context, in which they occur. </b>
This makes it quite difficult to learn from text-books,
but also to criticize a theory and to try to improve it.
</aside>

--
## @head:"CALC workflows"
### @subhead:"From strict cognates to sound correspondence patterns"
<p style="text-align:center">
<img src="img/ratliff2010.png" alt="img" style="width:600px;text-align:center;"></img>
</p>

<p style='text-align:center;font-size:60%;'>Ratliff et al. (2010). Hmong-Mien language history. Pacific Linguistics (Page 57)</p>

<aside class='notes'>
A better example is provided by Martha Ratliff’s
study on Hmong-Mien in 2010. This table shows us
the cognate sets she used in the study, so in a way, it’s
more transparent than the previous example. But there
are remain some problems:
(1) the table does not provide the full words in the
examples, but only the morphemes
(2) the table does not provide us with information on
the degree to which patterns are inconsistent,
reflecting secondary variation in the individual
languages
(3) the representation is only to some degree machine-readable,
not only because it is not digitized, but also
because we do not know completely to which
correspondence pattern (or set) each of the other
sounds in the data belongs, and we will have problems
to check the consistency of entire words when given
the data in this form.
</aside>
--
## @head:"CALC workflows"
### @subhead:"From strict cognates to sound correspondence patterns"

<p style="text-align:center">
<img src="img/edictor-hn.png" alt="img" style="width:600px;text-align:center;"></img>
</p>

<aside class='notes'>
In our proposal for the handling of sound
correspondence patterns, we propose a different format, and specifically an interactive way of
inspecting patterns, along with an automatic analysis
by which the patterns can be inferred in a first place.
The result of this automatic analysis is like a table, in
which languages are placed in the columns, and
correspondence patterns are placed in rows, with each
cell indicating for each individual correspondence
pattern, which reflex sound a given language shows
for this pattern. In this format, everything can be
traced back to the original data, no data is “missing”
It’s also interactive, which I will demonstrate soon.
</aside>
--
## @head:"Illustration of the Workflow"
### @subhead:"From Raw Data to Segmented Data"
<a style="color:#2d1f23;text-align:center" href='http://calc.digling.org/profile/'> http://calc.digling.org/profile/</a>
--
## @head:"Illustration of the Workflow"
### @subhead:"EDICTOR"
<p>EDICTOR: a web-based tool to edit, analyse, and publish etymological data.</p>
<p style="text-align:center">
<a style="color:#2d1f23" href='http://edictor.digling.org/' align='middle'><img src='img/edictor.png' width=300px></img></a>
</p>

---
## @head:"Conclusion and outlook"
<img src="img/outlook.jpg" alt="img" style="width:900px;text-align:center;"></img>

--
## @head:"Conclusion and outlook"
### @subhead:"Discussion"

Possible improvements:

<ul>
<li>Semi-automatic reconstruction (currently tested by Nathan Hill and Johann-Mattis List).</li>
<li>Clearer integration of automatic and semi-automatic methods in the workflows.</li>
<li>Enhancing the visualization of the results (Xun Gong is working on this for the Burmish Etymological Dictionary project).</li>
</ul>


--
## @head:"Conclusion and outlook"
### @subhead:"Discussion"

Challenges:

<ul>
<li>Lexical reconstruction: how can we reconstruct whole words?</li>
<li>Sound change: can we represent all changes from a proto-form along some phylogeny along with sound laws?</li>
</ul>

---

<p style="font-size:100px;color:#768ca0;text-align:center;font-weight:bold;">
Thanks for Your Attention!

<p>CALC members:</p>
<ul>                        
<li> Dr. Johann-Mattis List (Group Leader)</li>    
<li> Dr. Yunfan Lai (Post-Doc)</li>
<li> Dr. Tiago Tresoldi (Post-Doc)</li>
<li> Nathanael E.Schweikhard (Doctoral student)</li>
<li> Mei-Shin Wu (Doctoral student)</li>
</ul>
