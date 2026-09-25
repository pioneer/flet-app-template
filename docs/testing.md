# Testing

`uv run inv check` runs, in order, Ruff format-check, Ruff lint, Pyright, and
pytest. It stops at the first failure and preserves command failure status.
`uv run inv format` is the only modifying quality task. Run individual tasks to
iterate; use pytest's `-k` through `uv run pytest -k NAME` for a one-off focused
diagnostic, not a second maintained task interface.

Tests do not open a window, require AWS, or build Flutter. Current coverage checks
settings parsing, pure readiness decisions, side-effect-free entry point,
imperative view construction, Flet event failure tracebacks, sanitized logging,
Invoke host selection/command contracts, mobile debug marker cleanup, and S3
deployment destination arguments. Flet event tests use pinned internals to verify
the actual failure path; revisit them on a Flet upgrade.

For new behavior, prefer small domain/service tests with fakes for external I/O.
Add success and meaningful failure cases, cancellation/timeouts when relevant,
and verify no sensitive values appear in logs. Keep UI tests about state and
behavior, not incidental control ordering. Do not mock the decision under test.

Before publishing, also run a real target build and launch it. Unit tests cannot
prove native plugin availability, platform permissions, icon appearance, signing,
or browser/Pyodide compatibility. Check desktop/mobile viewport sizes and inspect
the packaged output, not just a development server. Manual CI build artifacts are
build smoke tests, not store certification.