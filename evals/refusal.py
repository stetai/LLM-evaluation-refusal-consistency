from inspect_ai import task, Task
from inspect_ai.dataset import json_dataset
from inspect_ai.solver import chain_of_thought, generate
from inspect_ai.scorer import model_graded_fact


@task
def refusal():

    dataset = json_dataset(
        [
            "data/260422_refusal_direct_hypothetical.json",
            "data/260501_refusal_villain_madscientist_eli5.json",
            "data/260503_refusal_endorsement_blackmail.json",
            "data/260504_refusal_trust_homework.json"
        ],
        input="input",
        target="target",
    )

    return Task(
        dataset=dataset,
        solver = [chain_of_thought(), generate()],
        scorer=model_graded_fact(),
    )