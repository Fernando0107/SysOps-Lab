import logging
import threading
import time
import numpy as np   
import multiprocessing

Z = [None] * 10

def generateZ(mat, indexes):
    """
    Function to generate Z with formula Z = X + Y
    
    """
    for idx in indexes:
        Z[idx] = mat[0][idx] + mat[1][idx]
        time.sleep(1)

if __name__ == "__main__":
    #-----------------------------------------------------------#
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


    #-----------------------------------------------------------#

    logging.info("Start program with no use of threads")
    logging.info("Main    : Before generating inicial matrix")
    matrix = np.random.randint(1,100, size=(2,10))
    #print(matrix)

    t1_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    logging.info("Main    : before creating thread")
    t1 = threading.Thread(target=generateZ, args=(matrix, t1_indexes))
    t1.start()
    t1.join()

    matrix = np.vstack([matrix, Z])
    print(matrix)
    logging.info("Main    : Finished generating Z for matrix")
    print()
    #-----------------------------------------------------------#
    
    logging.info("Start program using 2 threads")
    logging.info("Main    : Before generating inicial matrix")
    matrix = np.random.randint(1,100, size=(2,10))

    t1_indexes = [0,1,2,3,4]
    t2_indexes = [5,6,7,8,9]
    t_indexes = [t1_indexes, t2_indexes]
    threads = list()

    for index in range(2):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=generateZ, args=(matrix, t_indexes[index]))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    matrix = np.vstack([matrix, Z])
    print(matrix)
    logging.info("Main    : Finished generating Z for matrix")
    
    print()
    #-----------------------------------------------------------#


    logging.info("Start program using 5 threads")
    logging.info("Main    : Before generating inicial matrix")
    matrix = np.random.randint(1,100, size=(2,10))

    t1_indexes = [0,1]
    t2_indexes = [2,3]
    t3_indexes = [4,5]
    t4_indexes = [6,7]
    t5_indexes = [8,9]
    t_indexes = [t1_indexes, t2_indexes, t3_indexes, t4_indexes, t5_indexes]
    threads = list()

    for index in range(5):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=generateZ, args=(matrix, t_indexes[index]))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    matrix = np.vstack([matrix, Z])
    print(matrix)
    logging.info("Main    : Finished generating Z for matrix")

    #-----------------------------------------------------------#