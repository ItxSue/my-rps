"""RPS-001 outcomes and a submitted round using the real rules."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_all_nine_outcomes(player, computer, expected):
    """Match each literal spec outcome from the player's perspective."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_submitted_losing_round(monkeypatch):
    """A real request displays both choices and the real losing result."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "You chose" in body and "Computer chose" in body
    assert 'class="choice-value">Rock ' in body
    assert 'class="choice-value">Paper ' in body
    assert 'data-outcome="lose"' in body
    assert "Computer wins" in body
    assert "game rules not built yet" not in body
