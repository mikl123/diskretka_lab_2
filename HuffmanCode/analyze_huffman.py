def analyze_huffman():
    '''
    Function to measure time and build graphics of Huffman algorithm.
    '''
    encoded = []
    decoded = []
    text = []
    number_of_ch = [i for i in range(100, 100000, 1000)]
    data = open_file('text.txt')
    for k in number_of_ch:
        string1 = data[:k]
        text.append(string1)
    for data in text:
        start1 = time.time()
        to_code = HuffmanCode(data)
        prob = to_code.calculate_frequency()
        code = to_code.encode_start(prob)
        encode = to_code.encode()
        end1 = time.time()
        time_to_encode = end1 - start1
        encoded.append(time_to_encode)

    #Visualization of the result:
    #Encoding:
    x = encoded
    y = number_of_ch
    plt.scatter(x, y)
    plt.xlabel("Time to encode")
    plt.ylabel("Number of symbols")
    plt.title("Huffman encoding")
    plt.show()

    return 'So we can see that time that Huffman code algorithm takes\
 to encode data also almost linearly depends on the size of input data. '

print(analyze_huffman())
