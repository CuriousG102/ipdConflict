ipdConflict
===========

An application to process data on resources from disparate resources and consolidate it into a more helpful format

Plan for Automating Collection of Resource-Conflict Data

Resources and Output
  Final Doc - Data to Fill:
  	•	Resource (e.g. Cement, Coal, Cobalt)
  	•	Mine Type (industrial or artisanal) - USER INPUT
  	•	Location Name
  	•	Standard measure (e.g. metric ton)
  	•	Annual location capacity in standard measure
  	•	January price per unit for year of yearbook (from World Bank historical price data)
  	•	Yearly location value - CALCULATE
  	•	Capacity of location in kilograms - CALCULATE
  	•	Price per kilogram - CALCULATE
  	•	Longitude & Latitude (Geonames) - Will likely need user help
  	•	Precision Code - Will likely need user help

Google Doc - USGS Yearbook - Data to Scrape:
	•	Resource
	•	Location Name
	•	Annual capacity
	•	Standard measure

Google Doc - World Bank Commodity - Data to Scrape:
	•	January price per unit for year of yearbook for each resource

Geonames API - Data to secure:
	•	Lat & Long of location name
	•	Precision of lat & long

Application Architecture
Goals:
	•	Automate tasks as much as possible, requiring user input less often
	•	Minimize amount of time spent needing to code
	•	Heavily lean on Google Docs for storing, accessing, and writing data. Use the Spreadsheets API and avoid the requirement of devising your own data management scheme
Method:
	•	Use MVC to build out this application. The model should have full fledged accessor and mutator methods so that it can be entirely independent. All other aspects of the program should be subject to improvement. This should also allow a quick and dirty prototype before considering more difficult or time consuming interfaces
  	⁃	  Model
  	  ⁃	  Primary key is an arbitrary number (will likely be sequentially assigned but I have no desire to provide guarantees to view and controller)
  	  ⁃	  Full fledged class model takes care of data processing, but all locations likely won’t be instantiated at once. Long term storage will occur in google doc output. Users will be warned not to modify original output file or intermediate files until the program is done processing.
  	⁃	  View
  	  ⁃	  Iteration 1: Google Doc Spreadsheet final output provides all necessary view features. During intermediate processing, Google Docs are also the means by which people issue clarifications to the program. 
  	⁃	  Controller
  	  ⁃	  Iteration 0: Controller is person’s own computer, running Python program. This eliminates security concerns in a big way. They are asked for all things that are needed, e.g. password and username, names of initial files, names of intermediates
  	  ⁃	  Iteration 1: Controller is a Django powered webpage. The user gives access to their google docs, selects the ones they need, and works through webpage
