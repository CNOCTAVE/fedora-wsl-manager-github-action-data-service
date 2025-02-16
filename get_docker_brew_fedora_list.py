import os, sys
from subprocess import call

if len(sys.argv) < 2:
    print("Usage: %s <file>" % (os.path.basename(__file__)))
else:
    call(["/opt/vc/bin/tvservice", "-e", "DMT 87", "-p", "0x1c,0x46,0x5a,0x9d,0xa0"])