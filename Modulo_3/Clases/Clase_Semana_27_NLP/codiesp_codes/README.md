#### Introduction
This compressed folder contains two files:

 + codiesp-D_codes.tsv: list of CIE10-Diagnósticos terms (2018 version) with their description in Spanish and in English.
 + codiesp-P_codes.tsv: list of CIE10-Procedimiento terms (2018 version) with their description in Spanish and in English. In addition, the list also contains the codes until the 4th axis, which are also used in the CodiEsp-P track due to annotation reasons.

A limited number of codes do not have English description because they were removed from the English version but maintained in the Spanish version of the terminology.

#### Format: 
Tab-separated file with 3 columns
code	es-description	en-description

#### Spanish to English description mapping:
For CodiEsp-D, the mapping to the English description was done through the files in the National Center for Health Statistics webpage: https://www.cdc.gov/nchs/icd/icd10cm.htm
Specifically, the file used was: ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2018/2018-ICD-10-CM-Codes-File.zip/icd10cm_codes_2018.txt

For CodiEsp-P, the mapping to the English description was done through the files in the Centers for Medicare Services webpage: https://www.cms.gov/Medicare/Coding/ICD10/2018-ICD-10-PCS-and-GEMs
Specifically, the file used was: 2018_icd10pcs_codes_file.zip/icd10pcs_codes_2018.txt
