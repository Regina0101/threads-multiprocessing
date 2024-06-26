import logging
from multiprocessing import Pool, cpu_count

def factorize_number(number):
    logging.info(f'Starting factorization for {number}')
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    logging.info(f'Finished factorization for {number}')
    return factors

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(processName)s - %(message)s')

    numbers = [128, 255, 99999, 10651060]

    logging.info('Starting parallel factorization')
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(factorize_number, numbers)
    logging.info('Finished parallel factorization')

    a, b, c, d = results

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    logging.info('All tests passed.')
