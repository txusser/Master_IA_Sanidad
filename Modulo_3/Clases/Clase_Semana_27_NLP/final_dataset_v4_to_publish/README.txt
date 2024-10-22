Introduction
These are the train, development and test sets of the CodiEsp corpus. Train, development and test have gold standard annotations. In addition, the unannotated background set is also distributed. All documents are released in the context of the CodiEsp track for CLEF ehealth 2020 (http://temu.bsc.es/codiesp/).

The CodiEsp corpus contains manually coded clinical cases. All documents are in Spanish language and CIE10 is the coding terminology (it is the Spanish version of ICD10-CM and ICD10-PCS). The CodiEsp corpus has been randomly sampled into three subsets: the train, the development, and the test set. The train set contains 500 clinical cases, and the development and test set 250 clinical cases each. CodiEsp participants must submit predictions for the test and background set, but they will only be evaluated on the test set.


Zip structure
Four folders: train, dev, test and background. Each one of them contains the files for the train, development, test and background corpora, respectively.
+ train, dev and test folders have:
	+ 3 tab-separated files with the annotation information relevant for each of the 3 sub-tracks of CodiEsp.
	+ A subfolder named text_files with the plain text files of the clinical cases.
	+ A subfolder named text_files_en with the plain text files machine-translated to English. Due to the translation process, the text files are sentence-splitted.
+ The background folder has only text_files and text_files_en subfolders with the plain text files.


Corpus format description
The CodiEsp corpus is distributed in plain text in UTF8 encoding, where each clinical case is stored as a single file whose name is the clinical case identifier. Annotations are released in a tab-separated file. Since the CodiEsp track has 3 sub-tracks, every set of documents (train and test) has 3 tab-separated files associated with it. 

For the sub-tracks CodiEsp-D and CodiEsp-P, the file has the following fields:
articleID	ICD10-code 

Tab-separated files for the sub-track CodiEsp-X contain extra fields that provide the text-reference and its position:
articleID	label	ICD10-code	text-reference	reference-position


Corpus summary statistics
The final collection of 1000 clinical cases that make up the corpus had a total of 16504 sentences, with an average of 16.5 sentences per clinical case. It contains a total of 396,988 words, with an average of 396.2 words per clinical case.

For more information, visit the track webpage: http://temu.bsc.es/codiesp/
