from tokened.sources import mathiot


def test_mathiot(monkeypatch, tmpdir):
    mathiot.Version1()
