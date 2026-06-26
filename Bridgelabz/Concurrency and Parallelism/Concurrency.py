import threading
def download(url):
    print('Downloading:', url)

if __name__ == '__main__':
    t1 = threading.Thread(target=download, args=('https://www.python.org',))
    t2 = threading.Thread(target=download, args=('https://www.google.com',)) 
    t1.start()
    t2.start()
    t1.join()
    t2.join() 


import asyncio
async def read_file(filename):
    print('Reading file:', filename)
    await asyncio.sleep(1)  
    print('Finished reading:', filename)

async def main():
    await asyncio.gather(read_file('file1.txt'), read_file('file2.txt'))
asyncio.run(main()) 