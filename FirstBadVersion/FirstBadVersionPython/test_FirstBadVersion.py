from pytest import MonkeyPatch

from . import FirstBadVersion
from .FirstBadVersion import Solution


def test_isBadVersion_when_n1_and_bad1(monkeypatch: MonkeyPatch):
    def mock_isbadVersion(version: int) -> bool:
        return version >= 1
    monkeypatch.setattr(FirstBadVersion, "isBadVersion", mock_isbadVersion)
    assert Solution().firstBadVersion(1) == 1

def test_isBadVersion_when_n2_and_bad1(monkeypatch: MonkeyPatch):
    def mock_isbadVersion(version: int) -> bool:
        return version >= 1
    monkeypatch.setattr(FirstBadVersion, "isBadVersion", mock_isbadVersion)
    assert Solution().firstBadVersion(2) == 1

def test_isBadVersion_when_n10_and_bad1(monkeypatch: MonkeyPatch):
    def mock_isbadVersion(version: int) -> bool:
        return version >= 1
    monkeypatch.setattr(FirstBadVersion, "isBadVersion", mock_isbadVersion)
    assert Solution().firstBadVersion(10) == 1

def test_isBadVersion_when_n10_and_bad5(monkeypatch: MonkeyPatch):
    def mock_isbadVersion(version: int) -> bool:
        return version >= 5
    monkeypatch.setattr(FirstBadVersion, "isBadVersion", mock_isbadVersion)
    assert Solution().firstBadVersion(10) == 5

def test_isBadVersion_when_n10_and_bad9(monkeypatch: MonkeyPatch):
    def mock_isbadVersion(version: int) -> bool:
        return version >= 9
    monkeypatch.setattr(FirstBadVersion, "isBadVersion", mock_isbadVersion)
    assert Solution().firstBadVersion(10) == 9

def test_isBadVersion_when_n10_and_bad10(monkeypatch: MonkeyPatch):
    def mock_isbadVersion(version: int) -> bool:
        return version >= 10
    monkeypatch.setattr(FirstBadVersion, "isBadVersion", mock_isbadVersion)
    assert Solution().firstBadVersion(10) == 10