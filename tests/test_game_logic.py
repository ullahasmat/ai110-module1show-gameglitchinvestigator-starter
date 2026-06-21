from logic_utils import check_guess, parse_guess, update_score


def test_check_guess_outcomes():
    # check_guess returns (outcome, message); we only assert the outcome.
    assert check_guess(50, 50)[0] == "Win"       # exact match
    assert check_guess(60, 50)[0] == "Too High"  # guess above secret
    assert check_guess(40, 50)[0] == "Too Low"   # guess below secret


def test_hint_messages_point_the_right_way():
    # A guess that's too high should tell the player to go LOWER, and vice versa.
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


def test_wrong_guess_does_not_change_score():
    # Neither Too High nor Too Low should move the score.
    assert update_score(50, "Too High", 3) == 50
    assert update_score(50, "Too Low", 4) == 50


def test_first_guess_win_returns_100():
    # Winning on the first attempt awards the full 100 points.
    assert update_score(0, "Win", 1) == 100


# --- Challenge 1: edge-case inputs to parse_guess ---

def test_parse_guess_rejects_non_numeric():
    # Letters should be rejected gracefully, not crash the game.
    assert parse_guess("abc") == (False, None, "That is not a number.")


def test_parse_guess_rejects_empty_input():
    # Submitting an empty box should be rejected, not treated as a number.
    assert parse_guess("") == (False, None, "Enter a guess.")


def test_parse_guess_accepts_negative_number():
    # Negative ints are out of range but must still parse cleanly.
    assert parse_guess("-7") == (True, -7, None)


def test_parse_guess_truncates_decimal():
    # "3.9" should truncate to int 3 via int(float(...)), not raise.
    assert parse_guess("3.9") == (True, 3, None)


def test_parse_guess_handles_large_number():
    # Python ints are unbounded, so very large input should not overflow.
    assert parse_guess("1000000000") == (True, 1000000000, None)
