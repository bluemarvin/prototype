import sys, getopt, glob, os

nameCache = {}

def write(out, files):
  for name in files:
    try:
      src = open(name, 'r')
    except IOError:
      print 'Failed to open file: ' + name + ' for writing'
      sys.exit()
    attrName, ext = os.path.splitext(os.path.basename(name))
    if not attrName in nameCache:
      nameCache[attrName] = True
      out.write("shaders['" + attrName + "'] = {};\n")
    out.write("item = shaders['" + attrName + "'];\n")
    out.write("item" + ext + "file = '" + name + "';\n")
    out.write("item" + ext + " = ''\n")
    line = src.readline()
    while line:
      out.write("  + '" + line.rstrip('\n') + "\\n'")
      line = src.readline()
      if line:
        out.write('\n')
      else:
        out.write(';\n\n')

def main(argv):
  path = ''
  ofile = ''
  try:
    opts, args = getopt.getopt(argv,"hp:o:")
  except getopt.GetoptError:
    print sys.arg[0] + ' -p <path> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print sys.arg[0] + ' -p <path> -o <outputfile>'
      sys.exit()
    elif opt == '-p':
      path = arg
    elif opt == '-o':
      ofile = arg
  vp =  glob.glob(path + '/*.vp')
  fp =  glob.glob(path + '/*.fp')

  print 'Input directory is "' + path + '"'

  if len(vp) == 0:
    print 'No vertex programs found'
  if len(fp) == 0:
    print 'No fragment programs found'
  if len(vp) == 0 and len(fp) == 0:
    sys.exit()

  print 'Output file is "' + ofile + '"'

  try:
    out = open(ofile, 'w')
  except IOError:
    print 'Failed to open file: ' + ofile
    sys.exit()

  out.write('//\n')
  out.write('// *** WARNING: DO NOT EDIT. THIS FILE IS AUTO GENERATED. ***\n')
  out.write('//\n')
  out.write('// source files can be found in: ' + path +'\n')
  out.write('//\n\n')
  out.write('var shaders = exports || {};\n')
  out.write('var item;\n\n')
  out.write('// Vertex Programs\n');
  write(out, vp)
  out.write('// Fragment Programs\n');
  write(out, fp)

if __name__ == "__main__":
   main(sys.argv[1:])
