def analyze_lzw():
  '''
  Function to measure time and build graphics of the LZW algorithm.
  '''
  data = open_file('text.txt')
  encoded = []
  decoded = []
  text = []
  number_of_ch = [i for i in range(100, 10000, 300)]
  for k in number_of_ch:
    string1 = data[:k]
    text.append(string1)

  for data in text:
    #Initialize the object of class Lzw:
    text_to_code = Lzw(data)

    #Measuring time of encoding:
    start1 = time.time()
    encoding = text_to_code.encode()
    end1 = time.time()
    time_encode = end1 - start1

    encoded.append(time_encode)

    #Measuring the time of decoding:
    start2 = time.time()
    decoding = text_to_code.decode(encoding)
    end2 = time.time()
    time_decode = end2 - start2
    decoded.append(time_decode)

  #Visualization of the result:
  #Encoding:
  x = encoded
  y = number_of_ch
  plt.scatter(x, y)
  plt.xlabel("Time to encode")
  plt.ylabel("Number of symbols")
  plt.title("LZW encoding")
  plt.show()
  
  #Decoding:
  x = decoded
  y = number_of_ch
  plt.scatter(x, y)
  plt.xlabel("Time to decode")
  plt.ylabel("Number of symbols")
  plt.title("LZW decoding")
  plt.show()
  return f'So we can see that time that LZW algorithm takes to decode and encode data almost linearly depends on the size of input data.'

print(analyze_lzw())

