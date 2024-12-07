import threading
import time
import requests

def downloader(url, download_time):
    start = time.time()
    requests.get(url).json()
    end = time.time()
    download_time.append((url, end - start))

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    processes = []
    time_to_download = []
    for url in urls:
        process = threading.Thread(target=downloader, args=(url, time_to_download,  ))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
    
    for item in time_to_download:
        print(f"{item[0][37:]} took {round(item[1], 4)} seconds to download")


if __name__ == "__main__":
    main()
