# Debate Intelligence Engine

A sophisticated natural language processing and network analysis system for analyzing international debate sessions, extracting linguistic features, detecting diplomatic alliances, and identifying influential speakers.

## Overview

The Debate Intelligence Engine processes transcripts from international forums (such as UN sessions, parliamentary debates, or multilateral negotiations) to provide deep insights into:

- **Speaker Influence**: Quantifies delegate influence based on speech intensity, frequency, and network centrality
- **Diplomatic Alliances**: Identifies coalition patterns and bloc formation through similarity analysis
- **Debate Dynamics**: Measures cooperation levels, assertiveness, and stance polarization
- **Session Volatility**: Tracks opinion consistency and debate tension across speakers

## Features

### 1. **Text Preprocessing**
- Automatic text normalization and cleaning
- Punctuation removal and whitespace standardization
- Intelligent stopword filtering
- Lowercase conversion for consistency

### 2. **Feature Extraction**
Calculates multiple linguistic and rhetorical indicators per speech:

| Feature | Description |
|---------|-------------|
| **Cooperation Index** | Measures collaborative language (partnership, dialogue, consensus) |
| **Assertive Index** | Quantifies strong, decisive language (must, demand, definitely) |
| **Stance Score** | Normalized ratio of support vs. opposition sentiment |
| **Text Length** | Speech word count for participation analysis |

**Lexical Inventories**: Over 150 curated words across cooperation, assertiveness, support, and opposition categories with weighted intensity values.

### 3. **TF-IDF Vectorization & Similarity Analysis**
- Converts speeches into TF-IDF vectors
- Computes pairwise cosine similarity between delegates
- Identifies speech similarity patterns for alliance detection
- Creates a delegate similarity matrix for network analysis

### 4. **Influence Scoring**
Combines three weighted dimensions:
- **Stance Intensity** (40%): Absolute strength of speaker's positions
- **Speech Ratio** (30%): Proportion of total session participation
- **Centrality** (30%): Average similarity to other delegates' rhetoric

### 5. **Bloc Detection**
- Hierarchical agglomerative clustering on delegate speech similarity
- Configurable number of blocs
- Automatic group assignment based on rhetorical patterns
- Identifies natural diplomatic coalitions

### 6. **Volatility Analysis**
- Calculates standard deviation of stance scores across session
- Measures debate intensity and consensus
- Higher volatility = greater disagreement

### 7. **Alliance Network Visualization**
- Generates interactive network graphs
- Nodes: Delegates
- Edges: Strong similarities (configurable threshold)
- Edge labels: Similarity scores
- Circular layout for clear visualization

### 8. **Comprehensive Reporting**
Automated report generation including:
- Session overview (delegates, speech count)
- Top influential speakers ranked by influence score
- Probable alliances with similarity metrics
- Detected diplomatic blocs with membership
- Average indices across all speakers
- Debate volatility metrics

## Project Structure

```
debate-analyser/
├── src/
│   ├── main.py                 # Pipeline orchestration
│   ├── loader.py               # CSV data ingestion
│   ├── preprocess.py           # Text cleaning and normalization
│   ├── features.py             # Linguistic feature extraction
│   ├── vectorizer.py           # TF-IDF and similarity computation
│   ├── influence.py            # Influence score calculation
│   ├── volatility.py           # Debate volatility metrics
│   ├── bloc_detector.py        # Hierarchical clustering for bloc detection
│   ├── alliance.py             # Network visualization
│   └── report.py               # Report generation
├── data/
│   └── sample_session.csv      # Sample debate session data
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

## Data Format

Input CSV file should contain:

| Column | Type | Description |
|--------|------|-------------|
| `Speech_ID` | Integer | Unique speech identifier |
| `delegate` | String | Speaker/delegate name or country |
| `Topic` | String | Debate topic or agenda item |
| `Speech_Text` | String | Full speech transcript |

### Example:
```csv
Speech_ID,delegate,Topic,Speech_Text
1,Iran,Cyber Warfare,"This committee must stop hiding..."
2,Sweden,Cyber Warfare,"We strongly believe dialogue and multilateral..."
```

## Installation

### Requirements
- Python 3.8+
- pip or conda

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd debate-analyser
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Required packages:**
   - pandas >= 1.3.0
   - scikit-learn >= 0.24.0
   - networkx >= 2.5
   - matplotlib >= 3.3.0
   - numpy >= 1.19.0

## Usage

### Quick Start

```bash
cd src
python main.py
```

### Detailed Workflow

The pipeline executes in this order:

```python
# 1. Load debate session data
data = load_data("./data/sample_session.csv")
df = pd.DataFrame(data)

# 2. Preprocess speeches (clean text, remove stopwords)
df = preprocess_dataframe(df)

# 3. Extract linguistic features
df = add_features(df)

# 4. Compute delegate similarity via TF-IDF
delegates, similarity_matrix = delegate_similarity(df)

# 5. Detect diplomatic blocs
blocs = detect_blocs(delegates, similarity_matrix, num_blocs=2)

# 6. Calculate influence scores
influence_table = calculate_influence(df, similarity_matrix)

# 7. Measure debate volatility
volatility = calculate_volatility(df)

# 8. Generate comprehensive report
generate_report(df, delegates, similarity_matrix, influence_table, volatility, blocs)

