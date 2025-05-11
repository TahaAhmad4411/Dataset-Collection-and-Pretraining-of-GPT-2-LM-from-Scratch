# Dataset-Collection-and-Pretraining-of-GPT-2-LM-from-Scratch
Objective: 
The goal of this project is to provide hands-on experience with the end-to-end process 
of collecting domain-specific data, building a dataset, and pretraining a GPT-2 
language model from scratch on the collected dataset. 

I practiced the Data Acquisition, Preprocessing of the data and model training workflows that are critical to language model development.

The project is divided into 2 parts
Part 1: Data Collection
Part 2: Pretraining the GPT-2 Model from Scratch

Part 1: Data Collection 
  The first and the foremost challenge of Data Collection itself is the authencity of the data. It was found out that the most authentic data sources are in-actual the Government-based and Educational websites having the domains of .gov and .edu.

  The second challenge was to respect the robots.txt of the websites. For context, robots.txt are the rules set by the website owners to scrape the data.

  Third challenge was the extraction of data, there are 2 most commone websites I learned that upload all the internet dump
        Common Crawl
        ClueWeb22
  
  After getting the json of all links relevant to .gov.pk, I used BeautifulSoup to extract the data but that approach did bad more than good as the data extracted was almost 770MBs of roughly 12000 links, each creating into a separate .txt file but most of the data I found was garbage.
  Most of these were
    In corrupted HTML format.
    Were in binary format.
    Contained JS based tags
    Non-ASCII characters
    Short lines and Repeated words
    Meaningless information (like Munir 0 1 2 3 4 ... 10)
    
Cleaning this data reduced down to roughly 2 MB and I found a single website that formed 3MB of data with 3.1 million tokens. And that was "pastic.edu.pk"

Now the 2nd step was to feed the cleaned data into GPT-2 model and fine-tune it. 
The model architecture was as follows
vocab_ size: 50,257.
n_embd: 768 (embedding dimension).
n_layer: 24 (number of transformer layers).
n_head: 16 (number of attention heads).
n_positions: 1,024 (context length).

Training Setup:
  The training setup was as follows
    num_train_epochs: 3
    per_device_train_batch_size: 2
    save_steps: 500
    logging_steps: 1
    evaluation_steps: 10
    learning_rate: 5e-5
    The dataset was split into 2069 training examples and 24 validation examples with a block-size of 1024.
  Training Loss:
    The training loss started from 5.7 till 2.49 over the iterations.

The dataset was trained and fine-tuned on simple google colab GPU T4.
