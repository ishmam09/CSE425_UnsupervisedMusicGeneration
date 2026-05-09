# CSE425_UnsupervisedMusicGeneration
# 🎵 Unsupervised Neural Network for Multi-Genre Music Generation

> **Course:** CSE425 
> **Institution:** BRAC University | Department of Computer Science & Engineering
## N.B: All files including models training and evaluation are in the notebooks together. 
---

## 👥 Group Members

| Name | Student ID | Contribution |
|------|-----------|-------------|
| Syed Azmain Ishmam | 22201654 | Setup, Dataset preprocessing, EDA, Task 1 LSTM Autoencoder, Task 2 VAE |
| Mahmud Al Fuad Rubai | 22201329 | Task 3 Transformer, Task 4 RLHF, Baseline Models, Evaluation |


---

## 📌 Project Overview

This project builds a four-stage unsupervised generative framework for symbolic music generation using MIDI data from the **MAESTRO v3.0.0** dataset. Rather than relying on labeled data, all models learn musical structure directly from raw MIDI files.

We implement four progressively powerful models:

| Task | Model | Goal |
|------|-------|------|
| Task 1 | LSTM Autoencoder | Single-genre reconstruction via compressed latent codes |
| Task 2 | Variational Autoencoder (VAE) | Multi-genre diversity via structured latent space |
| Task 3 | Decoder-only Transformer | Long-horizon autoregressive sequence generation |
| Task 4 | RLHF Fine-Tuning | Human preference alignment via policy gradient |

All models are compared against two baselines: a **Random Note Generator** and a **First-Order Markov Chain**.

---

## 🎧 Generated MIDI Samples

All generated MIDI files are publicly available on Google Drive:

> 🔗 **https://drive.google.com/drive/folders/1JFRRC2D9c5wq8S04ZvpVKth0LcS4POHj?usp=sharing**

| Model | Files | Description |
|-------|-------|-------------|
| Random Generator | `baseline_random_1.mid` - `baseline_random_5.mid` | Random pitch/duration sampling |
| Markov Chain | `baseline_markov_1.mid` - `baseline_markov_5.mid` | First-order pitch transition model |
| Task 1: LSTM AE | `task1_generated_1.mid` - `task1_generated_5.mid` | 8-second window reconstruction |
| Task 2: VAE | `task2_vae_sample_1.mid` - `task2_vae_sample_8.mid` | Multi-style diverse generation |
| Task 2: Interpolation | `task2_interpolation_alpha0.00.mid` - `task2_interpolation_alpha1.00.mid` | Latent space morphing between two pieces |
| Task 3: Transformer | `task3_transformer_1.mid` - `task3_transformer_10.mid` | Long coherent compositions |
| Task 4: RLHF | `task4_rlhf_1.mid` - `task4_rlhf_10.mid` | Human-preference aligned outputs |

