# Discrete Laboratory work #2

Work was done by Team 17: Михайло Булешний та Сумик Марта

In this laboratory work we`ve realized four algorithms of compression: LZ77, LZW, Huffman code and Deflate.

Distribution of our work:
- LZW: Marta Sumyk
- LZ77: Mykhailo Byleshnyi
- Huffman and Deflate: together

The below diagram shows all the classes that we`ve implemented:


![](https://drive.google.com/uc?export=view&amp;id=1LXUwFFCaPwKSdnFY5I7t48EQRri-aqUx)

`LZW algorithm:`

LZW is a 'dictionary-based' lossless compression algorithm that scans a file for data patterns that appear more than once. In this way compression of files that have many string that repeats is much more effective.

Let`s measure the time LZW algorithm takes based on different length of input string.

To do this we`ll randomly generate strings with length from 100 to 10000 with step 300 from the book 'Introduction to algorithms' by Thomas Cormen.

The below graphics ilustate time of endoding and decoding of LZW:

![](https://drive.google.com/uc?export=view&amp;id=1Wdjy35WKhzvA0RvCpLCiGFXS3mOxbYBQ)

![](https://drive.google.com/uc?export=view&amp;id=1zkBqhJChDAiUn4hWK8Goj7XN8zedfLsp)


So we can see that time that LZW algorithm takes to decode and encode data almost linearly depends on the size of input data.
