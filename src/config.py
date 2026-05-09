import torch

#Paths
PROJECT_DIR = '/content/drive/MyDrive/CSE425_MusicGen'
DATA_DIR = f'{PROJECT_DIR}/data'
RAW_MIDI_DIR = f'{DATA_DIR}/raw_midi'
PROCESSED_DIR = f'{DATA_DIR}/processed'
MODELS_DIR = f'{PROJECT_DIR}/models_saved'
OUTPUTS_DIR = f'{PROJECT_DIR}/outputs'
PLOTS_DIR = f'{OUTPUTS_DIR}/plots'
MIDI_OUT_DIR = f'{OUTPUTS_DIR}/generated_midis'
MAESTRO_DIR = f'{RAW_MIDI_DIR}/maestro-v3.0.0'

#Dataset
FRAME_RATE = 16    
WINDOW_SIZE = 128  
MIN_ACTIVITY = 0.02 
PIANO_MIN = 21   
PIANO_MAX = 108  
N_PITCHES = PIANO_MAX - PIANO_MIN + 1  

#Token Sequences (Tasks 3 & 4) 
SEQ_LEN = 256   
N_VELOCITIES = 32    

#odel Hyperparameters
INPUT_DIM = 88  
HIDDEN_DIM = 256   
LATENT_DIM  = 64 
NUM_LAYERS= 2  
DROPOUT = 0.3 

D_MODEL = 256    
NHEAD = 8     
NUM_LAYERS_TR = 4  
DIM_FF = 512  

#Training
BATCH_SIZE = 64
LR_AE = 1e-3   
LR_VAE = 1e-3  
LR_TR = 3e-4   
LR_RL = 1e-5   
EPOCHS_AE = 80    
EPOCHS_VAE = 100    
EPOCHS_TR = 50    
RL_ITERATIONS = 30    
CLIP_NORM = 1.0   
SEED = 42     

#Focal Loss
FOCAL_ALPHA = 10.0  
FOCAL_GAMMA = 2.0    

#KL Annealing (Task 2)
KL_WARMUP = 30 
MAX_BETA  = 1.0   

#Generation
GEN_THRESHOLD = 0.3  
TOP_K = 40 
TEMPERATURE = 0.9 

#Device 
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')