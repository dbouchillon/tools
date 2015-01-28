import os
import sys
import zipfile
import shutil

def mymain(argv):
  print 'Extracting kerberos.so from {0}'.format(argv[0])
  zp_egg = zipfile.ZipFile(argv[0])
  dest = os.path.join(os.environ['ZENHOME'], 'lib','python','kerberos.so')
  zp_egg.extract('ZenPacks/zenoss/Microsoft/Windows/lib/kerberos_el6/kerberos.so')
  zp_egg.close()
  print 'Copying kerberos.so to {0}'.format(dest)
  shutil.copy('ZenPacks/zenoss/Microsoft/Windows/lib/kerberos_el6/kerberos.so', dest)
  os.remove('ZenPacks/zenoss/Microsoft/Windows/lib/kerberos_el6/kerberos.so')

if __name__ == '__main__':
  mymain(sys.argv[1:])
