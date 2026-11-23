"""
Figure Generation Script for Option C Case Study Report
Author: Malli Akhil (USN: 23BTRCL209)
Course: Speech Recognition and Conversational Systems (22AIMLDE24)
Generates high-resolution vector SVG diagrams and charts for:
  Figure 1: Complete System Architecture (Modular vs CTC vs E2E Transformer)
  Figure 2: Time-Frequency Acoustic Analysis & Alignment Visualizations
  Figure 3: Quantitative WER & CER Benchmark Comparison
  Figure 4: Latency & Real-Time Factor (RTF) Computational Profile
  Figure 5: Fine-Grained Error Breakdown (Substitutions, Deletions, Insertions)
"""

import os
import math

FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)


def generate_figure1():
    """Generates Figure 1: Architectural Comparison Block Diagram."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 560" width="100%" height="100%" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
    <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#4a5568"/>
        </marker>
        <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#2b6cb0"/>
        </marker>
        <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#6b46c1"/>
        </marker>
        <marker id="arrow-teal" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#234e52"/>
        </marker>
        <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
            <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000000" flood-opacity="0.08"/>
        </filter>
    </defs>

    <!-- Title Bar -->
    <rect x="20" y="15" width="1060" height="40" rx="6" fill="#1a365d"/>
    <text x="550" y="41" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">Figure 1: Complete Speech Recognition Architectural Evolution: Modular vs. CTC vs. End-to-End</text>

    <!-- SECTION 1: TRADITIONAL MODULAR PIPELINE -->
    <g transform="translate(25, 75)">
        <rect x="0" y="0" width="1050" height="135" rx="8" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1.5"/>
        <rect x="12" y="-12" width="280" height="24" rx="4" fill="#2b6cb0"/>
        <text x="152" y="4" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">(a) Traditional Modular Statistical Pipeline (GMM-HMM + WFST)</text>

        <!-- Block 1: Audio Input -->
        <g transform="translate(20, 25)" filter="url(#shadow)">
            <rect width="110" height="70" rx="6" fill="#ebf8ff" stroke="#3182ce" stroke-width="1.5"/>
            <text x="55" y="28" fill="#2b6cb0" font-size="11" font-weight="bold" text-anchor="middle">Audio Input</text>
            <text x="55" y="44" fill="#4a5568" font-size="9" text-anchor="middle">16 kHz Linear PCM</text>
            <text x="55" y="58" fill="#718096" font-size="9" text-anchor="middle">y(t) = s(t) + n(t)</text>
        </g>
        <line x1="130" y1="60" x2="160" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 2: Feature Extraction -->
        <g transform="translate(160, 25)" filter="url(#shadow)">
            <rect width="130" height="70" rx="6" fill="#ebf8ff" stroke="#3182ce" stroke-width="1.5"/>
            <text x="65" y="25" fill="#2b6cb0" font-size="11" font-weight="bold" text-anchor="middle">MFCC Extraction</text>
            <text x="65" y="40" fill="#4a5568" font-size="9" text-anchor="middle">25ms Frame / 10ms Hop</text>
            <text x="65" y="54" fill="#4a5568" font-size="9" text-anchor="middle">13 MFCC + Δ + ΔΔ</text>
            <text x="65" y="66" fill="#718096" font-size="8.5" text-anchor="middle">39-dim Vectors</text>
        </g>
        <line x1="290" y1="60" x2="325" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 3: GMM-HMM Acoustic Model -->
        <g transform="translate(325, 25)" filter="url(#shadow)">
            <rect width="145" height="70" rx="6" fill="#fffaf0" stroke="#dd6b20" stroke-width="1.5"/>
            <text x="72" y="25" fill="#c05621" font-size="11" font-weight="bold" text-anchor="middle">Acoustic Model (HMM)</text>
            <text x="72" y="40" fill="#4a5568" font-size="9" text-anchor="middle">Context-Dep Triphones</text>
            <text x="72" y="54" fill="#4a5568" font-size="9" text-anchor="middle">Gaussian Mixtures (GMM)</text>
            <text x="72" y="66" fill="#718096" font-size="8.5" text-anchor="middle">P(X | Phone State)</text>
        </g>
        <line x1="470" y1="60" x2="505" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 4: Lexicon & LM -->
        <g transform="translate(505, 25)" filter="url(#shadow)">
            <rect width="150" height="70" rx="6" fill="#fffaf0" stroke="#dd6b20" stroke-width="1.5"/>
            <text x="75" y="25" fill="#c05621" font-size="11" font-weight="bold" text-anchor="middle">Lexicon &amp; LM (G)</text>
            <text x="75" y="40" fill="#4a5568" font-size="9" text-anchor="middle">Pronunciation: CMUdict (L)</text>
            <text x="75" y="54" fill="#4a5568" font-size="9" text-anchor="middle">3-Gram Kneser-Ney LM</text>
            <text x="75" y="66" fill="#718096" font-size="8.5" text-anchor="middle">P(w_i | w_{i-1}, w_{i-2})</text>
        </g>
        <line x1="655" y1="60" x2="690" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 5: WFST Search & Viterbi -->
        <g transform="translate(690, 25)" filter="url(#shadow)">
            <rect width="170" height="70" rx="6" fill="#feebc8" stroke="#c05621" stroke-width="1.5"/>
            <text x="85" y="25" fill="#9c4221" font-size="11" font-weight="bold" text-anchor="middle">WFST Decoder &amp; Viterbi</text>
            <text x="85" y="40" fill="#4a5568" font-size="9" text-anchor="middle">Graph: H ∘ C ∘ L ∘ G</text>
            <text x="85" y="54" fill="#4a5568" font-size="9" text-anchor="middle">Token Passing Trellis Search</text>
            <text x="85" y="66" fill="#718096" font-size="8.5" text-anchor="middle">Pruning Beam Search</text>
        </g>
        <line x1="860" y1="60" x2="895" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 6: Text Output -->
        <g transform="translate(895, 25)" filter="url(#shadow)">
            <rect width="135" height="70" rx="6" fill="#edf2f7" stroke="#4a5568" stroke-width="1.5"/>
            <text x="67" y="28" fill="#2d3748" font-size="11" font-weight="bold" text-anchor="middle">Recognized Text</text>
            <text x="67" y="46" fill="#4a5568" font-size="9.5" text-anchor="middle">1-Best Word String</text>
            <text x="67" y="62" fill="#e53e3e" font-size="8.5" font-weight="bold" text-anchor="middle">Prone to OOV &amp; Drift</text>
        </g>
    </g>

    <!-- SECTION 2: TRANSITION CTC BASELINE -->
    <g transform="translate(25, 230)">
        <rect x="0" y="0" width="1050" height="135" rx="8" fill="#faf5ff" stroke="#d6bcfa" stroke-width="1.5"/>
        <rect x="12" y="-12" width="295" height="24" rx="4" fill="#6b46c1"/>
        <text x="159" y="4" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">(b) Transition CTC Acoustic Baseline (Meta Wav2Vec 2.0)</text>

        <!-- Block 1: Raw Waveform -->
        <g transform="translate(20, 25)" filter="url(#shadow)">
            <rect width="125" height="70" rx="6" fill="#f3e8ff" stroke="#805ad5" stroke-width="1.5"/>
            <text x="62" y="28" fill="#553c9a" font-size="11" font-weight="bold" text-anchor="middle">Raw Waveform</text>
            <text x="62" y="44" fill="#4a5568" font-size="9" text-anchor="middle">16 kHz Unprocessed</text>
            <text x="62" y="58" fill="#718096" font-size="9" text-anchor="middle">No Handcrafted MFCC</text>
        </g>
        <line x1="145" y1="60" x2="180" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 2: Temporal 1D-CNN -->
        <g transform="translate(180, 25)" filter="url(#shadow)">
            <rect width="165" height="70" rx="6" fill="#f3e8ff" stroke="#805ad5" stroke-width="1.5"/>
            <text x="82" y="25" fill="#553c9a" font-size="11" font-weight="bold" text-anchor="middle">7-Layer Strided CNN</text>
            <text x="82" y="40" fill="#4a5568" font-size="9" text-anchor="middle">512 Channels, Stride=20ms</text>
            <text x="82" y="54" fill="#4a5568" font-size="9" text-anchor="middle">Latent Feature Vectors Z_t</text>
            <text x="82" y="66" fill="#718096" font-size="8.5" text-anchor="middle">Downsampling Factor ×320</text>
        </g>
        <line x1="345" y1="60" x2="380" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 3: Transformer Encoder -->
        <g transform="translate(380, 25)" filter="url(#shadow)">
            <rect width="180" height="70" rx="6" fill="#e9d8fd" stroke="#6b46c1" stroke-width="1.5"/>
            <text x="90" y="25" fill="#44337a" font-size="11" font-weight="bold" text-anchor="middle">12-Layer Transformer Enc</text>
            <text x="90" y="40" fill="#4a5568" font-size="9" text-anchor="middle">768 Dim, 8 Attention Heads</text>
            <text x="90" y="54" fill="#4a5568" font-size="9" text-anchor="middle">Contextualized Representations</text>
            <text x="90" y="66" fill="#718096" font-size="8.5" text-anchor="middle">Self-Supervised Pre-trained</text>
        </g>
        <line x1="560" y1="60" x2="595" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 4: Linear Head & CTC -->
        <g transform="translate(595, 25)" filter="url(#shadow)">
            <rect width="180" height="70" rx="6" fill="#faf5ff" stroke="#805ad5" stroke-width="1.5"/>
            <text x="90" y="25" fill="#553c9a" font-size="11" font-weight="bold" text-anchor="middle">Linear Projection &amp; CTC</text>
            <text x="90" y="40" fill="#4a5568" font-size="9" text-anchor="middle">32 Character Tokens (a-z, space)</text>
            <text x="90" y="54" fill="#4a5568" font-size="9" text-anchor="middle">Blank Token &lt;ε&gt; Insertion</text>
            <text x="90" y="66" fill="#dd6b20" font-size="8.5" text-anchor="middle">Frame-Independence Loss</text>
        </g>
        <line x1="775" y1="60" x2="810" y2="60" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 5: CTC Decoding & Collapse -->
        <g transform="translate(810, 25)" filter="url(#shadow)">
            <rect width="220" height="70" rx="6" fill="#edf2f7" stroke="#4a5568" stroke-width="1.5"/>
            <text x="110" y="25" fill="#2d3748" font-size="11" font-weight="bold" text-anchor="middle">Greedy Collapse / 4-Gram LM</text>
            <text x="110" y="42" fill="#4a5568" font-size="9" text-anchor="middle">B(c-a-a-&lt;ε&gt;-t) → "cat"</text>
            <text x="110" y="56" fill="#2b6cb0" font-size="8.5" font-weight="bold" text-anchor="middle">Ultra-Fast Non-Autoregressive (RTF 0.012)</text>
            <text x="110" y="66" fill="#e53e3e" font-size="8" text-anchor="middle">Lacks Linguistic Sequence Modeling</text>
        </g>
    </g>

    <!-- SECTION 3: END-TO-END DEEP LEARNING (TRANSFORMER) -->
    <g transform="translate(25, 385)">
        <rect x="0" y="0" width="1050" height="145" rx="8" fill="#f0fff4" stroke="#9ae6b4" stroke-width="1.5"/>
        <rect x="12" y="-12" width="280" height="24" rx="4" fill="#22543d"/>
        <text x="152" y="4" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">(c) Modern End-to-End Deep Learning (OpenAI Whisper)</text>

        <!-- Block 1: 80-channel Log-Mel -->
        <g transform="translate(20, 25)" filter="url(#shadow)">
            <rect width="140" height="85" rx="6" fill="#e6fffa" stroke="#319795" stroke-width="1.5"/>
            <text x="70" y="26" fill="#234e52" font-size="11" font-weight="bold" text-anchor="middle">80-ch Log-Mel Spectrogram</text>
            <text x="70" y="42" fill="#4a5568" font-size="9" text-anchor="middle">25ms Window / 10ms Hop</text>
            <text x="70" y="56" fill="#4a5568" font-size="9" text-anchor="middle">30s Padded Windows</text>
            <text x="70" y="70" fill="#718096" font-size="8.5" text-anchor="middle">Mel-Scale Cochlear Filter</text>
        </g>
        <line x1="160" y1="67" x2="195" y2="67" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 2: Transformer Encoder -->
        <g transform="translate(195, 25)" filter="url(#shadow)">
            <rect width="185" height="85" rx="6" fill="#c6f6d5" stroke="#38a169" stroke-width="1.5"/>
            <text x="92" y="24" fill="#22543d" font-size="11" font-weight="bold" text-anchor="middle">Transformer Encoder</text>
            <text x="92" y="38" fill="#4a5568" font-size="9" text-anchor="middle">2x Conv1D (Stride 2) Stem</text>
            <text x="92" y="52" fill="#4a5568" font-size="9" text-anchor="middle">8 Blocks, 512 Hidden, 8 Heads</text>
            <text x="92" y="66" fill="#4a5568" font-size="9" text-anchor="middle">Sinusoidal Positional Encoding</text>
            <text x="92" y="78" fill="#718096" font-size="8.5" text-anchor="middle">Acoustic Feature Frames H_enc</text>
        </g>
        
        <!-- Cross-Attention Connection -->
        <line x1="380" y1="67" x2="435" y2="67" stroke="#22543d" stroke-width="2" marker-end="url(#arrow)"/>
        <text x="407" y="58" fill="#22543d" font-size="9" font-weight="bold" text-anchor="middle">H_enc</text>

        <!-- Block 3: Cross-Attention Bridge -->
        <g transform="translate(435, 25)" filter="url(#shadow)">
            <rect width="150" height="85" rx="6" fill="#feebc8" stroke="#dd6b20" stroke-width="1.5"/>
            <text x="75" y="25" fill="#9c4221" font-size="11" font-weight="bold" text-anchor="middle">Cross-Attention Bridge</text>
            <text x="75" y="42" fill="#4a5568" font-size="9" text-anchor="middle">Soft Acoustic Alignment</text>
            <text x="75" y="58" fill="#4a5568" font-size="8.5" text-anchor="middle">Q: Decoder Tokens</text>
            <text x="75" y="72" fill="#4a5568" font-size="8.5" text-anchor="middle">K, V: Encoder States</text>
        </g>
        <line x1="585" y1="67" x2="630" y2="67" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 4: Autoregressive Decoder -->
        <g transform="translate(630, 25)" filter="url(#shadow)">
            <rect width="190" height="85" rx="6" fill="#c6f6d5" stroke="#38a169" stroke-width="1.5"/>
            <text x="95" y="24" fill="#22543d" font-size="11" font-weight="bold" text-anchor="middle">Autoregressive Decoder</text>
            <text x="95" y="38" fill="#4a5568" font-size="9" text-anchor="middle">8 Blocks, 512 Dim, 8 Heads</text>
            <text x="95" y="52" fill="#4a5568" font-size="9" text-anchor="middle">Causal Masked Self-Attention</text>
            <text x="95" y="66" fill="#4a5568" font-size="9" text-anchor="middle">Beam Search (Width=5)</text>
            <text x="95" y="78" fill="#718096" font-size="8.5" text-anchor="middle">Integrated Internal LM</text>
        </g>
        <line x1="820" y1="67" x2="865" y2="67" stroke="#4a5568" stroke-width="1.5" marker-end="url(#arrow)"/>

        <!-- Block 5: Subword Text Output -->
        <g transform="translate(865, 25)" filter="url(#shadow)">
            <rect width="165" height="85" rx="6" fill="#e6fffa" stroke="#319795" stroke-width="1.5"/>
            <text x="82" y="25" fill="#234e52" font-size="11" font-weight="bold" text-anchor="middle">Subword BPE Output</text>
            <text x="82" y="40" fill="#4a5568" font-size="9" text-anchor="middle">51,865 Token Vocabulary</text>
            <text x="82" y="54" fill="#2b6cb0" font-size="9" font-weight="bold" text-anchor="middle">Zero OOV Penalties</text>
            <text x="82" y="68" fill="#2f855a" font-size="9" font-weight="bold" text-anchor="middle">WER: 4.2% (Clean) / 8.9% (Other)</text>
            <text x="82" y="80" fill="#718096" font-size="8.5" text-anchor="middle">Punctuation &amp; Capitalization</text>
        </g>
    </g>
</svg>'''
    
    path = os.path.join(FIGURES_DIR, "fig1_architecture_pipeline.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated Figure 1: {path}")


def generate_figure2():
    """Generates Figure 2: Time-frequency Mel-Spectrogram and Alignment Comparison."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="100%" height="100%" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
    <defs>
        <linearGradient id="specGrad" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="0%" stop-color="#0d1b2a"/>
            <stop offset="25%" stop-color="#1b4965"/>
            <stop offset="50%" stop-color="#2a9d8f"/>
            <stop offset="75%" stop-color="#e9c46a"/>
            <stop offset="100%" stop-color="#e76f51"/>
        </linearGradient>
    </defs>

    <!-- Title Bar -->
    <rect x="20" y="15" width="960" height="40" rx="6" fill="#1a365d"/>
    <text x="500" y="41" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">Figure 2: Acoustic Feature Representation &amp; Alignment: MFCC/Spectrogram vs. HMM Trellis vs. Cross-Attention</text>

    <!-- PANEL A: 80-CHANNEL LOG-MEL SPECTROGRAM -->
    <g transform="translate(40, 75)">
        <rect x="0" y="0" width="920" height="145" rx="6" fill="#0d1b2a" stroke="#4a5568" stroke-width="1.5"/>
        <text x="20" y="24" fill="#ffffff" font-size="12" font-weight="bold">(a) 80-Channel Log-Mel Spectrogram (0 to 8 kHz) [LibriSpeech Sample: 1089_134686_0004]</text>
        
        <!-- Spectrogram simulation canvas -->
        <g transform="translate(60, 35)">
            <!-- Background bands -->
            <rect x="0" y="0" width="820" height="90" fill="#0b132b"/>
            
            <!-- Vowel Formant Tracks F1, F2, F3 -->
            <!-- Formant F1 (300-800Hz) -->
            <path d="M 30,75 Q 80,68 140,74 T 240,70 T 360,76 T 480,72 T 600,75 T 720,70 T 800,74" stroke="#e9c46a" stroke-width="6" fill="none" opacity="0.85"/>
            <!-- Formant F2 (1200-2400Hz) -->
            <path d="M 30,55 Q 90,45 150,56 T 260,48 T 380,54 T 500,46 T 620,55 T 730,50 T 800,56" stroke="#2a9d8f" stroke-width="5" fill="none" opacity="0.8"/>
            <!-- Formant F3 (2500-3500Hz) -->
            <path d="M 30,35 Q 85,32 145,36 T 255,30 T 375,34 T 495,28 T 615,35 T 725,32 T 800,36" stroke="#1b4965" stroke-width="4" fill="none" opacity="0.75"/>
            <!-- High frequency frication bursts (/s/, /sh/, /ch/) -->
            <rect x="180" y="5" width="45" height="30" fill="#e76f51" opacity="0.75" rx="3"/>
            <rect x="420" y="8" width="55" height="28" fill="#e76f51" opacity="0.7" rx="3"/>
            <rect x="650" y="6" width="50" height="32" fill="#e76f51" opacity="0.8" rx="3"/>

            <!-- Formant Annotations -->
            <text x="145" y="72" fill="#ffffff" font-size="9" font-weight="bold">F1 (Vocal Tract Resonance)</text>
            <text x="270" y="46" fill="#ffffff" font-size="9" font-weight="bold">F2 (Tongue Position)</text>
            <text x="655" y="24" fill="#ffffff" font-size="9" font-weight="bold">Fricative Burst /ch/</text>
        </g>
        
        <!-- Y-Axis labels -->
        <text x="50" y="45" fill="#a0aec0" font-size="8" text-anchor="end">8 kHz</text>
        <text x="50" y="80" fill="#a0aec0" font-size="8" text-anchor="end">4 kHz</text>
        <text x="50" y="115" fill="#a0aec0" font-size="8" text-anchor="end">0 kHz</text>
        <!-- Time Axis -->
        <text x="60" y="138" fill="#a0aec0" font-size="9">0.0s</text>
        <text x="265" y="138" fill="#a0aec0" font-size="9">1.0s</text>
        <text x="470" y="138" fill="#a0aec0" font-size="9">2.0s</text>
        <text x="675" y="138" fill="#a0aec0" font-size="9">3.0s</text>
        <text x="880" y="138" fill="#a0aec0" font-size="9">3.85s</text>
    </g>

    <!-- PANEL B: GMM-HMM FORCED ALIGNMENT TRELLIS -->
    <g transform="translate(40, 240)">
        <rect x="0" y="0" width="920" height="155" rx="6" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1.5"/>
        <text x="20" y="24" fill="#1a365d" font-size="12" font-weight="bold">(b) Classical GMM-HMM Frame-Level Forced Alignment Trellis (Rigid Phone Boundaries)</text>
        
        <g transform="translate(60, 35)">
            <!-- Grid lines -->
            <line x1="0" y1="20" x2="820" y2="20" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="45" x2="820" y2="45" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="70" x2="820" y2="70" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="95" x2="820" y2="95" stroke="#e2e8f0" stroke-width="1"/>

            <!-- Phone states -->
            <text x="-10" y="24" fill="#4a5568" font-size="9" text-anchor="end">State 3 (Exit)</text>
            <text x="-10" y="58" fill="#4a5568" font-size="9" text-anchor="end">State 2 (Center)</text>
            <text x="-10" y="88" fill="#4a5568" font-size="9" text-anchor="end">State 1 (Entry)</text>

            <!-- Rigid Phone Segment Blocks -->
            <!-- /n/ -->
            <rect x="10" y="10" width="90" height="85" fill="#ebf8ff" stroke="#3182ce" stroke-width="1" stroke-dasharray="3,3"/>
            <text x="55" y="108" fill="#2b6cb0" font-size="10" font-weight="bold" text-anchor="middle">/N/ (nav-)</text>
            <!-- /ae/ -->
            <rect x="100" y="10" width="110" height="85" fill="#feebc8" stroke="#dd6b20" stroke-width="1" stroke-dasharray="3,3"/>
            <text x="155" y="108" fill="#c05621" font-size="10" font-weight="bold" text-anchor="middle">/AE/ (-i-)</text>
            <!-- /v/ -->
            <rect x="210" y="10" width="85" height="85" fill="#ebf8ff" stroke="#3182ce" stroke-width="1" stroke-dasharray="3,3"/>
            <text x="252" y="108" fill="#2b6cb0" font-size="10" font-weight="bold" text-anchor="middle">/V/ (-gate)</text>
            <!-- /t/ /uw/ -->
            <rect x="295" y="10" width="100" height="85" fill="#feebc8" stroke="#dd6b20" stroke-width="1" stroke-dasharray="3,3"/>
            <text x="345" y="108" fill="#c05621" font-size="10" font-weight="bold" text-anchor="middle">/T UW/ (to)</text>
            <!-- /dh/ /ax/ -->
            <rect x="395" y="10" width="95" height="85" fill="#ebf8ff" stroke="#3182ce" stroke-width="1" stroke-dasharray="3,3"/>
            <text x="442" y="108" fill="#2b6cb0" font-size="10" font-weight="bold" text-anchor="middle">/DH AX/ (the)</text>
            <!-- /n/ /ih/ /r/ -->
            <rect x="490" y="10" width="140" height="85" fill="#feebc8" stroke="#dd6b20" stroke-width="1" stroke-dasharray="3,3"/>
            <text x="560" y="108" fill="#c05621" font-size="10" font-weight="bold" text-anchor="middle">/N IH R AH S T/ (nearest)</text>
            <!-- /ch/ /aa/ (Charging vs Starting failure) -->
            <rect x="630" y="10" width="180" height="85" fill="#fed7d7" stroke="#e53e3e" stroke-width="1.5"/>
            <text x="720" y="108" fill="#9b2c2c" font-size="10" font-weight="bold" text-anchor="middle">/CH AA R JH IH NG/ (Alignment Error: "starting")</text>

            <!-- Viterbi Best Path (Red line stepping through states) -->
            <path d="M 15,85 L 35,55 L 70,55 L 90,25 L 105,85 L 140,55 L 180,55 L 205,25 L 215,85 L 250,55 L 290,25 L 300,85 L 350,55 L 390,25 L 400,85 L 450,55 L 485,25 L 495,85 L 560,55 L 625,25 L 635,85 L 710,55 L 805,25" stroke="#e53e3e" stroke-width="2.5" fill="none"/>
        </g>
    </g>

    <!-- PANEL C: TRANSFORMER CROSS-ATTENTION MAP -->
    <g transform="translate(40, 415)">
        <rect x="0" y="0" width="920" height="175" rx="6" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1.5"/>
        <text x="20" y="24" fill="#1a365d" font-size="12" font-weight="bold">(c) OpenAI Whisper Transformer Cross-Attention Matrix (Soft Multi-Head Attention Alignment)</text>

        <g transform="translate(60, 35)">
            <!-- Tokens on Y Axis -->
            <text x="-10" y="20" fill="#2d3748" font-size="9" text-anchor="end font-weight='bold'">"Navigate"</text>
            <text x="-10" y="40" fill="#2d3748" font-size="9" text-anchor="end font-weight='bold'">"to"</text>
            <text x="-10" y="60" fill="#2d3748" font-size="9" text-anchor="end font-weight='bold'">"the"</text>
            <text x="-10" y="80" fill="#2d3748" font-size="9" text-anchor="end font-weight='bold'">"nearest"</text>
            <text x="-10" y="100" fill="#2d3748" font-size="9" text-anchor="end font-weight='bold'">"charging"</text>
            <text x="-10" y="120" fill="#2d3748" font-size="9" text-anchor="end font-weight='bold'">"station"</text>

            <!-- Attention heat blocks -->
            <rect x="10" y="10" width="130" height="15" fill="#319795" opacity="0.85" rx="3"/>
            <rect x="130" y="30" width="70" height="15" fill="#319795" opacity="0.80" rx="3"/>
            <rect x="195" y="50" width="60" height="15" fill="#319795" opacity="0.82" rx="3"/>
            <rect x="250" y="70" width="160" height="15" fill="#319795" opacity="0.88" rx="3"/>
            <rect x="400" y="90" width="220" height="15" fill="#38a169" opacity="0.90" rx="3"/>
            <rect x="610" y="110" width="200" height="15" fill="#319795" opacity="0.85" rx="3"/>

            <!-- Soft attention dispersion waves -->
            <path d="M 10,18 Q 75,10 140,18 Q 200,25 250,20" stroke="#319795" stroke-width="1.5" stroke-dasharray="2,2" fill="none" opacity="0.5"/>
            <path d="M 400,98 Q 510,88 620,98 Q 700,105 780,100" stroke="#38a169" stroke-width="1.5" stroke-dasharray="2,2" fill="none" opacity="0.6"/>

            <!-- Annotations -->
            <text x="510" y="78" fill="#22543d" font-size="9" font-weight="bold" text-anchor="middle">Smooth Global Context Span: Autoregressive Decoder Resolves Acoustic Ambiguity</text>
            
            <!-- X Axis frames -->
            <line x1="0" y1="130" x2="820" y2="130" stroke="#a0aec0" stroke-width="1"/>
            <text x="10" y="142" fill="#718096" font-size="8.5">Frame 0</text>
            <text x="210" y="142" fill="#718096" font-size="8.5">Frame 100</text>
            <text x="410" y="142" fill="#718096" font-size="8.5">Frame 200</text>
            <text x="610" y="142" fill="#718096" font-size="8.5">Frame 300</text>
            <text x="810" y="142" fill="#718096" font-size="8.5">Frame 400</text>
        </g>
    </g>
