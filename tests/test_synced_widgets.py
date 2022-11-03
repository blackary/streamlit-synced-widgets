def test_import():
    import streamlit_synced_widgets as stc

    assert stc.checkbox
    assert stc.radio
    assert stc.selectbox
    assert stc.slider
    assert stc.multiselect
    assert stc.date_input
    assert stc.text_input
    assert stc.text_area
    assert stc.number_input
