# Setup

## Project setup
Clone the repository from the CLI by running:

```
git clone https://github.com/stetai352/LLM-evaluation-refusal-consistency.git
```

Activate your virtual environment...

... on Windows:
```
python -m venv .venv
.\.venv\Scripts\activate
```

... on Mac or Linux:
```
python -m venv .venv
source .venv/bin/activate
```

Install the necessary dependencies:

```
pip install -r requirements.txt
```

## Mistral setup
Install optional dependencies that Mistral API requires:
```
pip install mistral mistralai
```

This is by default already included in the `requirements.txt`.
Then add a Mistral API key. 

For example, in Linux:
```
export MISTRAL_API_KEY=<your-api-key>
```


## llama3.2 setup (obsolete)
To install Ollama's Llama 3.2, install Ollama using the package manager of your choosing, then run
```
ollama pull llama3.2:3b
```

You might have to activate the service by running `ollama serve`. Verify its functionality by running `ollama -v`.

llama3.2 has 3.2 billion parameters and supports a context window of 131,072 tokens.

To run the model in the terminal, run
```
ollama run llama3.2:3b
```

For more detailled info, e.g. on how to uninstall the model, see Real Python's [Ollama guide](https://realpython.com/ollama/).


## Execution

Run the evaluation in the terminal using
```
inspect eval <task> --model <model>
```
where `<model>` is the evaluated LLM.