import librosa as lr
from glob import glob

# Function to extract audio features from a single file

def breakStartAndEndChuck(audioFile, timeLength: int):
    """
    Breaks an audio file into three chunks: start, middle and end.
    Input: audioFile: path to audio file
            timeLength: length of each chunk in sec
    Output: startChunk, midChunk, endChunk
    """
    # load audio and sample rate into memory
    audio, sampleRate = lr.load(audioFile)
    # calculate number of samples in each chunk based on the timeLength
    chunkSamples = int(sampleRate * timeLength)
    # calculate total number of chunks
    totalChunks = len(audio) // chunkSamples
    # print(f"Total chunks: {totalChunks}")
    # split the audio file into chunks using python's slice operator

    if totalChunks == 0:
        raise Exception("Audio file is too short.")
    startChunk = audio[:chunkSamples]
    midChunk = audio[chunkSamples:-chunkSamples]
    endChunk = audio[-chunkSamples:]

    return startChunk, midChunk, endChunk


if __name__ == "__main__":
    timeStamp = 10 #in millisec (10 seconds)
    audioFile = "test.mp3"
    try:
        startChunk, midChunk, endChunk = breakStartAndEndChuck(audioFile, timeStamp)
    except Exception as e:
        if repr(e) == "Audio file is too short.":
            print("Audio file is too short.")