# 9. Visualize alliance networks
plot_alliance_network(delegates, similarity_matrix)
```

### Custom Configuration

Modify parameters in `main.py`:

```python
# Adjust number of blocs
blocs = detect_blocs(delegates, similarity_matrix, num_blocs=3)

# Influence weighting (alpha + beta + gamma must = 1.0)
# Currently: 40% intensity, 30% speech ratio, 30% centrality
influence_table = calculate_influence(df, similarity_matrix, 
                                      alpha=0.4, beta=0.3, gamma=0.3)

# Alliance detection threshold
plot_alliance_network(delegates, similarity_matrix, threshold=0.7)
```

## Key Algorithms

### Stance Score Calculation
$$\text{Stance Score} = \frac{\text{Support Words} - \text{Opposition Words}}{\text{Support Words} + \text{Opposition Words} + \epsilon}$$

- Ranges from -1 (fully opposed) to +1 (fully supportive)
- ε = 0.0000001 prevents division by zero

### Influence Score
$$I = \alpha \cdot |S| + \beta \cdot \frac{N_s}{N_{total}} + \gamma \cdot C$$

Where:
- $S$ = Mean stance score (intensity)
- $N_s$ = Speaker's speech count
- $N_{total}$ = Total speeches
- $C$ = Average cosine similarity to all delegates

### Similarity Matrix
Based on cosine similarity of TF-IDF vectors:
$$\text{Similarity}(d_i, d_j) = \frac{V_i \cdot V_j}{||V_i|| \cdot ||V_j||}$$

### Bloc Detection
Hierarchical agglomerative clustering with:
- Distance metric: 1 - Cosine Similarity
- Linkage criterion: Average (UPGMA)
- Pre-computed distance matrix

## Output Files

### Generated During Execution

- **`processed_data.csv`**: Enhanced dataset with all calculated features
  - Includes Cooperation Index, Assertive Index, Stance Score, Text Length
  
### Console Report
- Session statistics
- Top 5 influential delegates
- Detected alliances (similarity > 0.7)
- Diplomatic blocs with members
- Average indices and volatility

### Visualizations
- **Alliance Network Graph**: Interactive network showing delegate connections

## Sample Output

```
================ Debate Intelligence Engine Report ================

Total Delegates: 10
Total Speeches: 10
Debate Volatility Index: 0.4823

Top Influential Delegates:
     delegate  influence_score
0        Iran           0.6234
1     Germany           0.5891
2      Sweden           0.5447
3      Canada           0.4923
4        China           0.4756

Probable Alliances (Similarity > 0.7):
- Canada ↔ Norway (Similarity: 0.78)
- Sweden ↔ Norway (Similarity: 0.75)

Detected Blocs:
Bloc 1: Iran, North Korea, China
Bloc 2: Sweden, Canada, Germany, USA, Brazil, Maldives, Norway

Average Cooperation Index: 0.0847
Average Assertiveness Index: 0.1203
Average Stance Score: -0.0156
```

## Use Cases

1. **Diplomatic Analysis**: Understand coalition formation in multilateral forums
2. **Policy Research**: Analyze stance positions and opposition patterns
3. **Debate Scoring**: Quantify speaker influence and participation
4. **Conflict Studies**: Monitor escalation through volatility metrics
5. **Network Analysis**: Visualize political/diplomatic relationships
6. **AI Debates**: Analyze synthetic debate transcripts

## Customization

### Add Custom Lexicons

Modify word lists in `features.py`:

```python
COOPERATION_WORDS = {
    "customize": 2,
    "your_word": 3,
    # ... more words
}
```

### Adjust Feature Weights

In `influence.py`, modify the alpha, beta, gamma parameters to prioritize different influence dimensions.

### Change Similarity Threshold

Modify threshold in `alliance.py` (default 0.7) or adjust in `main.py` call.

## Performance Considerations

- **Data Size**: Optimized for 100-10,000 speeches
- **Computational Complexity**: O(n²) for similarity matrix calculation
- **Memory Usage**: Similarity matrix stores dense matrix ~(n_delegates²) floats
- **Execution Time**: ~1-5 seconds for typical session (10-100 speakers)

## Limitations & Future Enhancements

### Current Limitations
- Word-level analysis (no multi-word phrases)
- Language: English only
- No temporal analysis (treats all speeches equally)
- Static word weights (no TF-IDF for feature words)

### Planned Enhancements
- Multi-language support with translation
- Temporal dynamics (speech evolution over time)
- Sentiment analysis integration
- Speaker emotion detection
- Cross-session trend analysis
- Interactive dashboard
- API endpoints

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Submit a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Citation

If you use this system in academic research, please cite:

```bibtex
@software{debate_intelligence_engine,
  title={Debate Intelligence Engine: Automated Analysis of International Debate Sessions},
  year={2026},
  url={https://github.com/yourusername/debate-analyser}
}
```

## Contact & Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [your-email@example.com]

## Changelog

### Version 1.0 (Current)
- Initial release with core analysis pipeline
- TF-IDF similarity computation
- Hierarchical clustering for bloc detection
- Network visualization
- Influence scoring algorithm
- Comprehensive reporting system

---

**Disclaimer**: This tool performs computational analysis of debate transcripts. Results should be interpreted with domain expertise and not taken as definitive political assessments. The system reflects patterns in word usage and speech similarity, not comprehensive geopolitical analysis.