> 💡 **To listen:** Drag any `.mid` file into [Signal MIDI Player](https://signal.vercel.app/edit) - free, browser-based, shows piano roll visualization.

---

## 📄 Final Report

> 🔗 **https://drive.google.com/drive/folders/1zaSqFUGhOk_JATHLr_nIzDuQnQDXKWPN?usp=sharing**

---

## 🎬 Demonstration Video

> 🔗 **https://www.youtube.com/watch?v=JkLmbocOdL4**

The video walks through the full pipeline: EDA -> Preprocessing -> Task 1 -> Task 2 -> Task 3 -> Task 4 -> Baselines -> Overall Analysis. Runtime: ~7 minutes.

---

## 📁 Repository Structure

```
music-generation-unsupervised/
│
├── README.md                          
├── requirements.txt                  
│
├── notebooks/
│   ├── 00_setup.ipynb                 
│   ├── 01_preprocessing.ipynb         
│   ├── 02_baseline_markov.ipynb       
│   ├── 03_task1_lstm_ae.ipynb        
│   ├── 04_task2_vae.ipynb             
│   ├── 05_task3_transformer.ipynb     
│   ├── 06_task4_rlhf.ipynb           
│   └── 07_evaluation_metrics.ipynb   
│
├── src/
│   ├── config.py                      
│   ├── preprocessing/
│   │   ├── midi_parser.py             
│   │   └── piano_roll.py              
│   ├── models/
│   │   ├── autoencoder.py            
│   │   ├── vae.py                     
│   │   └── transformer.py            
│   ├── training/
│   │   ├── train_ae.py                
│   │   ├── train_vae.py              
│   │   └── train_transformer.py       
│   └── evaluation/
│       └── metrics.py                
│
├── outputs/
│   ├── generated_midis/               
│   ├── plots/                         
│   ├── evaluation_metrics_all_files.csv    
│   ├── evaluation_summary_table.csv        
│   └── FINAL_results_table.csv             
│
└── report/
    └── final_report.pdf              
```

---

## 🚀 How to Run (Google Colab - Step by Step)

### Step 1 - Open Google Colab
Go to [colab.research.google.com](https://colab.research.google.com) and sign in with your Google account.

### Step 2 - Enable GPU
**Runtime -> Change runtime type -> T4 GPU -> Save**

### Step 3 - Open a Notebook
**File -> Open notebook -> GitHub tab → paste this repo URL -> open any notebook**

### Step 4 - Run in Order
Run all notebooks **in this exact order**:

```
00_setup.ipynb
    ↓
01_preprocessing.ipynb       <- Downloads MAESTRO, runs EDA, builds piano-roll dataset
    ↓
02_baseline_markov.ipynb     <- Generates baseline MIDI samples
    ↓
03_task1_lstm_ae.ipynb       <- Trains Task 1, generates 5 MIDI samples
    ↓
04_task2_vae.ipynb           <- Trains Task 2, generates 8 + 8 interpolation samples
    ↓
05_task3_transformer.ipynb   <- Trains Task 3, generates 10 long compositions
    ↓
[Run human survey here — collect ratings from 10+ participants]
    ↓
06_task4_rlhf.ipynb          <- RLHF fine-tuning, generates 10 RLHF samples
    ↓
07_evaluation_metrics.ipynb  <- Computes all metrics, produces final results table
```

> ⚠️ **Important:** Every notebook starts with mounting Google Drive. All outputs save automatically to `/content/drive/MyDrive/CSE425_MusicGen/`. Re-run the setup cells at the start of every new Colab session because Colab resets installed packages on reconnect.

---

## 📊 Results

### Quantitative Evaluation

| Model | Recon. Loss | Perplexity | Rhythm Diversity | Repetition Ratio | Human Score /5 |
|-------|------------|------------|-----------------|-----------------|---------------|
| Random Generator | - | - | 0.0579 | 0.0000 | 2.09 |
| Markov Chain | - | - | 0.1380 | 0.0000 | 2.09 |
| Task 1: LSTM AE | 0.0721 | - | 0.5391 | 0.0120 | 3.55 |
| Task 2: VAE | 0.1763 | - | 0.1086 | 0.0000 | 1.73 |
| Task 3: Transformer | - | 6.78 | 0.0535 | 0.0289 | 3.36 |
| Task 4: RLHF-Tuned | - | 8.58 | 0.0519 | 0.0242 | 3.73 |

> **Metrics guide:**
> - **Recon. Loss** -> lower is better
> - **Perplexity** -> lower is better
> - **Rhythm Diversity** -> higher is better (more rhythmic variety)
> - **Repetition Ratio** -> healthy range is 0.1–0.5
> - **Human Score** -> higher is better (1–5 scale, blind listening survey, n=11 participants)

### Human Survey

- **Survey participants:** [VALUE]
- **Clips rated per participant:** 6 (one per model, blind)
- **Rating scale:** 1 (incoherent) to 5 (excellent)
- **Survey tool:** Google Forms

---

## 🗂️ Dataset

**MAESTRO v3.0.0** - MIDI and Audio Edited for Synchronous TRacks and Organization

| Property | Value |
|----------|-------|
| Source | [magenta.tensorflow.org/datasets/maestro](https://magenta.tensorflow.org/datasets/maestro) |
| Total files | 1,276 MIDI recordings |
| Total duration | ~200 hours |
| Instrument | Classical piano (Yamaha Disklavier) |
| Train / Val / Test | 962 / 137 / 177 files |
| Package used | MIDI-only (~57 MB) |

---

## 🧠 Model Architectures

### Task 1 - LSTM Autoencoder
- **Encoder:** 2-layer LSTM (hidden=256) → Linear → z ∈ R⁶⁴
- **Decoder:** z repeated × T → 2-layer LSTM → Linear → logits ∈ R^(128×88)
- **Loss:** Focal Loss (α=10, γ=2) — handles 97% piano-roll sparsity
- **Training:** 80 epochs, Adam lr=1e-3, gradient clip=1.0

### Task 2 - Variational Autoencoder
- **Encoder:** 2-layer LSTM → [fc_mu, fc_log_var] → μ, log σ² ∈ R⁶⁴
- **Reparameterization:** z = μ + σ ⊙ ε, ε ~ N(0,I)
- **Loss:** L_VAE = L_recon + β·D_KL
- **KL Annealing:** β: 0 → 1.0 linearly over first 30 epochs
- **Training:** 100 epochs, Adam lr=1e-3

### Task 3 - Decoder-Only Transformer
- **Architecture:** Token embedding (d=256) + Positional encoding + 4× Transformer decoder layers (8 heads, ff=512)
- **Causal mask:** Upper triangular — prevents future token leakage
- **Loss:** Cross-entropy negative log-likelihood
- **Metric:** Perplexity = exp(1/T × L_TR)
- **Generation:** Top-k sampling (k=40, temperature=0.9)
- **Training:** 50 epochs, Adam lr=3e-4

### Task 4 - RLHF Fine-Tuning
- **Base model:** Task 3 best checkpoint
- **Reward:** Human survey ratings (1–5 scale) from [VALUE] participants
- **Reward model:** MLP (6 musical features → 1 predicted score)
- **Algorithm:** REINFORCE policy gradient with reward normalization
- **Fine-tuning:** 30 iterations, lr=1e-5, gradient clip=0.5

---

## 📏 Evaluation Metrics

All metrics computed from MIDI files using `pretty_midi`. Implemented in `07_evaluation_metrics.ipynb` and `src/evaluation/metrics.py`.

**Pitch Histogram Similarity**
```
H(p, q) = Σᵢ |pᵢ - qᵢ|    for i = 1..12 pitch classes
Lower = more similar to real music. Range: 0 (identical) to 2 (maximally different).
```

**Rhythm Diversity Score**
```
D = (# unique note durations) / (# total notes)
Durations quantized to nearest 50ms. Higher = more rhythmic variety.
```

**Repetition Ratio**
```
R = (# repeated 4-gram pitch patterns) / (# total 4-gram patterns)
Healthy range for classical music: 0.1 – 0.5
```

**Human Listening Score**
```
Blind survey. 1 clip per model. 10+ participants. Rating scale 1–5.
```

---

## ⚠️ Key Challenges and Solutions

| Challenge | What Happened | Solution |
|-----------|--------------|----------|
| Piano-roll sparsity (97% zeros) | MSE and BCE loss collapsed to predicting all silence | Replaced with **Focal Loss** (α=10, γ=2) |
| VAE posterior collapse | Encoder stopped using latent space by epoch 5 | **KL annealing** - β=0 for 30 epochs, then ramp to 1.0 |
| Transformer repetition loops | Greedy decoding caused model to loop same pattern forever | **Top-k sampling** (k=40) with temperature=0.9 |
| RLHF gradient variance | REINFORCE updates wildly unstable | **Reward normalization** - subtract batch mean, divide by std |
| Sigmoid + BCEWithLogitsLoss | Double sigmoid caused NaN loss from start | Removed sigmoid from decoder output layer, raw logits to loss |

---

## 🔧 Installation

**requirements.txt contents:**
```
pretty_midi==0.2.10
miditok==3.0.4
torch>=2.0.0
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
scikit-learn>=1.3.0
tqdm>=4.65.0
midi2audio>=0.1.1
```

> ⚠️ Install PyTorch first using the official selector at [pytorch.org](https://pytorch.org/get-started/locally/) — the correct command depends on your OS and CUDA version.

---

## 🔗 References

1. Hawthorne, C. et al. (2019). *Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset.* ICLR 2019.

---

## 📬 Contact

For questions about this project, contact any group member via syed.azmain.ishmam@g.bracu.ac.bd or mahmud.alfuad.rubai@g.bracu.ac.bd 

---
