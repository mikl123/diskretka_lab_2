def evaluate_deflate():
        text_sizes = [10000,20000,50000,100000]
        times=[]
        for size in text_sizes:  
            start1 = time.time()
            text_generated=str(''.join(random.choices(string.ascii_lowercase + string.digits, k = size)))
            compressor = Deflate(text_generated)
            compressor.encode()
            end1 = time.time()
            time_encode = end1 - start1

            assert compressor.decode() == text_generated
            print(f"{str(compressor.compare_compression())}% стиснення для таких блоків (100 ,100), для такого розміру {size}")
            times.append((size, time_encode))
        times = numpy.array(times)
        x = times[:, 1]
        y = times[:, 0]
        plt.scatter(y, x)
        plt.ylabel("Time to encode")
        plt.xlabel("Number of symbols of text")
        plt.title("Deflate encoding")
        plt.show()
evaluate_deflate()
