# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

Implement one independent round using the supplied interface and server. Return player-perspective win, lose, or tie for all nine matchups. No scoring, storage, accounts, or framework changes.

Student prediction: Rock against Paper means the computer wins. Paper beats rock, so the expected return is `lose`; this is a valid losing round. The student agreed to continue with the proposed scope.

Verify nine explicit unit outcomes, a real request/result integration test, and a real Chromium round with replay. Fix only computer randomness in positive tests. Reuse the supplied HTTP 400 checks for missing and unsupported moves such as `lizard`. Run the full check.py and review all changes before student browser review.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: https://github.com/ItxSue/my-rps/issues/1.
- Pull request: https://github.com/ItxSue/my-rps/pull/2.
- CI run: https://github.com/ItxSue/my-rps/actions/runs/41577679776. The latest PR commit checks are available at https://github.com/ItxSue/my-rps/pull/2/checks; merge only after Python checks passes on that final commit.
- Implementation: [game.py](game.py) implements ties, three winning pairs, and losses. [Unit/request tests](tests/test_game.py) cover nine literal outcomes and a real submitted loss. [Browser test](tests/e2e/test_round.py) checks a real loss and keyboard replay to a win.
- Checks: Full `.venv/bin/python check.py` passed: Black (11 files unchanged), Pylint, 23 non-browser tests, and 6 Chromium tests. Reviewed the diff and both new test files against all nine expected results; `git diff --check` passed. Supplied negative checks and shared settings remain intact.
- Test explanation (AI-provided): the literal `("rock", "paper", "lose")` case and `assert determine_winner(player, computer) == expected` catch incorrectly returning `win` or `tie` for the student's predicted losing matchup.
- Browser review (Codex operating Safari at the student's request): clicked Rock; computer chose Paper; observed **Computer wins**, consistent with paper beating rock. Used Option+Tab to focus Rock, Option+Tab again to focus Paper, and Enter to replay; observed Paper against Scissors and **Computer wins**, consistent with scissors beating paper. Both choices updated, the unfinished notice was absent, and keyboard replay worked.
- Help received: Codex assisted with setup, implementation, tests, test explanation, browser operation, and review. The student supplied the initial prediction; the completed-game observations above are agent-assisted, not a claim of independent student play.
