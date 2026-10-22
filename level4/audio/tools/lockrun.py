"""Run one command while holding an exclusive lock on a lock file (same idea as `flock LOCKFILE cmd ...`, but works on macOS too,
which has no flock command). Only one Chatterbox or Whisper process may run at a time.  Usage: python lockrun.py LOCKFILE cmd [args...]"""
import fcntl, subprocess, sys
with open(sys.argv[1], 'a') as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    sys.exit(subprocess.call(sys.argv[2:]))
