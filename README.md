# rag-project

This project provides an interface to query the  dataset using a vector store index. It includes enhanced logging with color coding for better readability.

## Requirements

- Python 3.6+
- OpenAI API Key

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/harshrajdabhi/rag-project
    cd rag-project
    ```

2. **Create a Virtual Environment and Activate It**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Set Up OpenAI API Key**

    You need an OpenAI API key to use this code. Set the API key as an environment variable:

    ```bash
    export OPENAI_API_KEY='your-openai-api-key'
    ```

    On Windows, use:

    ```bash
    set OPENAI_API_KEY='your-openai-api-key'
    ```

## Running the Code

1. **Prepare the Data Directory**

    Ensure that you have a directory named `data` with the documents you want to load and index.

2. **Run the Script**

    ```bash
    python starter.py
    ```

    This will start the query interface. You can type your questions about Calidad, and the responses will be logged and displayed.

## Logging

The code includes enhanced logging with color coding. The log levels and their corresponding colors are:

- **INFO**: Green
- **QUESTION**: Blue
- **RESPONSE**: Purple
- **WARNING**: Yellow
- **ERROR**: Red
- **CRITICAL**: Red with white background

## Exiting the Interface

To exit the query interface, type `q` and press Enter.

## Project Structure

- `starter.py`: Main script to run the query interface.
- `data/`: Directory containing the documents to be loaded and indexed.
- `storage/`: Directory where the index is stored.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by submitting issues or pull requests. Happy querying!
