
# Digital Certificate Generator

## Overview

The Digital Certificate Generator is a Python-based tool designed to create personalized digital certificates. This tool automates the generation of certificates by taking user inputs such as names, courses, and completion dates, and producing high-quality digital certificates in various formats.

## Features

- Customizable certificate templates.
- Batch processing for generating multiple certificates at once.
- Supports various output formats (PDF, PNG).
- User-friendly input via CSV files.
- Easy to integrate with other systems via API.

## Requirements

- Python 3.x
- `Pillow` library for image processing
- `reportlab` library for PDF generation

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Digital_Certificate_Generator.git
    cd digital-certificate-generator
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your certificate template. You can create a custom template using any graphic design tool. Ensure that there are placeholders for dynamic text such as names and dates.

2. Prepare your input data. Create a CSV file with columns for the information that needs to be inserted into the certificates (e.g., names, courses, dates).

3. Run the tool:
    ```bash
    python generate_certificates.py -t <template-file> -i <input-csv> -o <output-directory>
    ```

    Replace `<template-file>`, `<input-csv>`, and `<output-directory>` with the actual file paths.

### Example

```bash
python generate_certificates.py -t template.png -i participants.csv -o certificates/
```

## Options

- `-t, --template`: Path to the certificate template file.
- `-i, --input`: Path to the CSV file containing participant data.
- `-o, --output`: Directory where the generated certificates will be saved.
- `-f, --format`: (Optional) Output format (PDF or PNG). Default is PDF.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at www.linkedin.com/in/aravinth-aj.
