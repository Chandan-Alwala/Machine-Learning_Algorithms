# ID3 Variant Partitioning Tool

## Overview

This Python script implements a variant of the ID3 algorithm for partitioning datasets based on attribute values. The program takes as input a dataset file and a partition file, determines which partition to split, and identifies the attribute for the split. It then produces a new partition file based on the split.

## Usage

```bash
python id3variant.py <dataset_file> <input_partition_file> <output_partition_file>
```

- `<dataset_file>`: Path to the dataset file containing a matrix of integers. The last column represents the target attribute, which is binary (0 or 1).
- `<input_partition_file>`: Path to the input partition file describing the initial partitioning of the dataset.
- `<output_partition_file>`: Path to the output partition file where the new partitioning will be written.

### Example

```bash
python id3variant.py dataset-1.txt partition-1.txt partition-2.txt
```

## Input Files

### Dataset File Format

The dataset file should contain a matrix of integers where each row represents an instance, and the last column is the binary target attribute (0 or 1). Each attribute can have values 0, 1, or 2.

### Partition File Format

The partition file specifies the initial partitioning of the dataset. Each line represents a partition, starting with a unique partition ID followed by instance IDs separated by spaces.

## Output

The program will print a message indicating which partition was replaced and with what partitions, along with the attribute used for the split. The new partitioning will be written to the output partition file.

## Dependencies

The script relies on Python 3.x. No additional external libraries are required.

## Notes

- The script assumes that an attribute has no more than 3 distinct values (0, 1, or 2).
- The target attribute is binary (0 or 1).
- Partition IDs in the input file must be unique.