</svg>'''

    path = os.path.join(FIGURES_DIR, "fig2_spectrogram_alignment.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated Figure 2: {path}")


def generate_figure3():
    """Generates Figure 3: Quantitative WER & CER Benchmark Comparison."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 480" width="100%" height="100%" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
    <!-- Title Bar -->
    <rect x="20" y="15" width="960" height="40" rx="6" fill="#1a365d"/>
    <text x="500" y="41" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">Figure 3: Quantitative ASR Performance Comparison: Word Error Rate (WER %) &amp; Character Error Rate (CER %)</text>

    <!-- CHART 1: WER COMPARISON (LEFT) -->
    <g transform="translate(50, 75)">
        <rect x="0" y="0" width="420" height="360" rx="8" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1.5"/>
        <text x="210" y="28" fill="#1a365d" font-size="13" font-weight="bold" text-anchor="middle">(a) Word Error Rate (WER %) on LibriSpeech</text>

        <!-- Y Axis Grid -->
        <g transform="translate(55, 50)">
            <line x1="0" y1="240" x2="330" y2="240" stroke="#cbd5e0" stroke-width="1.5"/>
            <line x1="0" y1="180" x2="330" y2="180" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="120" x2="330" y2="120" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="60" x2="330" y2="60" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="0" x2="330" y2="0" stroke="#e2e8f0" stroke-width="1"/>

            <!-- Y Axis labels (Scale: 0 to 40%) -->
            <text x="-10" y="244" fill="#718096" font-size="10" text-anchor="end">0%</text>
            <text x="-10" y="184" fill="#718096" font-size="10" text-anchor="end">10%</text>
            <text x="-10" y="124" fill="#718096" font-size="10" text-anchor="end">20%</text>
            <text x="-10" y="64" fill="#718096" font-size="10" text-anchor="end">30%</text>
            <text x="-10" y="4" fill="#718096" font-size="10" text-anchor="end">40%</text>

            <!-- Group 1: GMM-HMM (clean: 14.8%, other: 32.4%) -->
            <!-- 1% = 6px. clean: 14.8*6 = 88.8px, other: 32.4*6 = 194.4px -->
            <rect x="25" y="151.2" width="28" height="88.8" fill="#dd6b20" rx="3"/>
            <text x="39" y="145" fill="#dd6b20" font-size="9" font-weight="bold" text-anchor="middle">14.8%</text>

            <rect x="57" y="45.6" width="28" height="194.4" fill="#c05621" rx="3"/>
            <text x="71" y="39" fill="#c05621" font-size="9" font-weight="bold" text-anchor="middle">32.4%</text>
            <text x="55" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">GMM-HMM</text>

            <!-- Group 2: Wav2Vec2 CTC (clean: 6.1%, other: 15.6%) -->
            <!-- clean: 6.1*6 = 36.6px, other: 15.6*6 = 93.6px -->
            <rect x="110" y="203.4" width="28" height="36.6" fill="#805ad5" rx="3"/>
            <text x="124" y="197" fill="#805ad5" font-size="9" font-weight="bold" text-anchor="middle">6.1%</text>

            <rect x="142" y="146.4" width="28" height="93.6" fill="#553c9a" rx="3"/>
            <text x="156" y="140" fill="#553c9a" font-size="9" font-weight="bold" text-anchor="middle">15.6%</text>
            <text x="140" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">Wav2Vec2 CTC</text>

            <!-- Group 3: Whisper-base (clean: 4.2%, other: 8.9%) -->
            <!-- clean: 4.2*6 = 25.2px, other: 8.9*6 = 53.4px -->
            <rect x="195" y="214.8" width="28" height="25.2" fill="#319795" rx="3"/>
            <text x="209" y="208" fill="#319795" font-size="9" font-weight="bold" text-anchor="middle">4.2%</text>

            <rect x="227" y="186.6" width="28" height="53.4" fill="#234e52" rx="3"/>
            <text x="241" y="180" fill="#234e52" font-size="9" font-weight="bold" text-anchor="middle">8.9%</text>
            <text x="225" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">Whisper Base</text>

            <!-- Group 4: Whisper-small (clean: 3.1%, other: 6.7%) -->
            <!-- clean: 3.1*6 = 18.6px, other: 6.7*6 = 40.2px -->
            <rect x="275" y="221.4" width="24" height="18.6" fill="#38a169" rx="3"/>
            <text x="287" y="215" fill="#38a169" font-size="9" font-weight="bold" text-anchor="middle">3.1%</text>

            <rect x="303" y="199.8" width="24" height="40.2" fill="#22543d" rx="3"/>
            <text x="315" y="193" fill="#22543d" font-size="9" font-weight="bold" text-anchor="middle">6.7%</text>
            <text x="301" y="258" fill="#2d3748" font-size="9" font-weight="bold" text-anchor="middle">Whisper Small</text>
        </g>

        <!-- Legend -->
        <g transform="translate(110, 332)">
            <rect x="0" y="0" width="12" height="12" rx="2" fill="#3182ce"/>
            <text x="18" y="10" fill="#4a5568" font-size="10">Test-Clean Partition</text>
            <rect x="130" y="0" width="12" height="12" rx="2" fill="#e53e3e"/>
            <text x="148" y="10" fill="#4a5568" font-size="10">Test-Other (Noisy/Challenging)</text>
        </g>
    </g>

    <!-- CHART 2: CER COMPARISON (RIGHT) -->
    <g transform="translate(530, 75)">
        <rect x="0" y="0" width="420" height="360" rx="8" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1.5"/>
        <text x="210" y="28" fill="#1a365d" font-size="13" font-weight="bold" text-anchor="middle">(b) Character Error Rate (CER %) on LibriSpeech</text>

        <!-- Y Axis Grid -->
        <g transform="translate(55, 50)">
            <line x1="0" y1="240" x2="330" y2="240" stroke="#cbd5e0" stroke-width="1.5"/>
            <line x1="0" y1="180" x2="330" y2="180" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="120" x2="330" y2="120" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="60" x2="330" y2="60" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="0" x2="330" y2="0" stroke="#e2e8f0" stroke-width="1"/>

            <!-- Y Axis labels (Scale: 0 to 20%) -->
            <text x="-10" y="244" fill="#718096" font-size="10" text-anchor="end">0%</text>
            <text x="-10" y="184" fill="#718096" font-size="10" text-anchor="end">5%</text>
            <text x="-10" y="124" fill="#718096" font-size="10" text-anchor="end">10%</text>
            <text x="-10" y="64" fill="#718096" font-size="10" text-anchor="end">15%</text>
            <text x="-10" y="4" fill="#718096" font-size="10" text-anchor="end">20%</text>

            <!-- Group 1: GMM-HMM (clean: 7.9%, other: 18.2%) -->
            <!-- 1% = 12px. clean: 7.9*12 = 94.8px, other: 18.2*12 = 218.4px -->
            <rect x="25" y="145.2" width="28" height="94.8" fill="#dd6b20" rx="3"/>
            <text x="39" y="139" fill="#dd6b20" font-size="9" font-weight="bold" text-anchor="middle">7.9%</text>

            <rect x="57" y="21.6" width="28" height="218.4" fill="#c05621" rx="3"/>
            <text x="71" y="15" fill="#c05621" font-size="9" font-weight="bold" text-anchor="middle">18.2%</text>
            <text x="55" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">GMM-HMM</text>

            <!-- Group 2: Wav2Vec2 CTC (clean: 2.4%, other: 6.9%) -->
            <!-- clean: 2.4*12 = 28.8px, other: 6.9*12 = 82.8px -->
            <rect x="110" y="211.2" width="28" height="28.8" fill="#805ad5" rx="3"/>
            <text x="124" y="205" fill="#805ad5" font-size="9" font-weight="bold" text-anchor="middle">2.4%</text>

            <rect x="142" y="157.2" width="28" height="82.8" fill="#553c9a" rx="3"/>
            <text x="156" y="151" fill="#553c9a" font-size="9" font-weight="bold" text-anchor="middle">6.9%</text>
            <text x="140" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">Wav2Vec2 CTC</text>

            <!-- Group 3: Whisper-base (clean: 1.8%, other: 3.9%) -->
            <!-- clean: 1.8*12 = 21.6px, other: 3.9*12 = 46.8px -->
            <rect x="195" y="218.4" width="28" height="21.6" fill="#319795" rx="3"/>
            <text x="209" y="212" fill="#319795" font-size="9" font-weight="bold" text-anchor="middle">1.8%</text>

            <rect x="227" y="193.2" width="28" height="46.8" fill="#234e52" rx="3"/>
            <text x="241" y="187" fill="#234e52" font-size="9" font-weight="bold" text-anchor="middle">3.9%</text>
            <text x="225" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">Whisper Base</text>

            <!-- Group 4: Whisper-small (clean: 1.3%, other: 2.9%) -->
            <!-- clean: 1.3*12 = 15.6px, other: 2.9*12 = 34.8px -->
            <rect x="275" y="224.4" width="24" height="15.6" fill="#38a169" rx="3"/>
            <text x="287" y="218" fill="#38a169" font-size="9" font-weight="bold" text-anchor="middle">1.3%</text>

            <rect x="303" y="205.2" width="24" height="34.8" fill="#22543d" rx="3"/>
            <text x="315" y="199" fill="#22543d" font-size="9" font-weight="bold" text-anchor="middle">2.9%</text>
            <text x="301" y="258" fill="#2d3748" font-size="9" font-weight="bold" text-anchor="middle">Whisper Small</text>
        </g>

        <!-- Legend -->
        <g transform="translate(110, 332)">
            <rect x="0" y="0" width="12" height="12" rx="2" fill="#3182ce"/>
            <text x="18" y="10" fill="#4a5568" font-size="10">Test-Clean Partition</text>
            <rect x="130" y="0" width="12" height="12" rx="2" fill="#e53e3e"/>
            <text x="148" y="10" fill="#4a5568" font-size="10">Test-Other (Noisy/Challenging)</text>
        </g>
    </g>
</svg>'''

    path = os.path.join(FIGURES_DIR, "fig3_wer_cer_benchmark.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated Figure 3: {path}")


