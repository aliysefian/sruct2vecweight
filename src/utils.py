# -*- coding: utf-8 -*-
from time import time
import logging, inspect
import cPickle as pickle
from itertools import islice
import os.path

dir_f = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
folder_pickles = dir_f + "/../pickles/"


def return_path_struc2vec():
    return dir_f


def is_pickle(fname):
    return os.path.isfile(folder_pickles+ fname + '.pickle')


def chunks(data, size=10000):
    it = iter(data)
    for i in xrange(0, len(data), size):
        yield {k: data[k] for k in islice(it, size)}


def partition(lst, n):
    division = len(lst) / float(n)
    return [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in xrange(n)]


def restore_variable_from_disk(name):
    logging.info('Recovering variable...')
    t0 = time()
    val = None
    with open(folder_pickles + name + '.pickle', 'rb') as handle:
        val = pickle.load(handle)
    t1 = time()
    logging.info('Variable recovered. Time: {}m'.format((t1 - t0) / 60))

    return val


def save_variable_on_disk(f, name):
    logging.info('Saving variable on disk...' + folder_pickles + name + '.pickle')
    t0 = time()
    name_of_file = folder_pickles
    if not os.path.exists(name_of_file):
        os.makedirs(name_of_file)
    with open(folder_pickles + name + '.pickle', 'wb') as handle:
        pickle.dump(f, handle, protocol=pickle.HIGHEST_PROTOCOL)
    t1 = time()
    logging.info('Variable saved. Time: {}m'.format((t1 - t0) / 60))
    logging.info(f)

    return


def save_variable_on_disk_th(f, name, id):
    import main
    print (main.ss)
    logging.info('Saving variable on disk...' + folder_pickles + name + '.pickle')
    t0 = time()
    with open(folder_pickles + name + '.pickle', 'wb') as handle:
        pickle.dump(f, handle, protocol=pickle.HIGHEST_PROTOCOL)
    t1 = time()
    logging.info('Variable saved. Time: {}m'.format((t1 - t0) / 60))
    logging.info(f)

    return


def set_path(var):
    global folder_pickles
    folder_pickles = folder_pickles+str(var)+"/"
    return folder_pickles
