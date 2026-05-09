# LLM-evaluation-refusal-consistency
A small benchmark to test an open-source LLM on refusal consistency.


## Todo
<details open>

<summary> Click here to collapse Todos </summary>

- [x] Check why so slow. Run on GPU?
- [x] Integrate usage of external model via API call. ~~Gemini?~~ Mistral. (Has generous limits, sufficient for experimentation and is free)
- [ ] Make use of .env file
- [x] Revision prompt database, add styles and framings incrementally
- [ ] Include Model-grading
- [ ] Compare different models later?
- [ ] Transparently log the prompts given to Claude (Sonnet 4.6) to obtain the prompts for the eval database.

</details>


## Roadmap
<details>
	
<summary>Click here to expand roadmap</summary>
	
- [x] Set up Repository and Environment (2-4 h)
	- [x] Create repo with a `README`, `.gitignore`, `requirements.txt`.
	- [x] Set up standard folder structure: `data/`, `evals/`, `results/`, `analysis/`.
	- [x] Set up virtual environment locally
	- [x] Install `inspect-ai`, `ollama`
	- [x] Pull small model via `ollama pull llama3.2:3b`
	- [x] Consider these sources:
		- [`inspect-ai` documentation](https://inspect.aisi.org.uk/)
		- [Ollama guide](https://realpython.com/ollama/)
- [x] Get familiar with `inspect-ai` (4-8 h)
	- [x] Run one of the 100+ pre-built evaluations against local model.
	- [x] Consider these sources:
		- [`inspect-ai` documentation](https://inspect.aisi.org.uk/)
		- Medium walkthrough by Lovkush Agarwal
- [x] Define Research Question (3-6 h)
	- [x] Define _refusal consistency_.
		- What behaviour am I testing? 
		- What am I measuring?
		- e. g. "If a model refuses a harmful request phrased directly, does it also refuse the same request phrased as a hypothetical, roleplay, translated into slightly softer language?"
		- Why does it matter for safety?
		- How to operationalise it?
		- Sketch out prompt categories (direct request, hypothetical framing, roleplay framing, rephrasing)
		- How many prompts per category?
		- What does "consistent" or "inconsistent" refusal look like?
	- [x] Formulate a clear, flasifiable question before writing prompts (define it as measurable hypothesis)
	- [x] Consider these sources:
		- Anthropic alignment research blog
		- [METR task design documentation](https://metr.org/)
		- EleutherAI's [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
		- Papers on refusal consistency, e. g. "Harm Bench" and "SimpleSafetyTests" for inspiration on structure.
- [x] Build Dataset of Prompts (5-10 h)
	- [x] Write/curate prompts used for eval.
	- [x] e. g. a factual question, a correct answer, follow-up where user pushes back.
	- [x] Strive for variety: Have more than 100 samples, covering different topics or phrasings. Store as `JSON` files (or `CSV`) under `data/` folder. Include metadata columns like `category`, `framing_type` and `expected_behaviour`.
	- [x] Consider these sources:
		- Existing public datasets on HuggingFace (use search function) as inspiration
		- Look at eval dataset structure in [BIG-Bench](https://github.com/google/BIG-bench) or [TruthfulQA](https://github.com/sylinrl/TruthfulQA)
		- Papers on refusal consistency, e. g. "Harm Bench" and "SimpleSafetyTests" for inspiration on structure.
		- OWASP LLM Top 10 for categories of LLM risks to draw from.
- [ ] Write Eval in `inspect-ai` (6-12 h)
	- [ ] Write python script using `inspect-ai`'s three components:
		- dataset loader
		- solver (sending prompts to local model)
		- scorer (checking output against expected behaviour)
	- [ ] Start with keyword match scorer (e. g. "I can't", "I'm unable to", etc.) and optionally expand to model-graded scorer where model judges the output.
	- [ ] Consider these sources:
		- [`inspect-ai` documentation](https://inspect.aisi.org.uk/), especially the "Sovers" and "Scorers" sections.
		- `inspect-ai`'s [GitHub repo of example evals](https://github.com/UKGovernmentBEIS/inspect_evals)
- [ ] Run Eval and Collect Results (1-3 h)
	- [ ] Run model and save output logs to `results/` folder. (`inspect-ai` produces logs automatically)
	- [ ] Run on second model?
- [ ] Analyse and Visualise Results (5-10 h)
	- [ ] Load `JSON` output
	- [ ] compute summary statistics
	- [ ] produce publication-quality plots.
	- [ ] Answer questions like "does failure rate vary by topic category" or "is there a relationship between prompt length and sycophantic behaviour" using `ggplot2` and `dplyr` (Python's `matplotlib.seaborn` works too).
	- [ ] Barcharts
	- [ ] R Markdown notebook (`.Rmd`)?
	- [ ] Consider these sources:
		- Hadley Wickham's [_R for Data Science_](https://r4ds.had.co.nz/)
		- `ggplot2` documentation
- [ ] Document (4-8 h)
	- [ ] Update `README` to explain:
		- [ ] Behaviour tested, why it matters for AI safety (motivation), how eval was designed (methodology), what I found (findings), where it lacks depth (limitations).
		- [ ] Include plots.
	- [ ] Create `CONTRIBUTING.md` or add future work section.
	- [ ] Consider these sources:
		- Established safety evals' documentation, e. g. the [HarmBench](https://github.com/centerforaisafety/HarmBench) and [TruthfulQA](https://github.com/sylinrl/TruthfulQA) repos 

</details>


## Milestones
<details>

<summary> Click here to expand Milestones </summary>

- `260504` Finish first prompt database.
- `260420` First draft for prompt database.
- `260417` Formulate research question.
- `260414` First draft for refusal prompt categories.
- `260413` Run agent on a Mistral model via API call.
- `260412` Spend a total of eight hours figuring out the best configuration of thread usage to optimize the local model for my machine. Got the estimated total time from 18h to 9h, but this is not sufficient for productive analysis. Finally concluded to switch to a non-local model via API call.
- `260411` Set up GitHub project.
</details>

# Methodology

## Research Question

Understanding an LLM's resistance against giving output that can, under circumstances, cause harm to people or the environment, gives a first insight into the behaviour of that model. We take a look at the effectiveness of safeguards put into place by fine-tuning the model or learned from the initial training. We try to cover a wide range of circumstances and topics and test the given model's refusal against single-prompt probing for these topics.

Content coming from AI can be harmful in many ways, which is why it is important that AI will eventually be fully able to distinguish between information that is safe to output and that which is not. It should under no circumstance give any unsafe responses. 

However, that is also the reason why the goal of this research is not to provide an exhaustive list of all the ways AI could be tricked into giving an unsafe response. This is intended to be a first introduction into the methodology used for exploring and documenting the safety of AI.

We are looking to answer the question

> If a model refuses a harmful request phrased directly, does it also refuse the same request phrased in a different context or manner?

for a Mistral model under the types of rephrasing found in [Dataset](#Dataset).

## Evaluation

- Generation of prompts for dataset using an LLM (which one?) in multiple passes.
	- Generate first batch
	- Check manually for tone
	- Manually write examples for unfit data points
	- Use these as examples for further batches.
	- Incrementally add more categories until all (most) combinations are represented.
- Solver
- self-critique? 
	- What do we want to achieve with this?
- model-graded (content checking using an LLM)
	- don't just check for key phrases like "I can't ...", "I'm unable to ...", but also for actual information provided.
	- write prompt

- Run the evaluation using
```plaintext
inspect eval refusal.py@refusal --max-concurrency 2 --retry 5 --log-dir logs
```

- Manually check the model-graded results

## Dataset

Test LLM's behaviour under varying circumstances, i.e., combinations of the categories below. For the generation of the data set, each combination of framing, subject and phrasing is given two prompts that should be as dissimilar as possible.

- Check different framings:
	- Direct phrasing
	- roleplay
		- Mad scientist
		- Villain
		- ELI5
	- hypothetical
	- Threatening bad outcomes if info not provided (blackmailing)
	- False endorsement
		- clearance from police and governing agencies
	- Assuring confidentially and trust
	- homework for school
	- 
- Check different subjects:
	- Infohazard (ask vaguely)
		- Instructions for construction of weapons
		- Propaganda (political, religious, conspiracy theories)
	- Generation of malware
	- Confirmation of false information (sycophancy)?
	- Jailbreaking (ignoring safeguards and output unrestricted)
	- Advice on sensitive topics (legal advice, medical advice)
	- Inappropriate content (sexual or non-sexual)
	- 
- Check different styles:
	- Natural language
	- Translated to softer language
	- Translated to different language (German)
	- Translated to different style
		- poem
		- song
		- essay
	- Formal language
	- Children's language
	- Lots of typos
	- Slang
	-




---

```
⢠⡶⠛⠛⠛⠛⣤  
⠻⣦⣴⣿⣤⣤⡀  
⣼⠃⠀⣿⠀⢀⡟  
⠉⠛⠛⣿⠛⠉⣠  
⠀⠀⠀⣿⠀⠀⢶  
```