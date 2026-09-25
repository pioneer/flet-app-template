```sh
uv sync
uv run inv run
uv run inv check
```

# Flet App Template

A reusable starting point for small and medium Python applications, not a demo
product. Python 3.13+, Flet 1.x imperative UI, uv, Invoke, pytest, Ruff, Pyright,
standard-library logging, and Flet MCP. Install [uv](https://docs.astral.sh/uv/)
first. The first command installs the selected Python and locked dependencies;
desktop startup also needs the host's GUI libraries and display.

**Branding is unfinished by design.** Replace the neutral crossed-square
[assets/icon.png](assets/icon.png), template names, and `com.example` identifiers
before shipping. Start with [initialize-app](skills/initialize-app/SKILL.md) and
[branding](docs/branding.md). The only UI is the placeholder, title, and readiness
status.

## Commands

All project operations use `uv run inv TASK`; `uv run inv --list` lists tasks and
`uv run inv --help TASK` shows options. Invoke is the only task runner.

| Task | Purpose / prerequisites |
| --- | --- |
| `setup` | Synchronize the locked development environment |
| `run`, `debug` | Desktop hot reload; debug adds application DEBUG and Flet diagnostics |
| `run-web`, `debug-web` | Live Python web server at http://127.0.0.1:8550; `--port=8551` to change |
| `debug-android` | Official device debugging; `--device=ID`, Android SDK/device |
| `debug-ios` | Official device debugging; `--device=ID`, macOS/Xcode/device or simulator |
| `logs-android` | Stream Python logcat; Android platform-tools, optional `--device=ID` |
| `doctor` | Python, uv, Flet, host, and optional tools diagnostics |
| `test`, `lint`, `format`, `format-check`, `typecheck` | pytest, Ruff lint/format, Pyright |
| `check` | Format-check, lint, typecheck, then test; stops on failure |
| `clean` | Remove generated builds/assets/caches; preserve source icon and `.venv` |
| `icon-check`, `icon-placeholder` | Validate icon; regenerate neutral placeholder only if absent |
| `build-local` | Build desktop app for the current host, not cross-compilation |
| `build-web` | Static Pyodide app in `build/web`; optional `--base-url=/prefix/` |
| `serve-web` | Serve existing static output on port 8000; optional `--port=8001` |
| `deploy-web` | Build then AWS CLI S3 sync with `--delete`; see deployment warning |
| `build-android`, `build-android-aab` | APK/AAB on Linux, Windows, or macOS; Android/JDK tools |
| `build-ios`, `build-ios-simulator` | macOS only; IPA needs signing, simulator is unsigned |
| `build-windows` | Windows only; Visual Studio C++ desktop toolchain |
| `build-linux` | Linux only; compiler, CMake, Ninja, GTK development libraries |
| `build-macos` | macOS only; Xcode and CocoaPods |

Flet downloads its supported Flutter SDK when necessary. Native builds also need
platform SDKs and may download substantial artifacts. Build artifacts are not
automatically signed for public distribution. Full host and signing requirements
are in [development](docs/development.md).

## Documentation

- [Architecture and boundaries](docs/architecture.md)
- [Development, dependencies, and builds](docs/development.md)
- [Debugging, tracebacks, and platform logs](docs/debugging.md)
- [Testing and quality gates](docs/testing.md)
- [Verified Flet and MCP workflow](docs/flet.md)
- [Branding and canonical icon](docs/branding.md)
- [Static web and S3 deployment](docs/deployment.md)
- [Agent conventions](AGENTS.md) and task-specific [skills](skills/initialize-app/SKILL.md)

Normal CI runs quality checks without GUI or signing secrets. Manually dispatch
the build workflow to exercise web, Android, and native desktop/iOS simulator
targets on matching hosts. No deployment runs automatically.