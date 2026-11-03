"""Completed rounds and independent replay through Chromium and real HTTP."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_round_and_keyboard_replay(page: Page, live_server, monkeypatch):
    """Real rules produce a loss, then a keyboard replay produces a win."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    page.goto(live_server)
    expect(page.get_by_text("Starter: game rules not built yet.")).to_have_count(0)
    page.get_by_role("button", name="Rock", exact=True).click()
    choices = page.get_by_label("This round’s choices")
    expect(choices.locator(".choice-value")).to_have_text(["Rock ✊", "Paper ✋"])
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "lose")
    expect(
        page.get_by_role("heading", name="Computer wins", exact=True)
    ).to_be_visible()

    scissors = page.get_by_role("button", name="Scissors", exact=True)
    scissors.focus()
    scissors.press("Enter")
    expect(choices.locator(".choice-value")).to_have_text(["Scissors ✌", "Paper ✋"])
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "win")
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Computer wins", exact=True)).to_have_count(
        0
    )
