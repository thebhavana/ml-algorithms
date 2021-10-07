## FIND-S ALGORITHM

* It is concept learning algorithm in machine learning. It finds the most specific hypothesis that fits all the positive training examples. 
* The algorithm contains only positive training examples. 
* The specific hypothesis fills in all the important details about the variables given in the general hypothesis. 
* S={'phi','phi','phi','phi',.....,'phi'}
* The algorithm imports data from .csv file.

### ALGORITHM

* Step1 : Initialize h to the most specific hypothesis.
* Step2 : For each positive training instance x  
  * For each attribute contraint ai in h  
  * If the constraint ai is satisfied by x  
  * then do something 
  * Else  
  * Replace ai in h by the next more general constraint that is satisfied by x
* Step3 : Output the hypothesis in h.
