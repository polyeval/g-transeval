# G-TransEval
This artifact for our paper "On the Evaluation of Neural Code Translation: Taxonomy and Benchmark" includes benchmark suite, results, materials and source code of our automatic unit test tool. We hope this artifact can motivate and help future research on code translation. 

## What's inside the artifact:

1. A benchmark suite of 400 code translation pairs between 5 languages, i.e., Python, C++, Java, C#, and JavaScript (Section V). Located in [./G-TransEval](G-TransEval/README.md)
2. Empirical study material (Section II and III). Located in [./EmpiricalStudy](EmpiricalStudy/README.md)
3. Taxonomy examples and experiment results (Section IV). Located in [./Taxonomy](Taxonomy/README.md)
4. Our automatic unit test tool for G-TransEval. Located in [./TestRunner](TestRunner/README.md)

## Taxonomy
We develop a taxonomy that categorizes code translation tasks into four primary types according to their complexity and knowledge dependence: 
- Token Level (Type 1): Map trivial tokens to their equivalent in the target
- Syntactic Level (Type 2): Migrate syntactic structures based on linguistic rules
- Library Level (Type 3): Migrate library to their equivalent in the target language
- Algorithm Level (Type 4): Reimplement the program in the target language using a different algorithm

More detailed information is at [./Taxonomy](Taxonomy/README.md).

## Benchmark
G-TransEval is the first categorized test set designed to provide fine-grained and extensive evaluations of code translation models. It comprises a total of 400 code translation pairs between 5 language, i.e., Python, C++, Java, C#, and JavaScript. Each test sample are augmented with unit test cases.

Type 1: 125 pairs. Located in `./G-TransEval/Type1`

Type 2: 125 pairs. Located in `./G-TransEval/Type2`

Type 3: 125 pairs. Located in `./G-TransEval/Type3`

Type 4: &nbsp; 25 pairs. Located in `./G-TransEval/Type4`

More detailed information is at [./G-TransEval](G-TransEval/README.md)

## Evaluation Results
We evaluate CodeBERT, CodeT5, TransCoder and TransCoder-ST on G-TransEval.  

### Models checkpoint
|Models          |Source                                        |
|----------------|----------------------------------------------|
|CodeBERT        |https://huggingface.co/microsoft/codebert-base|
|CodeT5          |https://huggingface.co/Salesforce/codet5-base |
|TransCoder      |https://github.com/facebookresearch/CodeGen   |
|TransCoder-ST   |https://github.com/facebookresearch/CodeGen   |

Their translation results are located in [./G-TransEval/Results](G-TransEval/Results/README.md). 

## Unit Test Runner
The automatic unit test tool is placed in `./TestRunner`. See [detailed instruction](TestRunner/README.md) for usages. 



