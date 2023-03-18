def evaluate_lz77(filename: str):
        """
        Function for evaluating Lz 77
        """
        text_sizes = [1000, 5000,10000]
        offsets = [(10, 10), (100, 100),(300,300),(500,500)]
        times=[]
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().split("\n")
        for size in text_sizes:
            for offset in offsets:
                start1 = time.time()
                compressor = Lz77("".join(text[:size]), offset[0], offset[1])
                compressor.lz77_encode()
                end1 = time.time()
                time_encode = end1 - start1
                assert compressor.decodelz77() == "".join(text[:size])
                print(f"{str(compressor.count_compressing())}% стиснення для таких блоків ({offset[0]} ,{offset[1]}), для такого розміру {size}")
                times.append((size, time_encode))
        times = numpy.array(times)
        x = times[:, 1]
        y = times[:, 0]
        plt.scatter(y, x)
        plt.ylabel("Time to encode")
        plt.xlabel("Number of lines of text")
        plt.title("LZ77 encoding")
        plt.show()
evaluate_lz77("text.txt")
