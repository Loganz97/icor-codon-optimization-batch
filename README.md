# ICOR: Improving Codon Optimization with Recurrent Neural Networks (Batch Implementation)

![ICOR Header](https://raw.githubusercontent.com/Lattice-Automation/icor-codon-optimization/main/docs/assets/images/header.png)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yI0fwaZad5Z-SrIIoh2Czma_9sTzHtKr#scrollTo=Adbc_f7ZORjt)

This repository contains a Google Colab notebook implementation of ICOR (Improving Codon Optimization with Recurrent neural networks), originally developed by [Jain et al. (2023)](https://doi.org/10.1186/s12859-023-05246-8). Our implementation focuses on providing a user-friendly interface for batch processing of DNA sequences using ICOR.

## Features

- Easy-to-use Google Colab interface
- Batch processing of multiple sequences
- Support for both DNA and amino acid input sequences
- Downloadable results in CSV format

## How to Use

1. Open the notebook in Google Colab using the badge above.
2. Run the cells in order, following the instructions provided.
3. Upload your CSV file with sequences when prompted.
4. Download the results containing optimized sequences.

## Input Format

The input CSV should contain the following columns:
- `Sequence Name`: A unique identifier for each sequence
- `Sequence`: The DNA or amino acid sequence to be optimized

## Output

The tool generates a CSV file with the following columns:
- `Sequence Name`: The original identifier
- `Original Sequence`: The input sequence
- `Optimized Sequence`: The ICOR-optimized sequence

## Dependencies

The notebook automatically sets up the following dependencies:
- Python 3.9+
- Biopython
- NumPy
- ONNX Runtime (version 1.12.0)
- Pandas

## Acknowledgments

This implementation is based on the original ICOR work by Jain et al. We acknowledge their significant contributions to the field of codon optimization. For more details on the underlying algorithm and its performance, please refer to the original paper:

Jain, R., Jain, A., Mauro, E. et al. ICOR: improving codon optimization with recurrent neural networks. BMC Bioinformatics 24, 132 (2023). https://doi.org/10.1186/s12859-023-05246-8

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues related to this batch implementation, please open an issue in this GitHub repository.

For inquiries about the original ICOR algorithm, please contact the original authors as specified in their paper.
