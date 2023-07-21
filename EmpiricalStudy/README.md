# Empirical Study
Here lists RQ results and other datasets used in our paper.

### RQ1

A fine-grained manual evaluation was conducted on 100 samples with unit tests from TransCoder-test dataset. The generated results of models are placed in `./rq1`. The results show that the models are most likely to make mistakes on API, followed by Syntactic Structure. Supervised approaches are more likely to make mistakes on Symbol.

| Task:<br>Java→C++            | CodeBERT | CodeT5 | TransCoder | TransCoder-ST |
|---------------------|----------|--------|------------|---------------|
| Semantic            | 67       | 80     | 75         | 79            |
| API                 | 86       | 92     | 82         | 85            |
| Syntactic Structure | 89       | 96     | 95         | 100           |
| Keyword             | 94       | 98     | 97         | 99            |
| Identifier          | 99       | 99     | 100        | 100           |
| Symbol              | 90       | 94     | 100        | 99            |

### RQ2

The BLEU and EM scores of CodeT5 on exisiting benchmarks are displayed here. We found that current datasets contain too many simple and naive translation pairs, leading to very high BLEU and EM scores. The generated results of models are placed in `./rq2`.

| Model:<br>CodeT5 | Task\Metric | BLEU  | EM    |
|------------------|-------------|-------|-------|
| CodeXGLUE        | Java→C#     | 91.46 | 68.1  |
|                  | C#→ Java    | 92.42 | 72.6  |
| TransCoder-test  | Java→C++    | 90.47 | 32.17 |
|                  | C++→ Java   | 90.25 | 37.03 |
| XLCoST-m         | Java→C++    | 93.48 | 51.1  |
|                  | C++→ Java   | 93.29 | 51.2  |

## Datasets 

### CodeXGLUE
Data of code translation subtask in [CodeXGLUE](https://microsoft.github.io/CodeXGLUE/) benchmark. All the code data are tokenized to achieve consistency on calculation method of BLEU and CodeBLEU.

### XLCoST-m
`Method level` paralle dataset extracted from [XLCoST](https://github.com/reddy-lab-code-research/XLCoST), which only supports snippet and program level code translation originally. The train set of XLCoST-m is used for training supervised model CodeBERT and CodeT5.

### TransCoder-test
The test dataset of [TransCoder](https://github.com/facebookresearch/CodeGen/tree/main/data/test_dataset). For Java-C++ translations, we catagorize the test set into three levels, placed in `transcoder-test-catagorized` folder.

### Statistics
|Datasets|Train |Valid|Test |Languages|
|---|:-:|:-:|:-:|:-:|
|CodeXGLUE|10,253|499  |1,000|Java, C#|
|XLCoST-m|8,389 |500  |1,000|Java, C++, Python, C#, JavaScript|
|TransCoder-test|- |470  |948|Java, C++, Python|


