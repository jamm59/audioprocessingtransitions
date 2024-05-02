import librosa as lr
from glob import glob

# Function to extract audio features from a single file

def breakStartAndEndChuck(audioFile, timeLength: int):
    """
    """
    audio, sampleRate = lr.load(audioFile)

    chunkSamples = int(sampleRate * timeLength)

    totalChunks = len(audio) // chunkSamples

    print(f"Total chunks: {totalChunks}")


    startChunk = audio[:chunkSamples]
    print(len(startChunk))
    midChunk = audio[chunkSamples:-chunkSamples]
    print(len(midChunk))
    endChunk = audio[-chunkSamples:]
    print(len(endChunk))

    return startChunk, midChunk, endChunk


if __name__ == "__main__":
    timeStamp = 10 #in millisec (10 seconds)
    audioFile = "test.mp3"
    startChunk, midChunk, endChunk = breakStartAndEndChuck(audioFile, timeStamp)
    # print("Start chunk: ", startChunk, "\nMid chunk: ", midChunk, "\nEnd chunk: ", endChunk)