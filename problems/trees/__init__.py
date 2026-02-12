from __future__ import annotations

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    value: Any = 0
    left: TreeNode | None = None
    right: TreeNode | None = None
