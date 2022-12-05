from dataclasses import dataclass
from base.result import Result


@dataclass
class FaceResult:
    status: Result
    url: str
    error: str
