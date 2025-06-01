import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time
import os

def plot(scores, mean_scores, filename='plots/training_progress.png'):
    plt.clf()
    plt.title("Training Progress")
    plt.xlabel("Games")
    plt.ylabel("Score")
    plt.plot(scores, label='Score', color='blue', alpha=0.5, linewidth=1)
    plt.plot(mean_scores, label='Mean Score', color='red', linewidth=2)
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.legend()
    plt.ylim(ymin=0)
    plt.tight_layout()
    
    os.makedirs('plots', exist_ok=True)
    plt.savefig("training_progress")  # Always save to the same file (overwrite)
    plt.close()

