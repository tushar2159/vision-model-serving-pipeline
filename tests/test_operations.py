import sys

import pytest
import torch

from vision_serving import cli
from vision_serving.evaluate import evaluate
from vision_serving.metrics import validate_response
from vision_serving.train import train
from vision_serving.utils import load_config, resolve_device, set_seed


def test_evaluation_and_response_contract():
    result = evaluate()
    assert result == {"contract_valid": True}
    assert not validate_response({"task": "classification"})


def test_serving_repository_rejects_training():
    with pytest.raises(RuntimeError, match="task-specific"):
        train()


def test_configuration_and_runtime_utilities(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text("seed: 7\n")
    assert load_config(path) == {"seed": 7}
    set_seed(7)
    first = torch.rand(1)
    set_seed(7)
    assert torch.equal(first, torch.rand(1))
    assert resolve_device("cpu").type == "cpu"


@pytest.mark.parametrize("command", ["prepare", "evaluate", "predict", "self-check"])
def test_cli_commands(command, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["vision-serving", command])
    cli.main()
    assert capsys.readouterr().out
