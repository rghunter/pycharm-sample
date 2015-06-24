import reverse_geocoder as rg
from concurrent.futures import ThreadPoolExecutor

def main():
    rg.RGeocoder()
    executor = ThreadPoolExecutor(max_workers=2)

    future = executor.submit(threadRun)
    print future.result()



def threadRun():
    Boston = (42.359502, -71.062282)
    result = rg.search(Boston)
    return result


if __name__ == '__main__':
    main()