#!/usr/env python

# decorator for saving arguments passed to a function 
# based on the presence of an environment variable
# ZP_DUMP.  includes regular and keyword args.
# saves args to a pickle file.


def save(f):
    def dumper(self, *args, **kwargs):
        import os
        if os.environ.get('ZP_DUMP', None):
            import pickle
            import time
            filetime = time.strftime('%H%M%S', time.localtime())
            fname = '_'.join((self.__class__.__name__,f.func_name,filetime))
            pkl_file = open(os.path.join('/tmp', fname + '.pickle') , 'w')
            arguments = []
            for count, thing in enumerate(args):
                arguments.append(thing)
            for name, value in kwargs.items():
                arguments.append('{}={}'.format(name,value))
            print 'writing {}'.format(fname)
            pickle.dump(arguments, pkl_file)
            pkl_file.close()
        return f(self, *args, **kwargs)
    return dumper


class foo(object):
    #@print_everything('foo', 'bar')
    @save
    def bar(self, x, y, z='bar'):
        print 'this is a test'

    def xyz(self):
        pass

x = foo()

x.bar(1, '2')
x.bar('abc', 'def', z='xyz')
x.bar([1, 2, 3], 'a')

