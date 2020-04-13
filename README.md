# Project-2-data-pipelines

# Shark/human interactions

<p align="center">
 <img src="input/Image_1.jpg"/>
</p>

## Scope:

The aim of this project is to generate an automatic report with the Infection Trajectory of a particular country. Moreover, two infection trajectories of two different countries will be compared with regard a measure category, to get insight on which countries acted earlier against COVID-19. The purpose of introducing measures is preventing and delaying the spread of the virus so that large portions of the population aren’t sick at the same time.

## Source:

· Dataset URL: https://www.kaggle.com/barun2104/government-measures-to-combat-covid19
· API URL: 

## Description of the dataset:

COLUMNS:

Column name   | Description
------------- | -------------
ID                 | Unique ID
COUNTRY            | Country Name
ISO                | ISO 3 Country Code
ADMIN_LEVEL_NAME   | Administration Level Name, if available
PCODE              | Pin Code, if available
REGION             | Asia, Americas, Europe, Africa, Middle East, Pacific
LOG_TYPE           | Introduction / extension of measures
CATEGORY           | Health measures, Governance and socio-economic measures, Social distancing, Movement restrictions, Lockdown
MEASURE            | Specific measure
TARGETED_POP_GROUP | Whether the measure is targeted to a particular population group only
COMMENTS           | Extra comments about a particular measure
NON_COMPLIANCE     | Consequences if people don't comply with the measure
SOURCE             | Source type
LINK               | Link to the source
ENTRY_DATE         | Entry date for measure
Alternative source | Alternative source, if any

## Hipotheses:

1) The measures under analysis will be those **approved** to enter the country.

2) The columns of interest will be:
 - COUNTRY
 - ISO
 - REGION
 - CATEGORY
 - MEASURE
 - COMMENTS
 - SOURCE
 - ENTRY_DATE
 
 3) Some cleaning will be done to the original dataset:
 - Drop duplicates
 - Drop rows with higher number of null values
 - Filling Null Values
 - Correcting values in columns

 NOTE: The API used in this project provides information about the COVID evolution throughout time for a specific country. It requests a string paremeter with the country code in ISO 3166-1 alpha-2 format. For this reason, the ISO column will be modified to meet these requirements.

## To take into consideration

- If you download this code, some libraries are requied to execute it (smtplib, getpass, argparse, nbformat, plotly.graph_objects, among others.)

- Obtain help to run the program from command line: python3 main.py -h

- In main.py change **<from@gmail.com>** with your personal email. 