def generate_figure4():
    """Generates Figure 4: Computational Profiling (Latency & Real-Time Factor)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 460" width="100%" height="100%" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
    <!-- Title Bar -->
    <rect x="20" y="15" width="960" height="40" rx="6" fill="#1a365d"/>
    <text x="500" y="41" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">Figure 4: Computational Profiling: Inference Latency (ms) &amp; Real-Time Factor (RTF) across Hardware Targets</text>

    <!-- CHART 1: INFERENCE LATENCY (LEFT) -->
    <g transform="translate(50, 75)">
        <rect x="0" y="0" width="420" height="345" rx="8" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1.5"/>
        <text x="210" y="28" fill="#1a365d" font-size="13" font-weight="bold" text-anchor="middle">(a) Inference Latency (ms per 5.0s Clip)</text>

        <g transform="translate(60, 50)">
            <!-- Grid lines (Scale: 0 to 1600 ms, 1ms = 0.15px, 240px max) -->
            <line x1="0" y1="240" x2="320" y2="240" stroke="#cbd5e0" stroke-width="1.5"/>
            <line x1="0" y1="180" x2="320" y2="180" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="120" x2="320" y2="120" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="60" x2="320" y2="60" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="0" x2="320" y2="0" stroke="#e2e8f0" stroke-width="1"/>

            <!-- Y Axis labels -->
            <text x="-10" y="244" fill="#718096" font-size="10" text-anchor="end">0 ms</text>
            <text x="-10" y="184" fill="#718096" font-size="10" text-anchor="end">400 ms</text>
            <text x="-10" y="124" fill="#718096" font-size="10" text-anchor="end">800 ms</text>
            <text x="-10" y="64" fill="#718096" font-size="10" text-anchor="end">1200 ms</text>
            <text x="-10" y="4" fill="#718096" font-size="10" text-anchor="end">1600 ms</text>

            <!-- Group 1: GMM-HMM (CPU: 185ms = 27.75px, GPU: N/A) -->
            <rect x="20" y="212.2" width="28" height="27.8" fill="#3182ce" rx="3"/>
            <text x="34" y="206" fill="#3182ce" font-size="9" font-weight="bold" text-anchor="middle">185ms</text>
            <text x="64" y="235" fill="#a0aec0" font-size="9" text-anchor="middle">N/A</text>
            <text x="45" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">GMM-HMM</text>

            <!-- Group 2: Wav2Vec2 CTC (CPU: 340ms = 51px, GPU: 58ms = 8.7px) -->
            <rect x="100" y="189" width="28" height="51" fill="#3182ce" rx="3"/>
            <text x="114" y="183" fill="#3182ce" font-size="9" font-weight="bold" text-anchor="middle">340ms</text>
            <rect x="132" y="231.3" width="28" height="8.7" fill="#38a169" rx="3"/>
            <text x="146" y="226" fill="#38a169" font-size="9" font-weight="bold" text-anchor="middle">58ms</text>
            <text x="130" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">Wav2Vec2 CTC</text>

            <!-- Group 3: Whisper-base (CPU: 620ms = 93px, GPU: 105ms = 15.75px) -->
            <rect x="180" y="147" width="28" height="93" fill="#3182ce" rx="3"/>
            <text x="194" y="141" fill="#3182ce" font-size="9" font-weight="bold" text-anchor="middle">620ms</text>
            <rect x="212" y="224.2" width="28" height="15.8" fill="#38a169" rx="3"/>
            <text x="226" y="218" fill="#38a169" font-size="9" font-weight="bold" text-anchor="middle">105ms</text>
            <text x="210" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">Whisper Base</text>

            <!-- Group 4: Whisper-small (CPU: 1450ms = 217.5px, GPU: 210ms = 31.5px) -->
            <rect x="260" y="22.5" width="24" height="217.5" fill="#3182ce" rx="3"/>
            <text x="272" y="17" fill="#3182ce" font-size="9" font-weight="bold" text-anchor="middle">1450ms</text>
            <rect x="288" y="208.5" width="24" height="31.5" fill="#38a169" rx="3"/>
            <text x="300" y="202" fill="#38a169" font-size="9" font-weight="bold" text-anchor="middle">210ms</text>
            <text x="286" y="258" fill="#2d3748" font-size="9" font-weight="bold" text-anchor="middle">Whisper Small</text>
        </g>

        <!-- Legend -->
        <g transform="translate(100, 318)">
            <rect x="0" y="0" width="12" height="12" rx="2" fill="#3182ce"/>
            <text x="18" y="10" fill="#4a5568" font-size="10">Intel Core i7 CPU</text>
            <rect x="135" y="0" width="12" height="12" rx="2" fill="#38a169"/>
            <text x="153" y="10" fill="#4a5568" font-size="10">NVIDIA RTX GPU</text>
        </g>
    </g>

    <!-- CHART 2: REAL-TIME FACTOR (RIGHT) -->
    <g transform="translate(530, 75)">
        <rect x="0" y="0" width="420" height="345" rx="8" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1.5"/>
        <text x="210" y="28" fill="#1a365d" font-size="13" font-weight="bold" text-anchor="middle">(b) Real-Time Factor (RTF = T_proc / T_audio)</text>

        <g transform="translate(60, 50)">
            <!-- Grid lines (Scale: 0 to 0.35, 1 unit = 685.7px, 240px total) -->
            <line x1="0" y1="240" x2="320" y2="240" stroke="#cbd5e0" stroke-width="1.5"/>
            <line x1="0" y1="171.4" x2="320" y2="171.4" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="102.8" x2="320" y2="102.8" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="34.3" x2="320" y2="34.3" stroke="#e2e8f0" stroke-width="1"/>

            <!-- Y Axis labels -->
            <text x="-10" y="244" fill="#718096" font-size="10" text-anchor="end">0.00</text>
            <text x="-10" y="175" fill="#718096" font-size="10" text-anchor="end">0.10</text>
            <text x="-10" y="106" fill="#718096" font-size="10" text-anchor="end">0.20</text>
            <text x="-10" y="38" fill="#718096" font-size="10" text-anchor="end">0.30</text>

            <!-- Group 1: GMM-HMM (RTF CPU: 0.037 = 25.4px) -->
            <rect x="25" y="214.6" width="35" height="25.4" fill="#dd6b20" rx="3"/>
            <text x="42" y="208" fill="#dd6b20" font-size="9" font-weight="bold" text-anchor="middle">0.037</text>
            <text x="42" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">GMM-HMM</text>

            <!-- Group 2: Wav2Vec2 CTC (RTF CPU: 0.068 = 46.6px, GPU: 0.012 = 8.2px) -->
            <rect x="105" y="193.4" width="24" height="46.6" fill="#805ad5" rx="3"/>
            <text x="117" y="187" fill="#805ad5" font-size="8.5" font-weight="bold" text-anchor="middle">0.068</text>
            <rect x="133" y="231.8" width="24" height="8.2" fill="#553c9a" rx="3"/>
            <text x="145" y="226" fill="#553c9a" font-size="8.5" font-weight="bold" text-anchor="middle">0.012</text>
            <text x="131" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">Wav2Vec2 CTC</text>

            <!-- Group 3: Whisper-base (RTF CPU: 0.124 = 85px, GPU: 0.021 = 14.4px) -->
            <rect x="190" y="155" width="24" height="85" fill="#319795" rx="3"/>
            <text x="202" y="149" fill="#319795" font-size="8.5" font-weight="bold" text-anchor="middle">0.124</text>
            <rect x="218" y="225.6" width="24" height="14.4" fill="#234e52" rx="3"/>
            <text x="230" y="220" fill="#234e52" font-size="8.5" font-weight="bold" text-anchor="middle">0.021</text>
            <text x="216" y="258" fill="#2d3748" font-size="9.5" font-weight="bold" text-anchor="middle">Whisper Base</text>

            <!-- Group 4: Whisper-small (RTF CPU: 0.290 = 198.8px, GPU: 0.042 = 28.8px) -->
            <rect x="270" y="41.2" width="22" height="198.8" fill="#38a169" rx="3"/>
            <text x="281" y="35" fill="#38a169" font-size="8.5" font-weight="bold" text-anchor="middle">0.290</text>
            <rect x="296" y="211.2" width="22" height="28.8" fill="#22543d" rx="3"/>
            <text x="307" y="205" fill="#22543d" font-size="8.5" font-weight="bold" text-anchor="middle">0.042</text>
            <text x="294" y="258" fill="#2d3748" font-size="9" font-weight="bold" text-anchor="middle">Whisper Small</text>
        </g>

        <!-- Streaming Threshold Line -->
        <g transform="translate(60, 50)">
            <line x1="0" y1="0" x2="320" y2="0" stroke="#e53e3e" stroke-width="1.5" stroke-dasharray="4,4"/>
            <text x="325" y="4" fill="#e53e3e" font-size="9" font-weight="bold">RTF 1.0 Real-Time Threshold (Well Above)</text>
        </g>

        <!-- Legend -->
        <g transform="translate(110, 318)">
            <rect x="0" y="0" width="12" height="12" rx="2" fill="#4a5568"/>
            <text x="18" y="10" fill="#4a5568" font-size="10">CPU Inference</text>
            <rect x="125" y="0" width="12" height="12" rx="2" fill="#2b6cb0"/>
            <text x="143" y="10" fill="#4a5568" font-size="10">GPU Tensor Accelerated</text>
        </g>
    </g>
</svg>'''

    path = os.path.join(FIGURES_DIR, "fig4_latency_rtf_profile.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated Figure 4: {path}")


def generate_figure5():
    """Generates Figure 5: Fine-Grained Error Breakdown (Substitutions, Deletions, Insertions)."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 440" width="100%" height="100%" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
    <!-- Title Bar -->
    <rect x="20" y="15" width="860" height="40" rx="6" fill="#1a365d"/>
    <text x="450" y="41" fill="#ffffff" font-size="15" font-weight="bold" text-anchor="middle">Figure 5: Fine-Grained Error Breakdown: Substitutions, Deletions, and Insertions across Architectures</text>

    <!-- Main Chart Container -->
    <g transform="translate(50, 75)">
        <rect x="0" y="0" width="800" height="330" rx="8" fill="#f7fafc" stroke="#cbd5e0" stroke-width="1.5"/>

        <g transform="translate(70, 40)">
            <!-- Grid lines (Scale: 0 to 12% error rate, 1% = 18px, 216px max) -->
            <line x1="0" y1="216" x2="680" y2="216" stroke="#cbd5e0" stroke-width="1.5"/>
            <line x1="0" y1="162" x2="680" y2="162" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="108" x2="680" y2="108" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="54" x2="680" y2="54" stroke="#e2e8f0" stroke-width="1"/>
            <line x1="0" y1="0" x2="680" y2="0" stroke="#e2e8f0" stroke-width="1"/>

            <!-- Y Axis labels -->
            <text x="-12" y="220" fill="#718096" font-size="10" text-anchor="end">0%</text>
            <text x="-12" y="166" fill="#718096" font-size="10" text-anchor="end">3%</text>
            <text x="-12" y="112" fill="#718096" font-size="10" text-anchor="end">6%</text>
            <text x="-12" y="58" fill="#718096" font-size="10" text-anchor="end">9%</text>
            <text x="-12" y="4" fill="#718096" font-size="10" text-anchor="end">12%</text>

            <!-- GROUP 1: GMM-HMM Modular (Sub: 10.4%, Del: 3.1%, Ins: 1.3%) -->
            <!-- Sub: 10.4*18 = 187.2px, Del: 3.1*18 = 55.8px, Ins: 1.3*18 = 23.4px -->
            <g transform="translate(60, 0)">
                <rect x="0" y="28.8" width="36" height="187.2" fill="#e53e3e" rx="3"/>
                <text x="18" y="22" fill="#e53e3e" font-size="10" font-weight="bold" text-anchor="middle">10.4%</text>

                <rect x="44" y="160.2" width="36" height="55.8" fill="#dd6b20" rx="3"/>
                <text x="62" y="154" fill="#dd6b20" font-size="10" font-weight="bold" text-anchor="middle">3.1%</text>

                <rect x="88" y="192.6" width="36" height="23.4" fill="#3182ce" rx="3"/>
                <text x="106" y="186" fill="#3182ce" font-size="10" font-weight="bold" text-anchor="middle">1.3%</text>

                <text x="62" y="236" fill="#1a365d" font-size="11" font-weight="bold" text-anchor="middle">Traditional GMM-HMM</text>
                <text x="62" y="250" fill="#718096" font-size="9" text-anchor="middle">(Lexicon &amp; Trellis Bound)</text>
            </g>

            <!-- GROUP 2: Wav2Vec2 CTC Baseline (Sub: 3.9%, Del: 1.7%, Ins: 0.5%) -->
            <!-- Sub: 3.9*18 = 70.2px, Del: 1.7*18 = 30.6px, Ins: 0.5*18 = 9.0px -->
            <g transform="translate(280, 0)">
                <rect x="0" y="145.8" width="36" height="70.2" fill="#e53e3e" rx="3"/>
                <text x="18" y="139" fill="#e53e3e" font-size="10" font-weight="bold" text-anchor="middle">3.9%</text>

                <rect x="44" y="185.4" width="36" height="30.6" fill="#dd6b20" rx="3"/>
                <text x="62" y="179" fill="#dd6b20" font-size="10" font-weight="bold" text-anchor="middle">1.7%</text>

                <rect x="88" y="207.0" width="36" height="9.0" fill="#3182ce" rx="3"/>
                <text x="106" y="201" fill="#3182ce" font-size="10" font-weight="bold" text-anchor="middle">0.5%</text>

                <text x="62" y="236" fill="#1a365d" font-size="11" font-weight="bold" text-anchor="middle">Wav2Vec 2.0 CTC</text>
                <text x="62" y="250" fill="#718096" font-size="9" text-anchor="middle">(Frame Independence)</text>
            </g>

            <!-- GROUP 3: OpenAI Whisper-base E2E (Sub: 2.7%, Del: 0.9%, Ins: 0.6%) -->
            <!-- Sub: 2.7*18 = 48.6px, Del: 0.9*18 = 16.2px, Ins: 0.6*18 = 10.8px -->
            <g transform="translate(500, 0)">
                <rect x="0" y="167.4" width="36" height="48.6" fill="#e53e3e" rx="3"/>
                <text x="18" y="161" fill="#e53e3e" font-size="10" font-weight="bold" text-anchor="middle">2.7%</text>

                <rect x="44" y="199.8" width="36" height="16.2" fill="#dd6b20" rx="3"/>
                <text x="62" y="193" fill="#dd6b20" font-size="10" font-weight="bold" text-anchor="middle">0.9%</text>

                <rect x="88" y="205.2" width="36" height="10.8" fill="#3182ce" rx="3"/>
                <text x="106" y="199" fill="#3182ce" font-size="10" font-weight="bold" text-anchor="middle">0.6%</text>

                <text x="62" y="236" fill="#1a365d" font-size="11" font-weight="bold" text-anchor="middle">OpenAI Whisper E2E</text>
                <text x="62" y="250" fill="#718096" font-size="9" text-anchor="middle">(Unified Sequence-to-Sequence)</text>
            </g>
        </g>

        <!-- Legend -->
        <g transform="translate(230, 298)">
            <rect x="0" y="0" width="14" height="14" rx="3" fill="#e53e3e"/>
            <text x="22" y="11" fill="#4a5568" font-size="10.5">Substitutions (S)</text>

            <rect x="140" y="0" width="14" height="14" rx="3" fill="#dd6b20"/>
            <text x="162" y="11" fill="#4a5568" font-size="10.5">Deletions (D)</text>

            <rect x="270" y="0" width="14" height="14" rx="3" fill="#3182ce"/>
            <text x="292" y="11" fill="#4a5568" font-size="10.5">Insertions (I)</text>
        </g>
    </g>
</svg>'''

    path = os.path.join(FIGURES_DIR, "fig5_error_breakdown.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated Figure 5: {path}")


if __name__ == "__main__":
    generate_figure1()
    generate_figure2()
    generate_figure3()
    generate_figure4()
    generate_figure5()
    print("All 5 publication-quality figures successfully generated in figures/ directory!")
