# Biological Sequence Analysis Web Application

This bioformatics web application is developed for research purpose only at this moment. The research work is related to biological DNA sequence analysis that mainly conducted by Chong Li Chuin who is researcher in bioformatics.


The application is developed by using Flask framework that written in python. The main function and process flow of the simple version web application as following: <br>

<ol>
   <li>User enter the input of the biological DNA sequence which is in <a href="https://en.wikipedia.org/wiki/FASTA">FASTA</a> format.</li>
   <li>The input data will be passed into generator in backend for slicing and process to generate the unique peptides.</li>
   <li>The generator will output a text file format to allow user download.</li>
</ol>


## Stack and libraries used
<ol>
  <li>Flask</li>
  <li>Biopython</li>
</ol>

This project can be further development by add on storing data features and also integrate with NCBI database through API key so that user can always retrive updated FASTA file based on the taxonomy ID.
