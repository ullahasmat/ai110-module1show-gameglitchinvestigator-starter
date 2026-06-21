from logic_utils import check_guess


def test_check_guess_outcomes():
    # check_guess returns (outcome, message); we only assert the outcome.
    assert check_guess(50, 50)[0] == "Win"       # exact match
    assert check_guess(60, 50)[0] == "Too High"  # guess above secret
    assert check_guess(40, 50)[0] == "Too Low"   # guess below secret
