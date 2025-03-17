import os
import librosa
import numpy as np
import matplotlib.pyplot as plt

DATASET_PATH = os.path.expanduser("~/wakeword_project/data/")
FEATURES_PATH = os.path.expanduser("~/wakeword_project/features/")
os.makedirs(FEATURES_PATH, exist_ok=True)

def extract_features(file_path):
    """Extract MFCC features from an audio file."""
    y, sr = librosa.load(file_path, sr=16000)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)

wakeword_features = []
not_wakeword_features = []

for category in ["wakeword", "not-wakeword"]:
    folder_path = os.path.join(DATASET_PATH, category)
    for file in os.listdir(folder_path):
        if file.endswith(".wav"):
            file_path = os.path.join(folder_path, file)
            features = extract_features(file_path)
            if category == "wakeword":
                wakeword_features.append(features)
            else:
                not_wakeword_features.append(features)

# Save extracted features as numpy files
np.save(os.path.join(FEATURES_PATH, "wakeword.npy"), wakeword_features)
np.save(os.path.join(FEATURES_PATH, "not_wakeword.npy"), not_wakeword_features)

print("Feature extraction complete! Features saved in:", FEATURES_PATH)

