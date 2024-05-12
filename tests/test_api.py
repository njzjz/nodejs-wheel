from __future__ import annotations

from nodejs_wheel import (
    node,
    npm,
    npx,
)

return_code0 = node(["--version"])
return_code1 = npm(["--version"])
return_code2 = npx(["--version"])
assert return_code0 == 0
assert return_code1 == 0
assert return_code2 == 0

completed_process0 = node(["--version"], return_completed_process=True)
completed_process1 = npm(["--version"], return_completed_process=True)
completed_process2 = npx(["--version"], return_completed_process=True)

assert completed_process0.returncode == 0
assert completed_process1.returncode == 0
assert completed_process2.returncode == 0
