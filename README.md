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

`Huffman code algorithm:`

Huffman coding is a lossless data compression algorithm. In this algorithm, a variable-length code is assigned to input different characters. The code length is related to how frequently characters are used. Most frequent characters have the smallest codes and longer codes for least frequent characters.

Let`s also check time the Huffman code algorithm take to code data:

![](https://drive.google.com/uc?export=view&amp;id=1EBEEFbd49-MAE7-YlyjG2brOilURz4NB)


`LZ77 algorithm:`


LZ77 algorithms achieve compression by replacing repeated occurrences of data with references to a single copy of that data existing earlier in the uncompressed data stream. 

![](https://drive.google.com/uc?export=view&amp;id=1NLxpuI9qZ6hr7g_0TFAApwobM2lMcw0-)


You can see on the graph that the execution time of the compressed algorithm strongly depends on the size of the search block and the size of the front block. It can also be seen that with an increase in the size of the search block and the size of the front block, the amount of compression increases. You can achieve even greater compression if you increase the block sizes even more, but this will greatly affect the execution time.

