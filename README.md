yourgrind
=========


Name Sanitisation
=================


Steps

* Read CVS from file, line by line.
* Convert each line so every chr is lower case.
* Parse first name.
  * Check for "-", "\s", "&" chrs for double barrel names, multi word names and 
  the few noted & chrs in the by hand scan through.
  * Capitalise the first chr of each of the first name words, get the first name
  words by using a string split.
  
* Parse second name
  * Check for '-', '&', "'", split on these
  * Split on "\s", check that first word is not in ["von","de",....], otherwise
  capitilise.
  * Check that the first part of the name is not mc, if it is, capitilise 
  appropriately.
  
  
  
  
Shipping and Billing Barcodes
=============================
**Best to use two barcodes, one for billed, the other for shipped**


Steps

* Design barcode:
    1. Identifier for shipped or billed at the start of the barcode
    2. Unique identifier based on DB values, eg user ID, order number, etc.
* Create barcode with something like: https://pypi.python.org/pypi/pyBarcode/
  
* Barcode Parser
  * can use something like: http://zbar.sourceforge.net/ to read the code.
  * Read code, switch on shipping/billed identifier
  * Update database, dependant on the switch.
