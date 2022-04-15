# BytePressor 

## v0.1.0 Details

This project is a lossless data compressing algorithm that uses 5 most used characters in a given piece of text as indexes. NOTE: vowels will be used in place for this for now <br />

This is possibly the most useless compression algorithm, as it will not support numbers or non-letter words. <br />

Then, for every character that is next to one of these 5 most used characters, it will be replaced with a single-byte character. The limit to the number of characters other than the 5 is 93. The reason for this is that there are only 94 useable single-byte characters to replace these <br />

e.g. "Hello this is a test case for my algorithm" <br />
In this case:  5 indexes are a,e,i,o,u...which gives: <br />
he, lo, hi, is, te, ca, se, fo, al, go, ri <br />
q   w   e   r   t   y   u   i   o   p   a  --- dummy references <br />

The result is: <br />
"qlw tes r a tst i opathm" <br />
And there you go, that will later be un-compressed.
