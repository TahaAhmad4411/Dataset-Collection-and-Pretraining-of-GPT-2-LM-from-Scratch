# Dataset-Collection-and-Pretraining-of-GPT-2-LM-from-Scratch
# GPT-2 Pretraining on Domain-Specific Data (.gov.pk)

## Objective

The goal of this project is to provide hands-on experience with the end-to-end process of:

- Collecting domain-specific data  
- Building a clean and usable dataset  
- Pretraining a GPT-2 language model from scratch on the collected dataset

This project involved practicing critical workflows including **data acquisition**, **preprocessing**, and **model training**, which are essential in modern language model development.

---

## Project Structure

The project is divided into two main parts:

### 🔹 Part 1: Data Collection

#### Challenges Faced:

1. **Data Authenticity**  
   The most authentic content sources were found to be government and educational websites, typically using `.gov` and `.edu` domains.

2. **Respecting `robots.txt`**  
   Each website's `robots.txt` file was respected to ensure ethical scraping practices.

3. **Data Source Identification**  
   Two major open web dumps were explored for large-scale data extraction:
   - [Common Crawl](https://commoncrawl.org/)
   - [ClueWeb22](https://lemurproject.org/clueweb22/)

#### Extraction and Cleaning:

- Extracted `.gov.pk` URLs from Common Crawl JSON using filtering.
- Initial extraction using **BeautifulSoup** yielded ~770MB across ~12,000 text files.
- However, most of this content was unusable due to:
  - Corrupted or binary HTML
  - Embedded JavaScript tags
  - Non-ASCII characters
  - Repetitive meaningless text
  - Extremely short lines

#### Final Usable Dataset:

- After cleaning, the dataset size reduced to ~2MB.
- The most valuable content (~3.1 million tokens) came from a single site:  
  **[pastic.edu.pk](https://www.pastic.edu.pk)**

---

### 🔹 Part 2: GPT-2 Pretraining from Scratch

#### Model Configuration:

| Parameter            | Value     |
|----------------------|-----------|
| `vocab_size`         | 50,257    |
| `n_embd`             | 768       |
| `n_layer`            | 24        |
| `n_head`             | 16        |
| `n_positions`        | 1,024     |

#### Training Setup:

| Hyperparameter                  | Value     |
|----------------------------------|-----------|
| `num_train_epochs`              | 3         |
| `per_device_train_batch_size`   | 2         |
| `save_steps`                    | 500       |
| `logging_steps`                 | 1         |
| `evaluation_steps`              | 10        |
| `learning_rate`                 | 5e-5      |
| `block_size`                    | 1024      |
| `training_examples`             | 2069      |
| `validation_examples`           | 24        |

#### Results:

- **Training loss** reduced from **5.7** to **2.49** over the training iterations.

#### Hardware Used:

- Training was conducted on **Google Colab** using a **T4 GPU** instance.

#### Note: The tokenizers and checkpoints were utilizing a large amount of memory (>3 GB) and Github supports only 25 MB per file to upload. Hence I'm giving the link to google drive to download if required:
#### https://drive.google.com/drive/folders/1CDGgylsq_X9cgAvlkCKNJRxL1EyIZIDf?usp=sharing

---

## Summary

This project successfully demonstrated the workflow for collecting, cleaning, and utilizing domain-specific web data to pretrain a transformer-based language model. It highlighted key practical challenges and addressed them using scalable techniques, with a focus on ethical scraping, quality filtering, and efficient training.



