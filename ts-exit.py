#!/usr/bin/env python3
import subprocess
import sys

# Location of the Tailscale cli.  This was set as an alias in the
# USER space, therefore must call the application as such.
application = '/Applications/Tailscale.app/Contents/MacOS/Tailscale'

def enable(location):
    # tailscale set --accept-dns
    subprocess.run([application, 'set', '--accept-dns'])
    # tailscale set --exit-node ''
    subprocess.run([application, 'set', '--exit-node', location])

def disable():
    # tailscale set --exit-node ''
    subprocess.run([application, 'set', '--exit-node', ''])
    # tailscale set --accept-dns=false
    subprocess.run([application, 'set', '--accept-dns=false'])

def main():
    if len(sys.argv) >= 2:
        argv = sys.argv[1:]
        for i, v in enumerate(argv):
            # Lower all the argv's to compare and contrast
            argv[i] = v.lower()
        if '--connect' in argv: # on --connect command get server and connect
            enable(argv[argv.index('--connect') + 1])
        elif '--disconnect' in argv:
            disable()
        elif '--list' in argv: # Get the list of exit-nodes
            subprocess.run((application, 'exit-node', 'list'))
    else:
        print("Missing paramters:")
        print("{} --connect (location)".format(sys.argv[0]))
        print()
        print("or")
        print()
        print("{} --disconnect".format(sys.argv[0]))
        sys.exit(1)

if __name__ == "__main__":
    main()
