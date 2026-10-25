"""One place for the faster-whisper settings of every Level 4 draft checker (AGENTS.md section 4 and "Running audio locally").
Default: CPU, compute_type float32, cpu_threads 1 (int8 or several threads gives different text from run to run on a busy machine).
WHISPER_DEVICE=cuda runs it on an NVIDIA GPU (keep float32). faster-whisper has no Apple-GPU (MPS) backend: on a Mac it runs on the CPU."""
import os
from faster_whisper import WhisperModel
def model(name):
    return WhisperModel(name, device=os.environ.get('WHISPER_DEVICE', 'cpu'),
                        compute_type=os.environ.get('WHISPER_COMPUTE', 'float32'),
                        cpu_threads=int(os.environ.get('WHISPER_THREADS', '1')))
