from hypothesis import given, settings
import hypothesis.strategies as st
from rich.cells import split_text

@settings(max_examples=300, deadline=None)
@given(text=st.text(), pos=st.integers(min_value=0, max_value=1000))
def test_split_text_never_crashes(text, pos):
    split_text(text, pos)
